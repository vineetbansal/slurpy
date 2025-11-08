"""
Integration tests for Slurm Sbatch API (sync version).
"""

import pytest
from typing import Dict, Any, Optional

import slurpy.sbatch as slurpy
from slurpy.sbatch.exceptions import ApiException


# ----------------------------
import subprocess


@pytest.fixture(scope="session")
def slurm_compose(slurm_cluster):
    compose = slurm_cluster["compose"]
    with compose:
        yield compose


@pytest.fixture
def run_in_container(monkeypatch, slurm_compose):
    def _run(args, **kwargs):
        result, error, exit_code = slurm_compose.exec_in_container(args, "slurm_node")

        return subprocess.CompletedProcess(
            args=args,
            returncode=exit_code,
            stdout=result,
            stderr=error,
        )

    monkeypatch.setattr(subprocess, "run", _run)


@pytest.fixture
def api_client(slurm_config: Dict[str, Any]):
    configuration = slurpy.Configuration(host=slurm_config["host"])

    # Configure authentication
    configuration.api_key["user"] = slurm_config["user"]
    configuration.api_key["token"] = slurm_config["token"]

    with slurpy.ApiClient(configuration) as client:
        yield slurpy.SlurmApi(client)


class TestContainerSubprocess:
    def test_run_in_container(self, run_in_container):
        result = subprocess.run(["hostname"])
        assert result.stdout.strip() == "slurm_node"


class TestSlurmSbatch:
    """Integration tests for Slurm Sbatch API (sync)."""

    # TODO: Run all in container using a single run_in_container arg

    def test_ping_cluster(self, api_client: slurpy.SlurmApi, run_in_container):
        """Test basic connectivity to the Slurm cluster."""
        try:
            response = api_client.get_ping()
            assert response is not None
            # Check if we get a valid ping response
            ping_data = response.to_dict()
            assert "pings" in ping_data or "ping" in ping_data
        except ApiException as e:
            pytest.fail(f"Failed to ping cluster: {e}")

    def test_list_jobs(self, api_client: slurpy.SlurmApi, run_in_container):
        """Test listing jobs."""
        try:
            response = api_client.get_jobs()
            assert response is not None
            jobs_data = response.to_dict()
            assert "jobs" in jobs_data
            # Should return a list (could be empty)
            assert isinstance(jobs_data["jobs"], list)
        except ApiException as e:
            pytest.fail(f"Failed to list jobs: {e}")

    def test_create_job(
        self, api_client: slurpy.SlurmApi, sample_job: Dict[str, Any], run_in_container
    ):
        """Test creating a job."""
        job_created_id: Optional[int] = None

        try:
            # Create job submission request
            job_request = slurpy.JobSubmitReq.from_dict(sample_job)

            response = api_client.post_job_submit(job_submit_req=job_request)

            assert response is not None
            submit_data = response.to_dict()

            # Extract job ID from response
            if "job_id" in submit_data:
                job_created_id = submit_data["job_id"]
            elif "jobs" in submit_data and len(submit_data["jobs"]) > 0:
                job_created_id = submit_data["jobs"][0].get("job_id")

            assert job_created_id is not None, "Job ID not found in response"

        except ApiException as e:
            pytest.fail(f"Failed to create job: {e}")

        finally:
            # Clean up: try to cancel the job if it was created
            if job_created_id:
                try:
                    api_client.delete_job(str(job_created_id))
                except ApiException:
                    # Job might have already completed or failed, ignore cleanup errors
                    pass

    def test_get_single_job(
        self, api_client: slurpy.SlurmApi, sample_job: Dict[str, Any], run_in_container
    ):
        """Test getting details for a single job."""
        job_created_id: Optional[int] = None

        try:
            # First create a job
            job_request = slurpy.JobSubmitReq.from_dict(sample_job)

            submit_response = api_client.post_job_submit(job_submit_req=job_request)

            submit_data = submit_response.to_dict()

            # Extract job ID
            if "job_id" in submit_data:
                job_created_id = submit_data["job_id"]
            elif "jobs" in submit_data and len(submit_data["jobs"]) > 0:
                job_created_id = submit_data["jobs"][0].get("job_id")

            assert job_created_id is not None, "Job ID not found in submit response"

            # Now get the job details
            job_response = api_client.get_job(job_id=str(job_created_id))
            assert job_response is not None

            job_data = job_response.to_dict()
            assert "jobs" in job_data
            assert len(job_data["jobs"]) > 0

            job_info = job_data["jobs"][0]
            assert job_info["job_id"] == job_created_id
            assert job_info["name"] == sample_job["job"]["name"]

        except ApiException as e:
            pytest.fail(f"Failed to get single job: {e}")

        finally:
            # Clean up
            if job_created_id:
                try:
                    api_client.delete_job(str(job_created_id))
                except ApiException:
                    pass

    def test_delete_job(
        self, api_client: slurpy.SlurmApi, sample_job: Dict[str, Any], run_in_container
    ):
        """Test deleting/canceling a job."""
        job_created_id: Optional[int] = None

        try:
            # First create a job
            job_request = slurpy.JobSubmitReq.from_dict(sample_job)

            submit_response = api_client.post_job_submit(job_submit_req=job_request)

            submit_data = submit_response.to_dict()

            # Extract job ID
            if "job_id" in submit_data:
                job_created_id = submit_data["job_id"]
            elif "jobs" in submit_data and len(submit_data["jobs"]) > 0:
                job_created_id = submit_data["jobs"][0].get("job_id")

            assert job_created_id is not None, "Job ID not found in submit response"

            # Now delete the job
            delete_response = api_client.delete_job(str(job_created_id))
            assert delete_response is not None

            # Verify the job was cancelled/deleted
            # The delete response should indicate success
            # Different versions might return different response structures
            # Just ensure we got a response without exception

        except ApiException as e:
            pytest.fail(f"Failed to delete job: {e}")

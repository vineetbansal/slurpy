"""
Shared pytest fixtures for slurpy integration tests.
"""

import time
from pathlib import Path
from typing import Dict, Any
import pytest
from testcontainers.compose import DockerCompose


@pytest.fixture(scope="session")
def slurm_cluster():
    """
    Start a Slurm cluster using Docker Compose.

    Returns connection details for the cluster.
    """
    compose_dir = Path(__file__).parent.parent / "slurm"

    with DockerCompose(
        context=str(compose_dir), compose_file_name="docker-compose.yaml", pull=True
    ) as compose:
        # Wait for services to be healthy
        # compose.wait_for("http://localhost:6820")

        # Get the exposed port for the REST API
        rest_api_port = compose.get_service_port("slurm_node", 6820)

        # Additional wait to ensure all services are fully ready
        time.sleep(10)

        yield {
            "host": "localhost",
            "port": rest_api_port,
            "base_url": f"http://localhost:{rest_api_port}",
            "compose": compose,
        }


@pytest.fixture
def sample_job() -> Dict[str, Any]:
    """
    Sample job specification for testing.
    """
    return {
        "script": "#!/bin/bash\nsleep 30\necho 'Job completed'\n",
        "job": {
            "current_working_directory": "/home/slurm",
            "environment": ["PATH=/bin/:/usr/bin/:/sbin/"],
            "name": "test_job",
            "ntasks": 1,
            "time_limit": {"set": True, "number": 300},  # 5 minutes
        },
    }

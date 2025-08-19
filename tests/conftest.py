"""
Shared pytest fixtures for slurpy integration tests.
"""

import asyncio
import time
from pathlib import Path
from typing import Dict, Any
import pytest
import pytest_asyncio
from testcontainers.compose import DockerCompose


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


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


@pytest_asyncio.fixture(scope="session")
async def jwt_token(slurm_cluster) -> str:
    """
    Generate a JWT token for the 'slurm' user using scontrol inside the container.
    """
    compose = slurm_cluster["compose"]

    # Execute scontrol command inside the container to generate JWT token
    result, error, exit_code = compose.exec_in_container(
        ["scontrol", "token", "username=slurm"],
        "slurm_node",
    )

    if exit_code:
        raise RuntimeError(f"Failed to extract JWT token from scontrol output: {error}")

    # Parse the token from the output
    # Expected output format: "SLURM_JWT=<token>"
    output = result.strip()
    for line in output.split("\n"):
        if line.startswith("SLURM_JWT="):
            return line.split("=", 1)[1]

    raise RuntimeError(f"Failed to extract JWT token from scontrol output: {output}")


@pytest_asyncio.fixture(scope="session")
async def slurm_config(slurm_cluster, jwt_token) -> Dict[str, Any]:
    """
    Provide complete Slurm configuration for tests.
    """
    return {"host": slurm_cluster["base_url"], "user": "slurm", "token": jwt_token}


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

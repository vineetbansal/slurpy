from pydantic import Field
from typing import TYPE_CHECKING, Optional
from typing_extensions import Annotated

import subprocess
import json

from slurpy.sbatch.api_client import ApiClient

if TYPE_CHECKING:
    from slurpy.sbatch import JobSubmitReq


class Response:
    def __init__(self, d):
        self._d = d

    def to_dict(self):
        return self._d


class SlurmApi:
    @staticmethod
    # TODO: Watch out for exceptions and re-raise as ApiException
    # Add convenience wrappers for runs that should add --json
    # In those cases, perhaps better to parse out the results before return.
    def run(cmd, *args, **kwargs):
        cmd_list = [cmd]
        cmd_list.extend(map(str, args))

        for key, value in kwargs.items():
            key_str = f"--{key.replace('_', '-')}"
            if isinstance(value, bool):
                if value:
                    cmd_list.append(key_str)
            else:
                cmd_list.append(f"{key_str}={value}")

        result = subprocess.run(cmd_list, text=True)
        return result

    def __init__(self, api_client: ApiClient | None = None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    def get_ping(self, *args, **kwargs):
        result = self.run("scontrol", "ping", "--json")
        response = Response(json.loads(result.stdout))
        return response

    def get_jobs(self, *args, **kwargs):
        result = self.run("squeue", "--json")
        response = Response(json.loads(result.stdout))
        return response

    def post_job_submit(
        self,
        job_submit_req: Annotated[
            Optional["JobSubmitReq"], Field(description="Job description")
        ] = None,
    ):
        # TODO: Lots of extra args we can/should support!
        extra_args = {}
        if job_name := job_submit_req.job.name:
            extra_args["job-name"] = job_name

        result = self.run(
            "sbatch", "--wrap", job_submit_req.script, "--parsable", **extra_args
        )
        job_id = int(result.stdout.strip())
        response = Response({"job_id": job_id})
        return response

    def delete_job(self, job_id: str):
        result = self.run("scancel", job_id)
        job_id = result.stdout
        response = Response({})
        return response

    def get_job(self, job_id: str):
        result = self.run("squeue", "-j", job_id, "--json")
        response = Response(json.loads(result.stdout))
        return response

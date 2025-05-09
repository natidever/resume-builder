
from fastapi import APIRouter
from ...models import JobExperience

router  =  APIRouter()


@router.post("/job_experience/",tags=["Job Description"])
async def accept_job_experience(job_experience:JobExperience):
    return {"message":"Job experience accepted "}


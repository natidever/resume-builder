
from fastapi import APIRouter
from ...models import JobExperienceCreate,JobExprience
from ...configs.db_config import SessionDep

router  =  APIRouter()


@router.post("/job_experience/",tags=["Job Description"])
async def accept_job_experience(job_experience_create:JobExperienceCreate,session:SessionDep):
    db_job_experiance =JobExprience(**job_experience_create.model_dump(),user_id="1")
    session.add(db_job_experiance)
    session.commit()
    session.refresh(db_job_experiance)
    
    return db_job_experiance


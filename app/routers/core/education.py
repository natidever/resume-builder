
from fastapi import APIRouter
from ...models import EducationCreate,Education
from ...configs.db_config import SessionDep

router  =  APIRouter()


@router.post("/education/",tags=["Education"])
async def accept_education(education_create:EducationCreate,session:SessionDep):
    db_education = Education(**education_create.model_dump(),user_id="1")
    session.add(db_education)
    session.commit()
    session.refresh(db_education)
    return db_education


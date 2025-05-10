
from fastapi import APIRouter
from ...models  import Languages ,LanguagesCreate
from ...configs.db_config import SessionDep
router = APIRouter()

@router.post("/languages/",tags=["Languages"])
async def accept_skills(langauges_create:LanguagesCreate,session:SessionDep):
    db_Languages = Languages(**langauges_create.model_dump(),user_id="1")
    session.add(db_Languages)
    session.commit()
    session.refresh(db_Languages)
    return db_Languages


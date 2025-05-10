
from fastapi import APIRouter
from ...models import SkillsCreate,Skills
from ...configs.db_config import SessionDep
router = APIRouter()

@router.post("/skills/",tags=["Skills"])
async def accept_skills(skils_create:SkillsCreate,session:SessionDep):
    db_skill = Skills(**skils_create.model_dump(),user_id="1")
    session.add(db_skill)
    session.commit()
    session.refresh(db_skill)

    return db_skill


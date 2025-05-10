
from fastapi import APIRouter
from ...models  import PersonalInfoCreate,PersonalInfo
from  ...configs.db_config import SessionDep
router = APIRouter()

@router.post("/personal_information/",response_model=PersonalInfo,tags=["Personal Info"])
async def accept_personal_info(personal_info_create:PersonalInfoCreate,session:SessionDep):
    db_personal_info = PersonalInfo(**personal_info_create.model_dump(),user_id="1")
    session.add(db_personal_info)
    session.commit()
    session.refresh(db_personal_info)
    
    return db_personal_info







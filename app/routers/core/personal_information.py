
from fastapi import APIRouter
from ...models  import PersonalInfo
router = APIRouter()

@router.post("/personal_information/",tags=["Personal Info"])
async def accept_personal_info(personal_info:PersonalInfo):
    return {"message":"personal information accepted "}


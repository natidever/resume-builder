
from fastapi import APIRouter
from ...models import Skills
router = APIRouter()

@router.post("/skills/",tags=["Skills"])
async def accept_skills(skils:Skills):
    return {"message":"Skills  accepted "}


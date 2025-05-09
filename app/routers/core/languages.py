
from fastapi import APIRouter
from ...models  import Language
router = APIRouter()

@router.post("/languages/",tags=["Languages"])
async def accept_skills(skils:Language):
    return {"message":"languages  accepted "}


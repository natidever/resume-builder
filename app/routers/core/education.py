
from fastapi import APIRouter
from ...models import Education

router  =  APIRouter()


@router.post("/education/",tags=["Education"])
async def accept_education(education:Education):
    return {"message":"Education accepted "}


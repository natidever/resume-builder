import os 
from pathlib import Path


from fastapi.templating import Jinja2Templates
from fastapi import     Request,APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from sqlmodel import select
from ...configs.db_config import SessionDep



from ...models import CVData, Education, JobExprience, Languages,PersonalInfo, Skills


router =APIRouter()

# Get the directory of the current file (main.py)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Create static directory if it doesn't exist
# os.makedirs(STATIC_DIR, exist_ok=True)

# Mount static files at the app level instead of router level
STATIC_DIR_TEMPLATE = os.path.join(BASE_DIR, "templates")

# router.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
# router.mount("/static", StaticFiles(directory=STATIC_DIR_TEMPLATE), name="templates")












templates = Jinja2Templates(directory=STATIC_DIR_TEMPLATE)
  

#   for user id featch all the data then give feed it ass a context for the template engine

@router.get("/generate/", response_class=HTMLResponse)
async def read_item(request: Request,session:SessionDep):
    # qery the database
    user_id = "1"
    personal_info =session.exec(
        select(PersonalInfo).where(PersonalInfo.user_id == "1")
    
    ).first()

    job_exp=session.exec(
        select(JobExprience).where(JobExprience.user_id == "1")
    
    ).all()

    education = session.exec(
        select(Education).where(Education.user_id == "1")
    
    ).all()

    skills =session.exec(
        select(Skills).where(Skills.user_id == "1")
    
    ).all()
    languages =session.exec(
        select(Languages).where(Languages.user_id == "1")
    
    ).all()

    context = {
        "request":request,
        "personal_info":personal_info,
        "job_exp":job_exp,
        "education":education,
        "skills":skills,
        "languages":languages

    }
    return templates.TemplateResponse(
        request=request, name="example_cv.html", context=context
    )




























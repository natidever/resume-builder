import os 
from pathlib import Path


from fastapi.templating import Jinja2Templates
from fastapi import     Request,APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request


from ...models import CVData
template = Jinja2Templates("templates")

router =APIRouter()

# Get the directory of the current file (main.py)
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Create static directory if it doesn't exist
os.makedirs(STATIC_DIR, exist_ok=True)

# Mount static files at the app level instead of router level
router.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")



templates = Jinja2Templates(directory="templates")


@router.get("/items/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="example_cv.html", context=CVData
    )
import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles



from .routers.core import cv_generator, education, job_experience, languages, personal_information
from .routers.core import skills
from  .routers.auth import google_auth

from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware

from dotenv import load_dotenv
app = FastAPI()
# Get the directory of the current file (main.py)
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Create static directory if it doesn't exist
os.makedirs(STATIC_DIR, exist_ok=True)

# Mount static files at the app level instead of router level
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

load_dotenv(override=True)



app.add_middleware(SessionMiddleware, secret_key="FAST_API_KEY")


app.include_router(personal_information.router)
app.include_router(job_experience.router)
app.include_router(education.router)
app.include_router(skills.router)
app.include_router(languages.router)
app.include_router(cv_generator.router)
app.include_router(google_auth.router)









@app.get("/")
def read_root():
    return {"message":"server running ....🚀🚀"}



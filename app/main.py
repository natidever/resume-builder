import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv




from .routers.core import cv_generator, education, job_experience, languages, personal_information
from .routers.core import skills
from  .routers.auth import google_auth
from  .configs.db_config import create_db_and_tables, create_user




@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    # create_user()s
    yield

app = FastAPI(lifespan=lifespan)




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



from sqlmodel import create_engine ,Session,SQLModel, text
from fastapi import Depends, FastAPI, HTTPException, Query
from typing import Annotated
from pathlib import Path 
import os

from  ..models import User

# DB Connection

BASE_DIR = Path(__file__).resolve().parent.parent  # This gets the /app directory
DB_DIR = os.path.join(BASE_DIR, "db")

sqlite_file_name = "resume_builder.db"
sqlite_path = os.path.join(DB_DIR, sqlite_file_name)

sqlite_url = f"sqlite:///{sqlite_path}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args,echo=True)


def create_db_and_tables():
    try:
        print(f"Creating database at: {sqlite_path}")  # Debug print

        SQLModel.metadata.create_all(engine)
        with engine.connect() as connection:
            connection.execute(text("PRAGMA foreign_keys=ON"))  
        print("Database tables created successfully")  
    except Exception as e:
        print(f"Error creating database tables: {e}")
        import traceback
        traceback.print_exc()
    


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

def create_user():
    user = User(
        user_id="1",
        email="natidev404@gmail.com",
        profile_picture="urlforimage"
    )
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    print("User created:", user)
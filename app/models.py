from pydantic import BaseModel,EmailStr
from datetime import date 
from sqlmodel import JSON, SQLModel,Field ,Relationship



from typing import Optional

class User(SQLModel,table=True):
   user_id:str| None = Field(default=None ,primary_key=True)
   email:EmailStr
   profile_picture:Optional[str] =None
#    THE FOLLOWING ARE RELATION SHIP
# This use got person info
   personal_info:Optional["PersonalInfo"]=Relationship(back_populates="user",cascade_delete=True)
   job_expriences:list["JobExprience"] = Relationship(back_populates="user",cascade_delete=True)
   educations : list["Education"] = Relationship(back_populates="user",cascade_delete=True)
   languages: list["Languages"] = Relationship(back_populates="user",cascade_delete=True)
   skills : list ["Skills"] = Relationship(back_populates="user",cascade_delete=True)
   

# PersonalInfo

class PersonalInfo(SQLModel ,table=True):
    id:int | None = Field(default=None, primary_key=True)
    first_name:str
    last_name:str
    email:EmailStr
    phone_number:str
    professional_title:str
    professional_description:str
    summary:str
    residence:str
    linkedin:Optional[str]=None
    personal_website:Optional[str]=None
    user_id : int |None = Field(default=None,foreign_key="user.user_id")
    user : User | None = Relationship(back_populates="personal_info")




class PersonalInfoCreate(SQLModel):
    
    first_name:str
    last_name:str
    email:EmailStr
    phone_number:str
    professional_title:str
    professional_description:str
    summary:str
    residence:str
    linkedin:Optional[str]=None
    personal_website:Optional[str]=None

class PersonalInfoRead(PersonalInfoCreate):
    id:int
    user_id:int


# Personal Info end




    



# JobExp
class JobExperienceCreate(SQLModel):
    
    job_title: str
    description: str
    company: str
    start_date: date
    end_date: date
    location: Optional[str] = None


class JobExprience(JobExperienceCreate ,table=True):
    id:int | None=Field(default=None,primary_key=True)
    user_id:int | None = Field(default=None, foreign_key="user.user_id")
    user:User | None = Relationship(back_populates="job_expriences")


class JobExperienceRead(JobExperienceCreate):
     id:int
     user_id:int

     # JobExpend



    


    










# Educati


class EducationCreate(SQLModel):
    institution_name: str  
    degree_type: str       
    field_of_study: str
    description: str
    city: Optional[str] = None
    start_date:date
    end_date: date


class Education(EducationCreate,table=True):
    id:int | None=Field(default=None,primary_key=True)
    user_id : int | None = Field(default=None , foreign_key="user.user_id")
    user : User | None = Relationship(back_populates="educations")

class EducationRead(EducationCreate):
     id:int
     user_id:int






# 


class SkillsCreate(SQLModel):
    skills:list[str] =Field(sa_type=JSON)


class Skills(SkillsCreate,table=True):
    id:int | None=Field(default=None,primary_key=True)
    user_id : int | None = Field(default=None,foreign_key="user.user_id")
    user : User | None = Relationship(back_populates="skills")


class SkillRead(SkillsCreate):
     id:int
     user_id:int

















    
class LanguagesCreate(SQLModel):
  languages:list[str] = Field(sa_type=JSON)
    


class Languages(LanguagesCreate,table=True):
     id:int | None=Field(default=None,primary_key=True)
     languages:list[str] = Field(sa_type=JSON)
     user_id : int | None = Field(default=None,foreign_key="user.user_id")
     user : User | None = Relationship(back_populates="languages",)


class LanguagesRead(LanguagesCreate):
    id:int



















class CVData(BaseModel):
    personal_info: PersonalInfoCreate
    education: list[EducationCreate]
    experience: list[JobExperienceCreate]
    skills: list[SkillsCreate]
    languages: LanguagesCreate
   


    


    # cv data will the data that will be filled when by fetchign from database

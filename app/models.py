from pydantic import BaseModel,EmailStr,HttpUrl
from datetime import date 
from fastapi.templating import Jinja2Templates


from typing import Optional
class PersonalInfo(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    phone_number:str
    professional_title:str
    professional_description:str

    summary:str
    residence:str
    linkedin:Optional[HttpUrl]=None
    personal_website:Optional[HttpUrl]=None

class JobExperience(BaseModel):
    job_title: str
    description: str
    company: str
    start_date: date
    end_date: date
    location: Optional[str] = None


class Education(BaseModel):
    institution_name: str  
    degree_type: str       
    field_of_study: str
    description: str
    city: Optional[str] = None
    start_date:date
    end_date: date

class Skills(BaseModel):
    skills:list[str]
    
class Language(BaseModel):
     languages:list[str]



class CVData(BaseModel):
    personal_info: PersonalInfo
    education: list[Education]
    experience: list[JobExperience]
    skills: list[Skills]
    languages: Skills
   


    


    
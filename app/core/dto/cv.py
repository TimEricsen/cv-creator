from datetime import date
from typing import Union, List
from pydantic import BaseModel, EmailStr

from app.core.enums.cv import LangLevelEnum


class WorkExpCreate(BaseModel):
    company: Union[str, None] = None
    speciality: Union[str, None] = None
    stack: Union[str, None] = None
    work_from: Union[date, None] = None
    work_to: Union[date, None] = None
    responsibilities: Union[str, None] = None


class SkillCreate(BaseModel):
    skill: Union[str, None] = None


class LangCreate(BaseModel):
    lang: Union[str, None] = None
    level: Union[LangLevelEnum, None] = None


class BaseCV(BaseModel):
    full_name: Union[str, None] = None
    speciality: Union[str, None] = None
    salary_from: Union[int, None] = None
    salary_to: Union[int, None] = None
    age: Union[int, None] = None
    location: Union[str, None] = None
    email: Union[EmailStr, None] = None
    telegram: Union[str, None] = None
    about_me: Union[str, None] = None
    work_exp: Union[List[WorkExpCreate], None] = None
    skills: Union[List[SkillCreate], None] = None
    lang: Union[List[LangCreate], None] = None


class CreateCV(BaseCV):
    pass

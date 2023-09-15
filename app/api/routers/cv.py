from fastapi import APIRouter, Depends

from app.core.dto.cv import CreateCV
from app.infrastructure.dao.cv import CVDAO
from app.api.dependencies.cv import dao_provider
from app.core.services.cv import cv_create


router = APIRouter()


@router.post('/create-cv')
async def create_cv(cv: CreateCV, dao: CVDAO = Depends(dao_provider)) -> str:
    return await cv_create(cv, dao)

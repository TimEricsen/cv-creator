from app.core.dto.cv import CreateCV
from app.core.dal.cv import CVCreator


async def cv_create(cv: CreateCV, dao: CVCreator) -> str:
    return await dao.create_cv(cv)

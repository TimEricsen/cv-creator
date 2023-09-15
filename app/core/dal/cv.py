from typing import Protocol

from app.core.dto.cv import CreateCV


class CVCreator(Protocol):
    async def create_cv(self, cv: CreateCV):
        return NotImplementedError

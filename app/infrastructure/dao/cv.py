import json

from validate_email_address import validate_email
from datetime import date

from app.core.message_broker.cv_producer import get_cv_producer
from app.core.dto.cv import CreateCV
from app.core.utils.excpetions.cv import EmailValidationException, SalaryException, UsernameException, \
    WorkDateException


class CVDAO:
    async def create_cv(self, cv: CreateCV) -> str:
        await self._validate_email(cv.email)
        await self._validate_salaries(cv.salary_from, cv.salary_to)
        await self._validate_tg_username(cv.telegram)
        for work in cv.work_exp:
            await self._validate_work_dates(work.work_from, work.work_to)
        cv_prod = get_cv_producer()
        await cv_prod.publish_message(json.loads(cv.json()))
        return 'Thanks, we will send your cv to entered email!'

    async def _validate_email(self, email: str) -> None:
        if not validate_email(email, verify=True):
            raise EmailValidationException

    async def _validate_salaries(self, fs: int, ts: int) -> None:
        if fs > ts:
            raise SalaryException

    async def _validate_tg_username(self, username: str) -> None:
        if not username.startswith('@'):
            raise UsernameException

    async def _validate_work_dates(self, work_from: date, work_to: date) -> None:
        if work_from > work_to:
            raise WorkDateException

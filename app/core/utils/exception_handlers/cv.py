from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.utils.excpetions.cv import EmailValidationException, SalaryException, UsernameException, \
    WorkDateException


async def email_validation_handler(request: Request, exc: EmailValidationException):
    return JSONResponse(
        status_code=400,
        content={'message': 'This email does not exists!'}
    )


async def salary_handler(request: Request, exc: SalaryException):
    return JSONResponse(
        status_code=400,
        content={'message': 'The first value cannot be greater than the second!'}
    )


async def username_handler(request: Request, exc: UsernameException):
    return JSONResponse(
        status_code=400,
        content={'message': 'Username should start with @ symbol!'}
    )


async def work_date_handler(request: Request, exc: WorkDateException):
    return JSONResponse(
        status_code=400,
        content={'message': 'You entered the wrong date!'}
    )

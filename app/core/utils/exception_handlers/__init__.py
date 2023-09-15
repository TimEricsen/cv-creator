from fastapi import FastAPI

from app.core.utils.excpetions.cv import EmailValidationException, SalaryException, UsernameException, \
    WorkDateException
from app.core.utils.exception_handlers.cv import email_validation_handler, salary_handler, username_handler, \
    work_date_handler


def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(EmailValidationException, email_validation_handler)
    app.add_exception_handler(SalaryException, salary_handler)
    app.add_exception_handler(UsernameException, username_handler)
    app.add_exception_handler(WorkDateException, work_date_handler)

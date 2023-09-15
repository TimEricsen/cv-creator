from app.core.utils.excpetions.base import BaseAppException


class EmailValidationException(BaseAppException):
    pass


class SalaryException(BaseAppException):
    pass


class UsernameException(BaseAppException):
    pass


class WorkDateException(BaseAppException):
    pass

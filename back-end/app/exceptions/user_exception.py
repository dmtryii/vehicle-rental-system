
from app.exceptions.base_exception import InvalidUsage


class PasswordTooShortException(InvalidUsage):
    def __init__(self, message='The password must be longer', status_code=None, payload=None):
        super().__init__(message, status_code, payload)


class InvalidAgeException(InvalidUsage):
    def __init__(self, message='User must be older', status_code=None, payload=None):
        super().__init__(message, status_code, payload)

        
class InvalidEmailException(InvalidUsage):
    def __init__(self, message='Invalid email address', status_code=None, payload=None):
        super().__init__(message, status_code, payload)



class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class EmptyFieldException(InvalidUsage):
    def __init__(self, message='Field cannot be empty', status_code=None, payload=None):
        super().__init__(message, status_code, payload)


class EntityAllreadyPresentException(InvalidUsage):
    def __init__(self, message='The entity is already present', status_code=None, payload=None):
        super().__init__(message, status_code, payload)


class ImpossibleFieldValueError(InvalidUsage):
    def __init__(self, message='The field has acquired an impossible meaning', status_code=None, payload=None):
        super().__init__(message, status_code, payload)


class EntityNotFoundException(InvalidUsage):
    def __init__(self, message='Entity not found', status_code=404, payload=None):
        super().__init__(message, status_code, payload)

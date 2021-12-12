from typing import Tuple


__all__: Tuple[str, ...] = (
    "AlexFlipnoteException",
    "BadRequest",
    "NotFound",
    "InternalServerError",
    "Forbidden",
    "HTTPException",
)


class AlexFlipnoteException(Exception):
    pass


class BadRequest(AlexFlipnoteException):
    pass


class NotFound(AlexFlipnoteException):
    pass


class InternalServerError(AlexFlipnoteException):
    pass


class Forbidden(AlexFlipnoteException):
    pass


class HTTPException(AlexFlipnoteException):
    def __init__(self, response, message):
        self.response = response
        self.status = response.status
        self.message = message

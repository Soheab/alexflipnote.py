from __future__ import annotations
from typing import TYPE_CHECKING, Any, Tuple

if TYPE_CHECKING:
    from aiohttp import ClientResponse


__all__: Tuple[str, ...] = (
    "AlexFlipnoteException",
    "BadRequest",
    "NotFound",
    "InternalServerError",
    "Forbidden",
    "HTTPException",
)


class AlexFlipnoteException(Exception):
    def __init__(self, data: Any, /):
        self.data: Any = data

        self.message = f"{str(data)}"
        if isinstance(data, dict):
            try:
                self.message = data["description"]
            except KeyError:
                pass

            try:
                self.code = data["code"]
            except KeyError:
                self.code = 0

            self.message += f" (Code: {self.code})"
        super().__init__(self.message)


class BadRequest(AlexFlipnoteException):
    pass


class NotFound(AlexFlipnoteException):
    pass


class InternalServerError(AlexFlipnoteException):
    pass


class Forbidden(AlexFlipnoteException):
    pass


class HTTPException(AlexFlipnoteException):
    response: ClientResponse
    data: Any
    message: str
    code: int

    def __init__(self, response: ClientResponse, data: Any, /):
        self.response = response
        self.data = data
        if isinstance(data, dict):
            try:
                self.message = data["description"]
            except KeyError:
                pass
            try:
                self.code = data["code"]
            except KeyError:
                self.code = response.status
        else:
            self.message = str(data)
            self.code = response.status

        super().__init__(self.data)

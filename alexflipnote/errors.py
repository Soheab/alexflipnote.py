# source: https://github.com/BlistBotList/blist-wrapper/blob/bc0c0fe9afbea39993ccfa8b6d633c2b5be634c8/blist/errors.py


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

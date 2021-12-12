from typing import Optional, Tuple, ClassVar, Union, Dict, Any
from aiohttp import ClientSession, ClientResponse

from .errors import *


async def _get_error_message(response: ClientResponse) -> str:
    if response.content_type == "application/json":
        return str((await response.json()).get("description", None))
    return str(await response.text())


class HTTPClient:
    BASE_URL: ClassVar[str] = "https://api.alexflipnote.dev"
    BASE_URL_COFFEE: ClassVar[str] = "https://coffee.alexflipnote.dev"

    __slots__: Tuple[str, ...] = ("__session",)

    def __init__(self, session: Optional[ClientSession] = None) -> None:
        self.__session = session

    # Aiohttp client sessions must be created in async functions
    async def create_session(self) -> None:
        self.__session = ClientSession()

    async def query(self, url: str, method: Optional[str] = "GET", **kwargs) -> ClientResponse:
        if self.__session is None:
            await self.create_session()

        return await self.__session.request(method, url, **kwargs)  # type: ignore

    async def __call__(self, endpoint: str) -> Union[Dict[str, Any], ClientResponse]:
        if endpoint.startswith("coffee"):
            url = f"{self.BASE_URL_COFFEE}/random.json"
        elif endpoint.startswith("support"):
            url = self.BASE_URL
        else:
            url = f"{self.BASE_URL}/{endpoint}"

        response = await self.query(str(url))

        if response.status == 200:
            if response.content_type == "application/json":
                return await response.json()
            return response

        elif response.status == 400:
            raise BadRequest(await _get_error_message(response))
        elif response.status == 403:
            raise Forbidden(await _get_error_message(response))
        elif response.status == 404:
            raise NotFound(await _get_error_message(response))
        elif response.status == 500:
            raise InternalServerError(await _get_error_message(response))
        else:
            raise HTTPException(response, await _get_error_message(response))

    async def close(self) -> None:
        if self.__session is not None and not self.__session.closed:
            await self.__session.close()
            self.__session = None

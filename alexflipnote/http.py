from __future__ import annotations
from typing import Coroutine, Literal, Optional, Tuple, ClassVar, Union, Dict, Any, TYPE_CHECKING, TypeVar, overload

import json
import aiohttp
import urllib.parse

from .errors import *
from .enums import Endpoint, MinecraftIcon, NFTSeason, WithJsonEndpoint, MinecraftEndpoint, WithDocsEndpoint

if TYPE_CHECKING:
    from .client import Client

    from ._types.colour import ColourWithWebsafe as ColourData
    from ._types.http import Image as ImageData, Raw
    from ._types.nft import NFT as NFTData
    from ._types.sillycat import Sillycat as SillycatData

    T = TypeVar("T")
    Response = Coroutine[Any, Any, T]


# source: https://github.com/Rapptz/discord.py/blob/master/discord/http.py
async def json_or_text(response: aiohttp.ClientResponse) -> Union[Dict[str, Any], str]:
    text = await response.text(encoding="utf-8")
    if response.content_type == "application/json":
        return json.loads(text)

    return text


class HTTPClient:
    BASE_URL: ClassVar[str] = "https://api.alexflipnote.dev"
    BASE_URL_COFFEE: ClassVar[str] = "https://coffee.alexflipnote.dev"

    __slots__: Tuple[str, ...] = (
        "_client",
        "_session",
    )

    def __init__(self, client: Client, session: Optional[aiohttp.ClientSession] = None) -> None:
        self._client: Client = client
        self._session: Optional[aiohttp.ClientSession] = session

    async def initiate_session(self) -> None:
        if not self._session:
            self._session = aiohttp.ClientSession()

    @overload
    async def request(self, endpoint: Literal[WithDocsEndpoint.NFT], **parameters: Any) -> NFTData:
        ...

    @overload
    async def request(self, endpoint: Literal[WithDocsEndpoint.SILLYCAT], **parameters: Any) -> SillycatData:
        ...

    @overload
    async def request(
        self,
        endpoint: Union[Endpoint, MinecraftEndpoint] = ...,
        **parameters: Any,
    ) -> str:
        ...

    @overload
    async def request(
        self,
        endpoint: Literal[WithJsonEndpoint.COLOR] = ...,
        **parameters: Any,
    ) -> ColourData:
        ...

    @overload
    async def request(
        self,
        endpoint: WithJsonEndpoint = ...,
        **parameters: Any,
    ) -> ImageData:
        ...

    @overload
    async def request(
        self,
        endpoint: Literal[None] = ...,
        **parameters: Any,
    ) -> Raw:
        ...

    async def request(
        self,
        endpoint: Optional[Union[Endpoint, WithJsonEndpoint, MinecraftEndpoint, WithDocsEndpoint]] = None,
        **parameters: Any,
    ) -> Any:
        url = f"{self.BASE_URL}"
        if endpoint:
            if endpoint is WithJsonEndpoint.COFFEE:
                url = f"{self.BASE_URL_COFFEE}/random.json"
            else:
                url += f"{endpoint}"

        if parameters:
            if endpoint in (WithJsonEndpoint.COLOR, WithDocsEndpoint.NFT, WithDocsEndpoint.SILLYCAT):
                seed = parameters.pop("seed", None)
                quoted_parameters = list(map(urllib.parse.quote, list(parameters.values())))
                first = quoted_parameters.pop(0)
                url += f"/{first}/"
                if quoted_parameters:
                    url += f"{'/'.join(quoted_parameters)}/"
                if seed:
                    url += f"?seed={urllib.parse.quote(seed)}"

            if str(url[-1]) == "/":
                url = url[:-1]

            else:
                encoded_param = urllib.parse.urlencode(parameters, quote_via=urllib.parse.quote)
                url += f"?{str(encoded_param)}"

        await self.initiate_session()
        if not self._session:
            raise RuntimeError("Session is not initialized. This should never happen.")

        async with self._session.get(url) as response:
            data = response
            if response.content_type.startswith("image/"):
                if response.status == 200:
                    return url
            else:
                data = await json_or_text(response)
            if response.status == 200:
                return data

            elif response.status == 400:
                raise BadRequest(data)
            elif response.status == 403:
                raise Forbidden(data)
            elif response.status == 404:
                raise NotFound(data)
            elif response.status == 500:
                raise InternalServerError(data)
            else:
                raise HTTPException(response, data)

    def with_minecraft(self, endpoint: MinecraftEndpoint, text: str, icon: Optional[MinecraftIcon], /) -> Response[str]:
        payload = {"text": text}
        if icon:
            payload["icon"] = icon.value

        return self.request(endpoint, **payload)

    def colour(self, hex: str, /) -> Response[ColourData]:
        return self.request(WithJsonEndpoint.COLOR, hex=hex)

    def with_file(self, endpooint: WithJsonEndpoint, /) -> Response[ImageData]:
        return self.request(endpooint)

    def with_image(self, endpoint: Endpoint, /, **parameters: Any) -> Response[str]:
        return self.request(endpoint, **parameters)

    @overload
    def handle_nft(self, hex: str = ..., season: Optional[NFTSeason] = ..., /) -> Response[str]:
        ...

    @overload
    def handle_nft(
        self,
        hex: str = ...,
        season: Literal[
            NFTSeason.APRIL,
            NFTSeason.AUTUMN,
            NFTSeason.CHRISTMAS,
            NFTSeason.HALLOWEEN,
            NFTSeason.NONE,
            NFTSeason.NORWAY,
            NFTSeason.SPRING,
            NFTSeason.CHRISTMAS,
            NFTSeason.WINTER,
        ] = ...,
        /,
    ) -> Response[str]:
        ...

    @overload
    def handle_nft(
        self, hex: str = ..., season: Optional[NFTSeason] = ..., seed: Optional[Any] = ..., /
    ) -> Response[str]:
        ...

    @overload
    def handle_nft(
        self, hex: Optional[str] = ..., season: Literal[NFTSeason.RANDOM] = ..., seed: Optional[Any] = ..., /
    ) -> Response[NFTData]:
        ...

    @overload
    def handle_nft(
        self, hex: str = ..., season: Literal[NFTSeason.RANDOM] = ..., seed: Optional[Any] = ..., /
    ) -> Response[NFTData]:
        ...

    def handle_nft(
        self, hex: Optional[str] = None, season: Optional[NFTSeason] = None, seed: Optional[Any] = None, /
    ) -> Response[Union[NFTData, str]]:
        payload = {}
        if hex:
            payload["hex"] = hex
        if season and season is not NFTSeason.RANDOM:
            payload["season"] = season.value
        if seed:
            payload["seed"] = seed
        return self.request(WithDocsEndpoint.NFT, **payload)

    @overload
    def handle_sillycat(
        self, hex: Optional[str] = ..., hex2: Optional[str] = ..., seed: Optional[Any] = ..., /
    ) -> Response[SillycatData]:
        ...

    @overload
    def handle_sillycat(self, hex: str = ..., hex2: Optional[str] = ..., seed: Optional[Any] = ..., /) -> Response[str]:
        ...

    @overload
    def handle_sillycat(self, hex: str = ..., hex2: str = ..., seed: Optional[Any] = ..., /) -> Response[str]:
        ...

    def handle_sillycat(
        self, hex: Optional[str] = None, hex2: Optional[str] = None, seed: Optional[Any] = None, /
    ) -> Response[Union[str, SillycatData]]:
        payload = {}
        if hex:
            payload["hex"] = hex
        if hex2:
            payload["hex2"] = hex2
        if seed:
            payload["seed"] = seed
        return self.request(WithDocsEndpoint.SILLYCAT, **payload)

    def support_server(self) -> Response[Raw]:
        return self.request(None)

    async def close(self) -> None:

        if self._session and not self._session.closed:
            await self._session.close()

        self._session = None  # type: ignore

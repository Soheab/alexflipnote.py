from random import randint
from typing import Match, Optional, Tuple, Union, Dict
from re import search

from .errors import BadRequest
from .colour import Colour
from .http import HTTPClient, ClientSession

__all__: Tuple[str, ...] = ("Client",)


def __gen_colour(numbers: Optional[int] = None) -> str:
    random_number = numbers or randint(0, 16777215)
    hex_number = str(hex(random_number))
    return hex_number[2:]


def _check_colour_value(hex_input: Optional[Union[str, int]]) -> str:
    if not hex_input or isinstance(hex_input, int):
        hex_input = __gen_colour(int(hex_input) if hex_input else None)

    _INVALID_HEX_VALUE_ERROR = "Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)"
    match: Optional[Match[str]] = search(r"^#?(?:[0-9a-fA-F]{3}){1,2}$", str(hex_input))
    if not match:
        raise BadRequest(_INVALID_HEX_VALUE_ERROR)

    return match.string.strip("#")


class Client:

    __slots__: Tuple[str, ...] = ("__http",)

    def __init__(self, *, session: ClientSession = None) -> None:
        self.__http: HTTPClient = HTTPClient(session=session)

    # Animals / JSON

    async def birb(self) -> str:
        json_response: Dict[str, str] = await self.__http("birb")  # type: ignore
        return json_response["file"]

    async def cats(self) -> str:
        json_response: Dict[str, str] = await self.__http("cats")  # type: ignore
        return json_response["file"]

    async def sadcat(self) -> str:
        json_response: Dict[str, str] = await self.__http("sadcat")  # type: ignore
        return json_response["file"]

    async def dogs(self) -> str:
        json_response: Dict[str, str] = await self.__http("dogs")  # type: ignore
        return json_response["file"]

    async def coffee(self) -> str:
        json_response: Dict[str, str] = await self.__http("coffee")  # type: ignore
        return json_response["file"]

    # Colour

    async def colour(self, colour: Union[str, int] = None) -> Colour:
        final_colour = await self.__http(f"colour/{_check_colour_value(colour)}")
        return Colour(final_colour)  # type: ignore

    # Alias
    color = colour

    # Other

    async def support_server(self, *, creator: bool = False) -> Union[str, Tuple]:
        data: Dict[Any, Any] = await self.__http("support")  # type: ignore
        discord_server = data["support_server"]
        if creator:
            return discord_server, "https://discord.gg/yCzcfju"

        return discord_server

    # Aliases

    color = colour

    # Session

    async def close(self) -> None:
        await self.__http.close()

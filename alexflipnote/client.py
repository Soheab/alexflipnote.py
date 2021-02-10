from asyncio import AbstractEventLoop, get_event_loop
from random import choice, randint
from re import search
from typing import Any, Tuple, Union
from urllib.parse import quote, urlencode

from aiohttp import ClientSession

from .classes import Colour, Filters, Image, MinecraftIcons
from .errors import BadRequest, Forbidden, HTTPException, InternalServerError, NotFound

_hex_regex = r"^(?:[0-9a-fA-F]{3}){1,2}$"
_hex_regex_failed = "Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)"


def _get_from_enum(enum_class, value: Union[str, int]) -> Any:
    try:
        if isinstance(value, str):
            val = enum_class[str(value.upper())]
        elif isinstance(value, int):
            val = enum_class(int(value))
        else:
            val = value

        return val
    except (KeyError, ValueError):
        return None


class Client:
    __slots__ = ("token", "session", "loop", "_api_url")

    def __init__(self, token: str, *, session: ClientSession = None, loop: AbstractEventLoop = None) -> None:
        self.token = token
        self.session = ClientSession(loop = get_event_loop() or loop) or session
        self._api_url = "https://api.alexflipnote.dev"

    async def _api_request(self, endpoint: str, params: dict = None):

        headers = {"Authorization": str(self.token).strip()}
        url = f"https://api.alexflipnote.dev/{endpoint}"
        if params:
            encoded_param = urlencode(params, quote_via = quote)
            url += f"?{encoded_param}"
        response = await self.session.get(str(url), headers = headers)

        if response.content_type == "application/json" and response.status == 200:
            return await response.json()
        elif response.status == 200:
            return response
        elif response.status == 400:
            raise BadRequest((await response.json()).get("description"))
        elif response.status == 403:
            raise Forbidden((await response.json()).get("description"))
        elif response.status == 404:
            raise NotFound((await response.json()).get("description"))
        elif response.status == 500:
            raise InternalServerError((await response.json()).get("description"))
        else:
            msg = (await response.json()).get("description") or "didn't return json..."
            raise HTTPException(response, msg)

    # Animals

    async def birb(self) -> str:
        json_response = await self._api_request("birb")
        return json_response.get('file')

    async def cats(self) -> str:
        json_response = await self._api_request("cats")
        return json_response.get('file')

    async def sadcat(self) -> str:
        json_response = await self._api_request("sadcat")
        return json_response.get('file')

    async def fml(self) -> str:
        json_response = await self._api_request("fml")
        return json_response.get("text")

    async def dogs(self) -> str:
        json_response = await self._api_request("dogs")
        return json_response.get('file')

    # Colour

    async def colour(self, colour: str = None) -> Colour:
        colour = str(colour).replace("#", "") if colour else None
        if not colour:
            colour = "%06x" % randint(0, 0xFFFFFF)

        if not search(_hex_regex, colour):
            raise BadRequest(_hex_regex_failed)

        color = await self._api_request(f"colour/{colour}")

        return Colour(color)

    async def colour_image(self, colour: str = None) -> Image:
        colour = str(colour).replace("#", "") if colour else None
        if not colour:
            colour = "%06x" % randint(0, 0xFFFFFF)

        if not search(_hex_regex, colour):
            raise BadRequest(_hex_regex_failed)

        response = await self._api_request(f"colour/image/{colour}")
        return Image(str(response.url), response)

    async def colour_image_gradient(self, colour: str = None) -> Image:
        colour = str(colour).replace("#", "") if colour else None
        if not colour:
            colour = "%06x" % randint(0, 0xFFFFFF)

        if not search(_hex_regex, colour):
            raise BadRequest(_hex_regex_failed)

        response = await self._api_request(f"colour/image/gradient/{colour}")
        return Image(str(response.url), response)

    async def colourify(self, image: str, colour: str = None, background: str = None) -> Image:
        colour = str(colour).replace("#", "") if colour else None
        background = str(background).replace("#", "") if background else None
        params = {"image": str(image)}
        if colour:
            if not search(_hex_regex, colour):
                raise BadRequest(_hex_regex_failed)

            params["c"] = colour

        if background:
            if not search(_hex_regex, background):
                raise BadRequest(_hex_regex_failed)

            params["b"] = background

        response = await self._api_request("colourify", params)
        return Image(str(response.url), response)

    async def github_colours(self) -> dict:
        colors = await self._api_request("color/github")
        return dict(colors)

    # Minecraft

    async def achievement(self, text: str, icon: Union[str, int, MinecraftIcons] = MinecraftIcons.RANDOM) -> Image:
        get_icon = _get_from_enum(MinecraftIcons, icon)
        if get_icon is MinecraftIcons.RANDOM or not get_icon:
            icon = choice(list(MinecraftIcons)).value
        else:
            icon = get_icon.value

        response = await self._api_request("achievement", {"text": str(text), "icon": int(icon)})
        return Image(str(response.url), response)

    async def challenge(self, text: str, icon: Union[str, int, MinecraftIcons] = MinecraftIcons.RANDOM) -> Image:
        get_icon = _get_from_enum(MinecraftIcons, icon)
        if get_icon is MinecraftIcons.RANDOM or not get_icon:
            icon = choice(list(MinecraftIcons)).value
        else:
            icon = get_icon.value

        response = await self._api_request("challenge", {"text": str(text), "icon": int(icon)})
        return Image(str(response.url), response)

    # Image

    async def amiajoke(self, image: str) -> Image:
        response = await self._api_request("amiajoke", {"image": str(image)})
        return Image(str(response.url), response)

    async def bad(self, image: str) -> Image:
        response = await self._api_request("bad", {"image": str(image)})
        return Image(str(response.url), response)

    async def calling(self, text: str) -> Image:
        response = await self._api_request("calling", {"text": str(text)})
        return Image(str(response.url), response)

    async def captcha(self, text: str) -> Image:
        response = await self._api_request("captcha", {"text": str(text)})
        return Image(str(response.url), response)

    async def didyoumean(self, top: str, bottom: str) -> Image:
        response = await self._api_request("didyoumean", {"top": str(top), "bottom": str(bottom)})
        return Image(str(response.url), response)

    async def drake(self, top: str, bottom: str, *, ayano: bool = False) -> Image:
        params = {"top": str(top), "bottom": str(bottom)}
        if ayano:
            params["ayano"] = bool(ayano)
        response = await self._api_request("drake", params)
        return Image(str(response.url), response)

    async def facts(self, text: str) -> Image:
        response = await self._api_request("facts", {"text": str(text)})
        return Image(str(response.url), response)

    async def filter(self, name: Union[str, int, Filters], image: str) -> Image:
        if isinstance(name, str):
            if name == "b&w":  # any better way ?
                name = Filters.BLACK_AND_WHITE
        get_filter = _get_from_enum(Filters, name)
        if not get_filter:
            all_filters = [
                fil.name.lower().replace("black_and_white", "b&w")
                for fil in list(Filters)
            ]
            raise NotFound(f"Filter not found. Valid options: {', '.join(all_filters)}")
        if get_filter is Filters.RANDOM:
            name = choice(list(Filters)).name
        else:
            name = get_filter.name

        name = name.replace("BLACK_AND_WHITE", "b&w")

        response = await self._api_request(f"filter/{name.lower()}", {"image": str(image)})
        return Image(str(response.url), response)

    async def floor(self, text: str, image: str = None) -> Image:
        params = {"text": str(text)}
        if image:
            params["image"] = str(image)

        response = await self._api_request("floor", params)
        return Image(str(response.url), response)

    async def jokeoverhead(self, image: str) -> Image:
        response = await self._api_request("jokeoverhead", {"image": str(image)})
        return Image(str(response.url), response)

    async def pornhub(self, text: str, text2: str) -> Image:
        response = await self._api_request("pornhub", {"text": str(text), "text2": str(text2)})
        return Image(str(response.url), response)

    async def salty(self, image: str) -> Image:
        response = await self._api_request("salty", {"image": str(image)})
        return Image(str(response.url), response)

    async def scroll(self, text: str) -> Image:
        response = await self._api_request(f"scroll", {"text": str(text)})
        return Image(str(response.url), response)

    async def ship(self, user: str, user2: str) -> Image:
        response = await self._api_request("ship", {"user": str(user), "user2": str(user2)})
        return Image(str(response.url), response)

    async def supreme(self, text: str, dark: bool = False, light: bool = False) -> Image:
        params = {"text": str(text)}
        if dark:
            params["dark"] = "true"
        if light:
            params["light"] = "true"

        response = await self._api_request("supreme", params)
        return Image(str(response.url), response)

    async def trash(self, face: str, trash: str) -> Image:
        response = await self._api_request("trash", {"face": str(face), "trash": str(trash)})
        return Image(str(response.url), response)

    async def what(self, image: str) -> Image:
        response = await self._api_request("what", {"image": str(image)})
        return Image(str(response.url), response)

    async def shame(self, image: str) -> Image:
        response = await self._api_request("shame", {"image": str(image)})
        return Image(str(response.url), response)

    # Other

    async def support_server(self, creator: bool = False) -> Union[str, Tuple]:
        api = await self.session.get(self._api_url)
        discord_server = (await api.json()).get("support_server")
        if creator:
            return discord_server, "https://discord.gg/yCzcfju"

        return discord_server

    # Aliases

    discord_server = support_server
    color = colour
    colorify = colourify
    github_colors = github_colours
    color_image = colour_image
    color_image_gradient = colour_image_gradient

    # Session

    async def close(self) -> None:
        if not self.session.closed:
            await self.session.close()

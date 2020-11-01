from asyncio import get_event_loop, AbstractEventLoop
from random import choice, randint
from re import search
from typing import Union, Tuple, Any
from urllib.parse import quote

from aiohttp import ClientSession

from .classes import Colour, Image, MinecraftIcons, Filters
from .errors import BadRequest, HTTPException, InternalServerError, NotFound

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
    def __init__(
            self, session: ClientSession = None, loop: AbstractEventLoop = None
    ) -> None:
        self.session = ClientSession(loop = get_event_loop() or loop) or session
        self._api_url = "https://api.alexflipnote.dev"

    async def _check_url(self, url: str):
        url = str(url)
        headers = {"User-Agent": f"AlexFlipnote.py"}
        response = await self.session.get(url = url, headers = headers)
        if (
                response.content_type == "application/json"
                and int((await response.json())["code"]) == 400
        ):
            raise BadRequest((await response.json()).get("description"))
        elif response.status == 200:
            return url
        elif response.status == 400:
            raise BadRequest((await response.json()).get("description"))
        elif response.status == 404:
            raise NotFound((await response.json()).get("description"))
        elif response.status == 500:
            raise InternalServerError((await response.json()).get("description"))
        else:
            raise HTTPException(response, (await response.json()).get("description"))

    # Animals

    async def birb(self) -> str:
        response = await self.session.get(f"{self._api_url}/birb")

        return (await response.json()).get("file")

    async def cats(self) -> str:
        response = await self.session.get(f"{self._api_url}/cats")
        return (await response.json()).get("file")

    async def sadcat(self) -> str:
        response = await self.session.get(f"{self._api_url}/sadcat")
        return (await response.json()).get("file")

    async def fml(self) -> str:
        response = await self.session.get(f"{self._api_url}/fml")
        return (await response.json()).get("text")

    async def dogs(self) -> str:
        response = await self.session.get(f"{self._api_url}/dogs")
        return (await response.json()).get("file")

    # Colour

    async def colour(self, colour: str = None) -> Colour:
        colour = str(colour).replace("#", "") if colour else None
        if not colour:
            colour = "%06x" % randint(0, 0xFFFFFF)

        if not search(_hex_regex, colour):
            raise BadRequest(_hex_regex_failed)

        response = await self.session.get(f"{self._api_url}/colour/{colour}")
        color = await response.json()

        return Colour(color)

    async def colour_image(self, colour: str = None) -> Image:
        colour = str(colour).replace("#", "") if colour else None
        if not colour:
            colour = "%06x" % randint(0, 0xFFFFFF)

        if not search(_hex_regex, colour):
            raise BadRequest(_hex_regex_failed)

        url = f"{self._api_url}/colour/image/{colour}"
        return Image(url, self.session)

    async def colour_image_gradient(self, colour: str = None) -> Image:
        colour = str(colour).replace("#", "") if colour else None
        if not colour:
            colour = "%06x" % randint(0, 0xFFFFFF)

        if not search(_hex_regex, colour):
            raise BadRequest(_hex_regex_failed)

        url = f"{self._api_url}/colour/image/gradient/{colour}"
        return Image(url, self.session)

    async def colourify(
            self, image: str, colour: str = None, background: str = None
    ) -> Image:
        colour = str(colour).replace("#", "") if colour else None
        background = str(background).replace("#", "") if background else None
        url = f"{self._api_url}/colourify?image={str(image)}"
        if colour:
            if not search(r"^(?:[0-9a-fA-F]{3}){1,2}$", colour):
                raise BadRequest(
                    "Invalid HEX value for colour. You're only allowed to enter HEX (0-9 & A-F)"
                )

            url += f"&c={colour}"

        if background:
            if not search(_hex_regex, background):
                raise BadRequest(
                    "Invalid HEX value for background. You're only allowed to enter HEX (0-9 & A-F)"
                )

            url += f"&b={background}"

        return Image(url, self.session)

    async def github_colours(self) -> dict:
        response = await self.session.get(f"{self._api_url}/color/github")
        colors = await response.json()

        return dict(colors)

    # Minecraft

    async def achievement(
            self, text: str, icon: Union[str, int, MinecraftIcons] = MinecraftIcons.RANDOM
    ) -> Image:
        get_icon = _get_from_enum(MinecraftIcons, icon)
        if get_icon is MinecraftIcons.RANDOM or not get_icon:
            icon = choice(list(MinecraftIcons)).value
        else:
            icon = get_icon.value

        url = f"{self._api_url}/achievement?text={quote(str(text))}&icon={icon}"
        return Image(url, self.session)

    async def challenge(
            self, text: str, icon: Union[str, int, MinecraftIcons] = MinecraftIcons.RANDOM
    ) -> Image:
        get_icon = _get_from_enum(MinecraftIcons, icon)
        if get_icon is MinecraftIcons.RANDOM or not get_icon:
            icon = choice(list(MinecraftIcons)).value
        else:
            icon = get_icon.value

        url = f"{self._api_url}/challenge?text={quote(str(text))}&icon={icon}"
        return Image(url, self.session)

    # Image

    async def amiajoke(self, image: str) -> Image:
        url = await self._check_url(f"{self._api_url}/amiajoke?image={str(image)}")
        return Image(url, self.session)

    async def bad(self, image: str) -> Image:
        url = await self._check_url(f"{self._api_url}/bad?image={str(image)}")
        return Image(url, self.session)

    async def calling(self, text: str) -> Image:
        url = f"{self._api_url}/calling?text={quote(str(text))}"
        return Image(url, self.session)

    async def captcha(self, text: str) -> Image:
        url = f"{self._api_url}/captcha?text={quote(str(text))}"
        return Image(url, self.session)

    async def didyoumean(self, top: str, bottom: str) -> Image:
        url = f"{self._api_url}/didyoumean?top={quote(str(top))}&bottom={quote(str(bottom))}"
        return Image(url, self.session)

    async def drake(self, top: str, bottom: str) -> Image:
        url = f"{self._api_url}/drake?top={quote(str(top))}&bottom={quote(str(bottom))}"
        return Image(url, self.session)

    async def facts(self, text: str) -> Image:
        url = f"{self._api_url}/facts?text={quote(str(text))}"
        return Image(url, self.session)

    async def filter(self, name: Union[str, int, Filters], image: str) -> Image:
        if isinstance(name, str):
            if name == "b&w":  # any better way ?
                name = Filters.BLACK_AND_WHITE
        get_filter = _get_from_enum(Filters, name)
        if not get_filter:
            #              want people to use the actual name (b&w) and all lower instead.
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

        url = await self._check_url(
            f"{self._api_url}/filter/{name.lower()}?image={str(image)}"
        )
        return Image(url, self.session)

    async def floor(self, text: str, image: str = None) -> Image:
        url = f"{self._api_url}/floor?text={quote(str(text))}"
        if image:
            url += f"&image={str(image)}"

        return Image(url, self.session)

    async def jokeoverhead(self, image: str) -> Image:
        url = await self._check_url(f"{self._api_url}/jokeoverhead?image={str(image)}")
        return Image(url, self.session)

    async def pornhub(self, text: str, text2: str) -> Image:
        url = (
            f"{self._api_url}/pornhub?text={quote(str(text))}&text2={quote(str(text2))}"
        )
        return Image(url, self.session)

    async def salty(self, image: str) -> Image:
        url = await self._check_url(f"{self._api_url}/salty?image={str(image)}")
        return Image(url, self.session)

    async def scroll(self, text: str) -> Image:
        url = f"{self._api_url}/scroll?text={quote(str(text))}"
        return Image(url, self.session)

    async def ship(self, user: str, user2: str) -> Image:
        url = await self._check_url(
            f"{self._api_url}/ship?user={str(user)}&user2={str(user2)}"
        )
        return Image(url, self.session)

    async def supreme(
            self, text: str, dark: bool = False, light: bool = False
    ) -> Image:
        url = f"{self._api_url}/supreme?text={quote(str(text))}"
        if dark:
            url += "&dark=true"
        if light:
            url += "&light=true"

        url = await self._check_url(url)
        return Image(url, self.session)

    async def trash(self, face: str, trash: str) -> Image:
        url = await self._check_url(f"{self._api_url}/trash?face={str(face)}&trash={str(trash)}")
        return Image(url, self.session)

    async def what(self, image: str) -> Image:
        url = await self._check_url(f"{self._api_url}/what?image={str(image)}")
        return Image(url, self.session)

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

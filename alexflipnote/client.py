from asyncio import get_event_loop
from random import choice, randint
from re import search
from typing import Any, Tuple, Union

from aiohttp import ClientSession

from .classes import Colour, Icon, Image
from .errors import BadRequest, HTTPException, InternalServerError, NotFound


def _replace_characters(text: str) -> str:
    replacements = {
        " ": "%20",
        "!": "%21",
        '"': "%22",
        "#": "%23",
        "$": "%24",
        "%": "%25",
        "&": "%26",
        "'": "%27",
        "(": "%28",
        ")": "%29",
        "*": "%2A",
        "+": "%2B",
        ",": "%2C",
        "-": "%2D",
        ".": "%2E",
        "/": "%2F",
        "=": "%3D",
        "@": "%40",
        ":": "%3A",
        ";": "%3B",
        "^": "%CB%86",
        "_": "%5F",
        "©": "%C2%A9"
    }
    return text.translate(str.maketrans(replacements))


version = "1.6.2"

_hex_regex = r'^(?:[0-9a-fA-F]{3}){1,2}$'
_hex_regex_failed = "Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)"


class Client:

    def __init__(self, session: ClientSession = None) -> None:
        self.session = ClientSession(loop = get_event_loop()) or session
        self._api_url = "https://api.alexflipnote.dev"

    async def _check_url(self, url: str):
        url = str(url)
        headers = {"User-Agent": f"AlexFlipnote.py by Soheab_#6240 | Version: {version}"}
        response = await self.session.get(url = url, headers = headers)
        if response.status == 200:
            return url
        elif response.status == 400:
            raise BadRequest((await response.json()).get("description"))
        elif response.status == 404:
            raise NotFound((await response.json()).get("description"))
        elif response.status == 500:
            raise InternalServerError((await response.json()).get("description"))
        else:
            raise HTTPException(response, (await response.json()).get("description"))

    # can anyone improve this? PRs are more than welcome.

    # remove next version.
    async def steam(self, profile: str) -> str:
        return "This endpoint is removed from the API, sorry."

    # Json/URL

    async def support_server(self, creator: bool = False) -> Tuple[Any, str]:
        api = await self.session.get(self._api_url)
        support_server = (await api.json()).get("support_server")
        if creator:
            return support_server, "https://discord.gg/yCzcfju"

        return support_server

    async def birb(self) -> str:
        response = await self.session.get(f"{self._api_url}/birb")

        return (await response.json()).get('file')

    async def cats(self) -> str:
        response = await self.session.get(f"{self._api_url}/cats")
        return (await response.json()).get('file')

    async def sadcat(self) -> str:
        response = await self.session.get(f"{self._api_url}/sadcat")
        return (await response.json()).get('file')

    async def fml(self) -> str:
        response = await self.session.get(f"{self._api_url}/fml")
        return (await response.json()).get('text')

    async def dogs(self) -> str:
        response = await self.session.get(f"{self._api_url}/dogs")
        return (await response.json()).get('file')

    # Colour

    async def colour(self, colour=None) -> Colour:
        if colour is None:
            colour = "%06x" % randint(0, 0xFFFFFF)

        if not search(_hex_regex, colour):
            raise BadRequest(_hex_regex_failed)

        response = await self.session.get(f"{self._api_url}/colour/{colour}")
        color = await response.json()

        return Colour(color)

    # Dict

    async def github_colours(self) -> dict:
        response = await self.session.get(f"{self._api_url}/color/github")
        colors = await response.json()

        return dict(colors)

    # Image

    async def achievement(self, text: str, icon: Union[int, str, Icon] = None) -> Image:
        text = _replace_characters(str(text))
        actual_icon = ""
        if icon is not None:
            if isinstance(icon, int):
                try:
                    actual_icon = Icon(int(icon)).value
                except ValueError:
                    icon = None
            elif isinstance(icon, str):
                try:
                    actual_icon = Icon[str(icon)].value
                except KeyError:
                    icon = None
            elif isinstance(icon, Icon):
                actual_icon = icon.value
            else:
                actual_icon = ""

        if icon is not None and actual_icon != "":
            actual_icon = f"&icon={actual_icon}"

        url = f"{self._api_url}/achievement?text={text}{actual_icon}"

        return Image(url, self.session)

    async def amiajoke(self, image: str) -> Image:
        url = await self._check_url(
            f"{self._api_url}/amiajoke?image={image}"
        )

        return Image(url, self.session)

    async def bad(self, image: str) -> Image:
        url = await self._check_url(
            f"{self._api_url}/bad?image={image}"
        )

        return Image(url, self.session)

    async def calling(self, text: str) -> Image:
        text = _replace_characters(text)
        url = f"{self._api_url}/calling?text={text}"

        return Image(url, self.session)

    async def captcha(self, text: str) -> Image:
        text = _replace_characters(text)
        url = f"{self._api_url}/captcha?text={text}"

        return Image(url, self.session)

    async def challenge(self, text: str, icon: Union[int, str, Icon] = None) -> Image:
        text = _replace_characters(text)
        actual_icon = ""
        if icon is not None:
            if isinstance(icon, int):
                try:
                    actual_icon = Icon(int(icon)).value
                except ValueError:
                    icon = None
            elif isinstance(icon, str):
                try:
                    actual_icon = Icon[str(icon)].value
                except KeyError:
                    icon = None
            elif isinstance(icon, Icon):
                actual_icon = icon.value
            else:
                actual_icon = ""

        if icon is not None and actual_icon != "":
            actual_icon = f"&icon={actual_icon}"

        url = f"{self._api_url}/challenge?text={text}{actual_icon}"

        return Image(url, self.session)

    async def colour_image(self, colour=None) -> Image:
        if colour is None:
            colour = "%06x" % randint(0, 0xFFFFFF)

        if not search(_hex_regex, colour):
            raise BadRequest(_hex_regex_failed)

        url = f"{self._api_url}/colour/image/{colour}"

        return Image(url, self.session)

    async def colour_image_gradient(self, colour=None) -> Image:
        if colour is None:
            colour = "%06x" % randint(0, 0xFFFFFF)

        if not search(_hex_regex, colour):
            raise BadRequest(_hex_regex_failed)

        url = f"{self._api_url}/colour/image/gradient/{colour}"

        return Image(url, self.session)

    async def colourify(self, image: str, colour=None, background=None) -> Image:
        url = f"{self._api_url}/colourify?image={image}"
        if colour is not None:
            if not search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
                raise BadRequest("Invalid HEX value for colour. You're only allowed to enter HEX (0-9 & A-F)")

            url += f"&c={colour}"

        if background is not None:
            if not search(_hex_regex, background):
                raise BadRequest("Invalid HEX value for background. You're only allowed to enter HEX (0-9 & A-F)")

            url += f"&b={background}"

        return Image(url, self.session)

    async def didyoumean(self, top: str, bottom: str) -> Image:
        top = _replace_characters(top)
        bottom = _replace_characters(bottom)
        url = f"{self._api_url}/didyoumean?top={top}&bottom={bottom}"

        return Image(url, self.session)

    async def drake(self, top: str, bottom: str) -> Image:
        top = _replace_characters(top)
        bottom = _replace_characters(bottom)
        url = f"{self._api_url}/drake?top={top}&bottom={bottom}"

        return Image(url, self.session)

    async def facts(self, text: str) -> Image:
        text = _replace_characters(text)
        url = f"{self._api_url}/facts?text={text}"

        return Image(url, self.session)

    async def filter(self, name: str, image: str) -> Image:
        options = ['blur', 'invert', 'b&w', 'deepfry', 'sepia', 'pixelate',
                   'magik', 'jpegify', 'wide', 'snow', 'gay', 'communist',
                   'random']

        if name.lower() not in options:
            raise NotFound("Filter not found. Valid options: " + ", ".join(options))
        if name.lower() == "random":
            name = choice(options)

        url = await self._check_url(f"{self._api_url}/filter/{name.lower()}?image={image}")
        return Image(url, self.session)

    async def floor(self, text: str, image: str = None) -> Image:
        text = _replace_characters(text)
        url = f"{self._api_url}/floor?text={text}"
        if image is not None:
            url += f"&image={image}"

        return Image(url, self.session)

    async def jokeoverhead(self, image: str) -> Image:
        url = await self._check_url(
            f"{self._api_url}/jokeoverhead?image={image}"
        )

        return Image(url, self.session)

    async def pornhub(self, text: str, text2: str) -> Image:
        text = _replace_characters(text)
        text2 = _replace_characters(text2)
        url = f"{self._api_url}/pornhub?text={text}&text2={text2}"

        return Image(url, self.session)

    async def salty(self, image: str) -> Image:
        url = await self._check_url(
            f"{self._api_url}/salty?image={image}"
        )

        return Image(url, self.session)

    async def scroll(self, text: str) -> Image:
        text = _replace_characters(text)
        url = f"{self._api_url}/scroll?text={text}"

        return Image(url, self.session)

    async def ship(self, user: str, user2: str) -> Image:
        url = await self._check_url(
            f"{self._api_url}/ship?user={user}&user2={user2}"
        )

        return Image(url, self.session)

    async def supreme(self, text: str, dark: bool = False, light: bool = False) -> Image:
        text = _replace_characters(text)
        darkorlight = ""
        if dark:
            darkorlight = "&dark=true"
        if light:
            darkorlight = "&light=true"
        if dark and light:
            raise BadRequest("You can only choose either light or dark, not both.")

        url = f"{self._api_url}/supreme?text={text}{darkorlight}"

        return Image(url, self.session)

    async def trash(self, face: str, trash: str) -> Image:
        url = await self._check_url(
            f"{self._api_url}/trash?face={face}&trash={trash}"
        )

        return Image(url, self.session)

    # aliases

    color = colour
    github_colors = github_colours
    color_image = colour_image

    async def close(self) -> None:
        if not self.session.closed:
            await self.session.close()

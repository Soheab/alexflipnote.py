from asyncio import get_event_loop
from random import choice, randint
from re import search
from typing import Any, Tuple, Union

from aiohttp import ClientSession

from .classes import Colour, Icon, Image, Steam


class BadRequest(Exception):
    pass


class NotFound(Exception):
    pass


class InternalServerError(Exception):
    pass


def _parse_text(text: str) -> str:
    replacements = {
        " ": "%20",
        "!": "%21",
        "#": "%23",
        "$": "%24",
        "%": "%25",
        "&": "%26",
        "*": "%2A",
        "=": "%3D",
        "@": "%40",
        ":": "%3A",
        ";": "%3B",
        "^": "%CB%86",
        "_": "%5F",
        "©": "%C2%A9"
        }
    return text.translate(str.maketrans(replacements))


class Client:

    def __init__(self) -> None:
        self._session = ClientSession(loop = get_event_loop())
        self._api_url = "https://api.alexflipnote.dev"

    # will be rewritten when json errors are a thing.
    async def _check_url(self, url: str):  # return_response=False):
        response = await self._session.get(url)
        # print(response.status, await response.text())
        # error.group().strip("</p>")
        if response.status in [400, 404, 500]:
            # text = await response.text()
            # error = search('<p>(.+?)</p>', str(text))
            if response.status == 400:
                raise BadRequest()
            if response.status == 404:
                raise NotFound()
            if response.status == 500:
                raise InternalServerError()
        return url
        # else:
        # raise HTTPException(response, await response.json().get("msg"))

    # else:
    # if return_response:
    # return response
    # return url
    # can anyone improve this? PRs are more than welcome.

    # Json/URL

    async def support_server(self, creator: bool = False) -> Tuple[Any, str]:
        api = await self._session.get(self._api_url)
        support_server = (await api.json()).get("support_server")
        if creator:
            return support_server, "https://discord.gg/yCzcfju"

        return support_server

    async def birb(self) -> str:
        response = await self._session.get(f"{self._api_url}/birb")

        return (await response.json()).get('file')

    async def cats(self) -> str:
        response = await self._session.get(f"{self._api_url}/cats")
        return (await response.json()).get('file')

    async def sadcat(self) -> str:
        response = await self._session.get(f"{self._api_url}/sadcat")
        return (await response.json()).get('file')

    async def fml(self) -> str:
        response = await self._session.get(f"{self._api_url}/fml")
        return (await response.json()).get('text')

    async def dogs(self) -> str:
        response = await self._session.get(f"{self._api_url}/dogs")
        return (await response.json()).get('file')

    # Colour

    async def colour(self, colour = None) -> Colour:
        if colour is None:
            colour = "%06x" % randint(0, 0xFFFFFF)

        if not search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        response = await self._session.get(f"{self._api_url}/colour/{colour}")
        color = await response.json()

        return Colour(color)

    # Steam

    async def steam(self, profile: str) -> Steam:
        response = await self._session.get(f"{self._api_url}/steam/user/{profile}")
        if response.status == 404:  # maybe remove and let _check_url handle it.
            raise NotFound("User not found on steam.")

        profile = await response.json()

        return Steam(profile)

    # Dict

    async def github_colours(self) -> dict:
        response = await self._session.get(f"{self._api_url}/color/github")
        colors = await response.json()

        return dict(colors)

    # Image

    async def achievement(self, text: str, icon: Union[int, str, Icon] = None) -> Image:
        text = _parse_text(str(text))
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

        return Image(url, self._session)

    async def amiajoke(self, image: str) -> Image:
        url = await self._check_url(
            f"{self._api_url}/amiajoke?image={image}"
            )

        return Image(url, self._session)

    async def bad(self, image: str) -> Image:
        url = await self._check_url(
            f"{self._api_url}/bad?image={image}"
            )

        return Image(url, self._session)

    async def calling(self, text: str) -> Image:
        text = _parse_text(text)
        url = f"{self._api_url}/calling?text={text}"

        return Image(url, self._session)

    async def captcha(self, text: str) -> Image:
        text = _parse_text(text)
        url = f"{self._api_url}/captcha?text={text}"

        return Image(url, self._session)

    async def challenge(self, text: str, icon: Union[int, str, Icon] = None) -> Image:
        text = _parse_text(text)
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

        return Image(url, self._session)

    async def colour_image(self, colour = None) -> Image:
        if colour is None:
            colour = "%06x" % randint(0, 0xFFFFFF)

        if not search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        url = f"{self._api_url}/colour/image/{colour}"

        return Image(url, self._session)

    async def colour_image_gradient(self, colour = None) -> Image:
        if colour is None:
            colour = "%06x" % randint(0, 0xFFFFFF)

        if not search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        url = f"{self._api_url}/colour/image/gradient/{colour}"

        return Image(url, self._session)

    async def colourify(self, image: str, colour = "", background = "") -> Image:
        if colour != "":
            if not search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
                raise BadRequest("Invalid HEX value for colour. You're only allowed to enter HEX (0-9 & A-F)")

            colour = f"&c={colour}"

        if background != "":
            if not search(r'^(?:[0-9a-fA-F]{3}){1,2}$', background):
                raise BadRequest("Invalid HEX value for background. You're only allowed to enter HEX (0-9 & A-F)")

            background = f"&b={background}"

        url = f"{self._api_url}/colourify?image={image}{colour}{background}"

        return Image(url, self._session)

    async def didyoumean(self, top: str, bottom: str) -> Image:
        top = _parse_text(top)
        bottom = _parse_text(bottom)
        url = f"{self._api_url}/didyoumean?top={top}&bottom={bottom}"

        return Image(url, self._session)

    async def drake(self, top: str, bottom: str) -> Image:
        top = _parse_text(top)
        bottom = _parse_text(bottom)
        url = f"{self._api_url}/drake?top={top}&bottom={bottom}"

        return Image(url, self._session)

    async def facts(self, text: str) -> Image:
        text = _parse_text(text)
        url = f"{self._api_url}/facts?text={text}"

        return Image(url, self._session)

    async def filter(self, name: str, image: str) -> Image:
        options = ['blur', 'invert', 'b&w', 'deepfry', 'sepia', 'pixelate',
                   'magik', 'jpegify', 'wide', 'snow', 'gay', 'communist',
                   'random']

        if name.lower() not in options:
            raise NotFound("Filter not found. Valid options: " + ", ".join(options))
        if name.lower() == "random":
            name = choice(options)

        url = await self._check_url(f"{self._api_url}/filter/{name}?image={image}")
        return Image(url, self._session)

    async def floor(self, text: str, image: str = None) -> Image:
        text = _parse_text(text)
        if image is not None:
            image = f"&image={image}"

        url = f"{self._api_url}/floor?text={text}{image}"

        return Image(url, self._session)

    async def jokeoverhead(self, image: str) -> Image:
        url = await self._check_url(
            f"{self._api_url}/jokeoverhead?image={image}"
            )

        return Image(url, self._session)

    async def pornhub(self, text: str, text2: str) -> Image:
        text = _parse_text(text)
        text2 = _parse_text(text2)
        url = f"{self._api_url}/pornhub?text={text}&text2={text2}"

        return Image(url, self._session)

    async def salty(self, image: str) -> Image:
        url = await self._check_url(
            f"{self._api_url}/salty?image={image}"
            )

        return Image(url, self._session)

    async def scroll(self, text: str) -> Image:
        text = _parse_text(text)
        url = f"{self._api_url}/scroll?text={text}"

        return Image(url, self._session)

    async def ship(self, user: str, user2: str) -> Image:
        url = await self._check_url(
            f"{self._api_url}/ship?user={user}&user2={user2}"
            )

        return Image(url, self._session)

    async def supreme(self, text: str, dark: bool = False, light: bool = False) -> Image:
        text = _parse_text(text)
        darkorlight = ""
        if dark:
            darkorlight = "&dark=true"
        if light:
            darkorlight = "&light=true"
        if dark and light:
            raise BadRequest("You can only choose either light or dark, not both.")

        url = f"{self._api_url}/supreme?text={text}{darkorlight}"

        return Image(url, self._session)

    async def trash(self, face: str, trash: str) -> Image:
        url = await self._check_url(
            f"{self._api_url}/trash?face={face}&trash={trash}"
            )

        return Image(url, self._session)

    # aliases

    color = colour
    github_colors = github_colours
    color_image = colour_image

    async def close(self) -> None:
        if not self._session.closed:
            await self._session.close()

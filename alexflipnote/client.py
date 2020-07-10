from random import randint as rand
from re import search
from typing import Union

from aiohttp import ContentTypeError
from url_regex import UrlRegex

from alexflipnote import http
from .classes import Colour, Steam, Image, Icon


# Exceptions

class BadRequest(Exception):
    pass


class NotFound(Exception):
    pass


def _parse_text(text: str) -> str:
    replacements = {
        " ": "%20",
        "!": "%21",
        "#": "%23",
        "$": "%24",
        "%": "%25",
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
    _BASE_URL = "https://api.alexflipnote.dev/"

    def __init__(self) -> None:
        self._http_client = http

    def _api_url(self, path: str) -> str:
        return self._BASE_URL + path

    def _check_url(self, image_url: str, path: str = None, only_image=False):
        get_url = UrlRegex(str(image_url))
        valid_domains = ["cdn.discordapp.com", "media.discordapp.net"]
        if get_url.links[0].domain not in valid_domains:
            raise BadRequest("Only Discord CDN URLs are allowed...")
        if path is None and only_image is True:
            return image_url
        return self._api_url(path + image_url)

    # Json/URL

    async def birb(self) -> str:
        url = await self._http_client.get(self._api_url("birb"), res_method = "json")

        return url.get('file')

    async def cats(self) -> str:
        url = await self._http_client.get(self._api_url("cats"), res_method = "json")

        return url.get('file')

    async def sadcat(self) -> str:
        url = await self._http_client.get(self._api_url("sadcat"), res_method = "json")

        return url.get('file')

    async def fml(self) -> str:
        url = await self._http_client.get(self._api_url("fml"), res_method = "json")

        return url.get("text")

    async def dogs(self) -> str:
        url = await self._http_client.get(self._api_url("dogs"), res_method = "json")

        return url.get('file')

    # Colour

    async def colour(self, colour=None) -> Colour:
        if colour is None:
            colour = "%06x" % rand(0, 0xFFFFFF)

        if not search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        response = await self._http_client.get(
            str(self._api_url(f"colour/{colour}")),
            res_method = "json"
        )
        return Colour(response)

    # Steam

    async def steam(self, profile: str) -> Steam:
        try:
            response = await self._http_client.get(self._api_url(f"steam/user/{profile}"), res_method = "json")
        except ContentTypeError:
            raise NotFound("User not found on steam.")

        return Steam(response)

    # Dict

    async def github_colours(self) -> dict:
        response = await self._http_client.get(str(self._api_url("color/github")), res_method = "json")

        return dict(response)

    # Image

    async def achievement(self, text: str, icon: Union[int, str, Icon] = None) -> Image:
        text = _parse_text(text)
        actual_icon = ""
        if icon is not None:
            if isinstance(icon, int):
                actual_icon = Icon(int(icon)).value
            elif isinstance(icon, str):
                actual_icon = Icon[str(icon)].value
            elif isinstance(icon, Icon):
                actual_icon = Icon.value
            else:
                raise BadRequest("Invalid icon. Icon can only be int, str or instance of Icon")

        if icon is not None and actual_icon != "":
            actual_icon = f"&icon={actual_icon}"

        url = self._api_url(f"achievement?text={text}{actual_icon}")

        return Image(url, self._http_client)

    async def amiajoke(self, image: str) -> Image:
        url = self._check_url(image, "amiajoke?image=")

        return Image(url, self._http_client)

    async def bad(self, image: str) -> Image:
        url = self._check_url(image, "bad?image=")

        return Image(url, self._http_client)

    async def calling(self, text: str) -> Image:
        text = _parse_text(text)
        url = self._api_url(f"calling?text={text}")

        return Image(url, self._http_client)

    async def captcha(self, text: str) -> Image:
        text = _parse_text(text)
        url = self._api_url(f"captcha?text={text}")

        return Image(url, self._http_client)

    async def challenge(self, text: str, icon: Union[int, str, Icon] = None) -> Image:
        text = _parse_text(text)
        actual_icon = ""
        if icon is not None:
            if isinstance(icon, int):
                actual_icon = Icon(int(icon)).value
            elif isinstance(icon, str):
                actual_icon = Icon[str(icon)].value
            elif isinstance(icon, Icon):
                actual_icon = Icon.value
            else:
                raise BadRequest("Invalid icon. Icon can only be int, str or instance of Icon")

        if icon is not None and actual_icon != "":
            actual_icon = f"&icon={actual_icon}"

        url = self._api_url(f"challenge?text={text}{actual_icon}")

        return Image(url, self._http_client)

    async def colour_image(self, colour=None) -> Image:
        if colour is None:
            colour = "%06x" % rand(0, 0xFFFFFF)

        if not search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        url = self._api_url(f"colour/image/{colour}")

        return Image(url, self._http_client)

    async def colour_image_gradient(self, colour=None) -> Image:
        if colour is None:
            colour = "%06x" % rand(0, 0xFFFFFF)

        if not search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        url = self._api_url(f"colour/image/gradient/{colour}")

        return Image(url, self._http_client)

    async def colourify(self, image: str, colour="", background="") -> Image:
        if colour != "":
            if not search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
                raise BadRequest("Invalid HEX value for colour. You're only allowed to enter HEX (0-9 & A-F)")

            colour = f"&c={colour}"

        if background != "":
            if not search(r'^(?:[0-9a-fA-F]{3}){1,2}$', background):
                raise BadRequest("Invalid HEX value for background. You're only allowed to enter HEX (0-9 & A-F)")

            background = f"&b={background}"

        url = self._api_url(f"colourify?image={image}{colour}{background}")

        return Image(url, self._http_client)

    async def didyoumean(self, top: str, bottom: str) -> Image:
        top = top.replace(" ", "%20").replace("#", "%23")
        bottom = bottom.replace(" ", "%20").replace("#", "%23")

        url = self._api_url(f"didyoumean?top={top}&bottom={bottom}")

        return Image(url, self._http_client)

    async def drake(self, top: str, bottom: str) -> Image:
        top = top.replace(" ", "%20").replace("#", "%23")
        bottom = bottom.replace(" ", "%20").replace("#", "%23")
        url = self._api_url(f"drake?top={top}&bottom={bottom}")

        return Image(url, self._http_client)

    async def facts(self, text: str) -> Image:
        text = _parse_text(text)
        url = self._api_url(f"facts?text={text}")

        return Image(url, self._http_client)

    async def filter(self, name: str, image: str) -> Image:
        options = ['blur', 'invert', 'b&w', 'deepfry', 'snow', 'gay',
                   'pixelate', 'jpegify', 'magik', 'communist']
        if name not in options:
            raise NotFound("Filter not found. Valid options: " + ", ".join(options))

        url = self._check_url(image, f"filter/{name}?image=")

        return Image(url, self._http_client)

    async def floor(self, text: str, image: str = None) -> Image:
        text = _parse_text(text)
        if image is not None:
            image = f"&image={image}"

        url = self._api_url(f"floor?text={text}{image}")

        return Image(url, self._http_client)

    async def jokeoverhead(self, image: str) -> Image:
        url = self._check_url(image, "jokeoverhead?image=")

        return Image(url, self._http_client)

    async def pornhub(self, text: str, text2: str) -> Image:
        text = _parse_text(text)
        text2 = _parse_text(text2)
        url = self._api_url(f"pornhub?text={text}&text2={text2}")

        return Image(url, self._http_client)

    async def salty(self, image: str) -> Image:
        url = self._check_url(image, "salty?image=")

        return Image(url, self._http_client)

    async def scroll(self, text: str) -> Image:
        text = _parse_text(text)
        url = self._api_url(f"scroll?text={text}")

        return Image(url, self._http_client)

    async def ship(self, user: str, user2: str) -> Image:
        user_url = self._check_url(user, only_image = True)
        user2_url = self._check_url(user2, only_image = True)
        url = self._api_url(f"ship?user={user_url}&user2={user2_url}")

        return Image(url, self._http_client)

    async def supreme(self, text: str, dark: bool = False, light: bool = False) -> Image:
        text = _parse_text(text)
        darkorlight = ""
        if dark:
            darkorlight = "&dark=true"
        if light:
            darkorlight = "&light=true"
        if dark and light:
            raise BadRequest("You can only choose either light or dark, not both.")

        url = self._api_url(f"supreme?text={text}{darkorlight}")

        return Image(url, self._http_client)

    async def trash(self, face: str, trash: str) -> Image:
        face_url = self._check_url(face, only_image = True)
        trash_url = self._check_url(trash, only_image = True)

        url = self._api_url(f"trash?face={face_url}&trash={trash_url}")

        return Image(url, self._http_client)

    # aliases

    color = colour
    github_colors = github_colours
    color_image = colour_image

    async def close(self) -> None:
        if not self._http_client.session.closed:
            await self._http_client.close()
        return

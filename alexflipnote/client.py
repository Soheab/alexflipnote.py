import random
import re
from typing import Dict, Union

import url_regex
from aiohttp import ContentTypeError

from alexflipnote import http
from .classes import Colour, Steam, Image, Icon


class BadRequest(Exception):
    pass


class NotFound(Exception):
    pass


class Client:
    _BASE_URL = "https://api.alexflipnote.dev/"

    def __init__(self) -> None:
        self._http_client = http

    def _api_url(self, path: str) -> str:
        return self._BASE_URL + path

    def _check_url(self, path: str, url: str):
        get_url = url_regex.UrlRegex(str(url))
        valid_domains = ["cdn.discordapp.com", "media.discordapp.net"]
        if get_url.links[0].domain not in valid_domains:
            raise BadRequest("Only Discord CDN URLs are allowed...")
        return self._api_url(path + url)

    async def achievement(self, text: str, icon: Union[int, str, Icon] = None) -> Image:
        text = text.replace(" ", "%20").replace("#", "%23")
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
        url = self._check_url("amiajoke?image=", image)

        return Image(url, self._http_client)

    async def bad(self, image: str) -> Image:
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self._api_url(f"bad?image={image}")

        return Image(url, self._http_client)

    async def birb(self) -> str:
        url: Dict = await self._http_client.get(self._api_url("birb"), res_method = "json")

        return url['file']

    async def calling(self, text: str) -> Image:
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self._api_url(f"calling?text={text}")

        return Image(url, self._http_client)

    async def captcha(self, text: str) -> Image:
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self._api_url(f"captcha?text={text}")

        return Image(url, self._http_client)

    async def cats(self) -> str:
        url: Dict = await self._http_client.get(self._api_url("cats"), res_method = "json")

        return url['file']

    async def challenge(self, text: str, icon: Union[int, str, Icon] = None) -> Image:
        text = text.replace(" ", "%20").replace("#", "%23")
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

    async def colour(self, colour=None) -> Colour:
        if colour is None:
            colour = "%06x" % random.randint(0, 0xFFFFFF)

        if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        response = await self._http_client.get(
            str(self._api_url(f"colour/{colour}")),
            res_method = "json"
        )
        return Colour(response)

    color = colour  # aliases to colour

    async def github_colours(self) -> dict:
        response = await self._http_client.get(str(self._api_url("color/github")), res_method = "json")

        return dict(response)

    github_colors = github_colours  # aliases to github_colours

    async def colour_image(self, colour=None) -> Image:
        if colour is None:
            colour = "%06x" % random.randint(0, 0xFFFFFF)

        if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        url = self._api_url(f"colour/image/{colour}")

        return Image(url, self._http_client)

    color_image = colour_image  # aliases to colour_image

    async def colour_image_gradient(self, colour=None) -> Image:
        if colour is None:
            colour = "%06x" % random.randint(0, 0xFFFFFF)

        if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        url = self._api_url(f"colour/image/gradient/{colour}")

        return Image(url, self._http_client)

    async def colourify(self, image: str, colour="", background="") -> Image:
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")

        if colour != "":
            if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
                raise BadRequest("Invalid HEX value for colour. You're only allowed to enter HEX (0-9 & A-F)")

            colour = f"&c={colour}"

        if background != "":
            if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', background):
                raise BadRequest("Invalid HEX value for background. You're only allowed to enter HEX (0-9 & A-F)")

            background = f"&b={background}"

        url = self._api_url(f"colourify?image={image}{colour}{background}")

        return Image(url, self._http_client)

    async def didyoumean(self, top: str, bottom: str) -> Image:
        top = top.replace(" ", "%20").replace("#", "%23")
        bottom = bottom.replace(" ", "%20").replace("#", "%23")

        url = self._api_url(f"didyoumean?top={top}&bottom={bottom}")

        return Image(url, self._http_client)

    async def dogs(self) -> str:
        url: Dict = await self._http_client.get(self._api_url("dogs"), res_method = "json")

        return url['file']

    async def drake(self, top: str, bottom: str) -> Image:
        top = top.replace(" ", "%20").replace("#", "%23")
        bottom = bottom.replace(" ", "%20").replace("#", "%23")
        url = self._api_url(f"drake?top={top}&bottom={bottom}")

        return Image(url, self._http_client)

    async def facts(self, text: str) -> Image:
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self._api_url(f"facts?text={text}")

        return Image(url, self._http_client)

    async def filter(self, name: str, image: str) -> Image:
        options = ['blur', 'invert', 'b&w', 'deepfry', 'snow', 'gay',
                   'pixelate', 'jpegify', 'magik', 'communist']
        if name not in options:
            raise NotFound("Filter not found. Valid options: " + ", ".join(options))

        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self._api_url(f"filter/{name}?image={image}")

        return Image(url, self._http_client)

    async def floor(self, text: str, image: str = None) -> Image:
        text = text.replace(" ", "%20").replace("#", "%23")
        if image is not None:
            get_url = url_regex.UrlRegex(str(image))
            if not get_url.detect:
                raise BadRequest("String passed is not a valid URL.")
            image = f"&image={image}"
        url = self._api_url(f"floor?text={text}{image}")

        return Image(url, self._http_client)

    async def fml(self) -> str:
        url: Dict = await self._http_client.get(self._api_url("fml"), res_method = "json")

        return url["text"]

    async def jokeoverhead(self, image: str) -> Image:
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")
        url = self._api_url(f"jokeoverhead?image={image}")

        return Image(url, self._http_client)

    async def pornhub(self, text: str, text2: str) -> Image:
        text = text.replace(" ", "%20").replace("#", "%23")
        text2 = text2.replace(" ", "%20").replace("#", "%23")
        url = self._api_url(f"pornhub?text={text}&text2={text2}")

        return Image(url, self._http_client)

    async def sadcat(self) -> str:
        url: Dict = await self._http_client.get(self._api_url("sadcat"), res_method = "json")

        return url['file']

    async def salty(self, image: str) -> Image:
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")
        url = self._api_url(f"salty?image={image}")

        return Image(url, self._http_client)

    async def scroll(self, text: str) -> Image:
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self._api_url(f"scroll?text={text}")

        return Image(url, self._http_client)
    # create a subclass and override the handler methods

    async def ship(self, user: str, user2: str) -> Image:
        user_url = url_regex.UrlRegex(str(user))
        if not user_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if user_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        user2_url = url_regex.UrlRegex(str(user2))
        if not user2_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if user2_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self._api_url(f"ship?user={user}&user2={user2}")

        return Image(url, self._http_client)

    async def steam(self, profile: str) -> Steam:
        try:
            response = await self._http_client.get(self._api_url(f"steam/user/{profile}"), res_method = "json")
        except ContentTypeError:
            raise NotFound("User not found on steam.")

        return Steam(response)

    async def supreme(self, text: str, dark: bool = False, light: bool = False) -> Image:
        text = text.replace(" ", "%20").replace("#", "%23")
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
        face_url = url_regex.UrlRegex(str(face))
        if not face_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if face_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        trash_url = url_regex.UrlRegex(str(trash))
        if not trash_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if trash_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self._api_url(f"trash?face={face}&trash={trash}")

        return Image(url, self._http_client)

    async def close(self) -> None:
        if not self._http_client.session.closed:
            await self._http_client.close()
        return

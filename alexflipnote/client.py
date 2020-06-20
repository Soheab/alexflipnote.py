import io
import random
import re

import aiohttp
import url_regex

from . import http
from .classes import Colour, Steam, Image, Icon
from typing import Union


class BadRequest(Exception):
    pass


class NotFound(Exception):
    pass


class Client:
    _BASE_URL = "https://api.alexflipnote.dev/"

    def __init__(self):
        self._http_client = http

    def _api_url(self, path):
        return self._BASE_URL + path

    async def achievement(self, text, icon: Union[int, str, Icon] = None):
        text = text.replace(" ", "%20").replace("#", "%23")
        actual_icon = ""
        if icon is not None:
            if isinstance(icon, int):
                actual_icon = Icon(icon).value

            elif isinstance(icon, str):
                actual_icon = Icon[icon].value

            elif isinstance(icon, Icon):
                actual_icon = Icon.value

        if icon is not None:
            actual_icon = f"&icon={actual_icon}"

        url = self._api_url(f"achievement?text={text}{actual_icon}")

        return Image(url, self._http_client)

    async def amiajoke(self, image: str):
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self._api_url(f"amiajoke?image={image}")

        return Image(url, self._http_client)

    async def bad(self, image: str):
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self._api_url(f"bad?image={image}")

        return Image(url, self._http_client)

    async def birb(self):
        url = await self._http_client.get(self._api_url("birb"), res_method = "json")

        return url['file']

    async def calling(self, text):
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self._api_url(f"calling?text={text}")

        return Image(url, self._http_client)

    async def captcha(self, text):
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self._api_url(f"captcha?text={text}")

        return Image(url, self._http_client)

    async def cats(self):
        url = await self._http_client.get(self._api_url("cats"), res_method = "json")

        return url['file']

    async def challenge(self, text, icon: Union[int, str, Icon] = None):
        text = text.replace(" ", "%20").replace("#", "%23")
        actual_icon = ""
        if icon is not None:
            if isinstance(icon, int):
                actual_icon = Icon(icon).value

            elif isinstance(icon, str):
                actual_icon = Icon[icon].value

            elif isinstance(icon, Icon):
                actual_icon = Icon.value

        if icon is not None:
            actual_icon = f"&icon={actual_icon}"

        url = self._api_url(f"challenge?text={text}{actual_icon}")

        return Image(url, self._http_client)

    async def colour(self, colour=None):
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

    async def github_colours(self):
        response = await self._http_client.get(str(self._api_url("color/github")), res_method = "json")

        return response

    github_color = github_colours  # aliases to github_colour

    async def colour_image(self, colour=None):
        if colour is None:
            colour = "%06x" % random.randint(0, 0xFFFFFF)

        if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        url = self._api_url(f"colour/image/{colour}")

        return Image(url, self._http_client)

    color_image = colour_image  # aliases to colour_image

    async def colour_image_gradient(self, colour=None):
        if colour is None:
            colour = "%06x" % random.randint(0, 0xFFFFFF)

        if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        url = self._api_url(f"colour/image/gradient/{colour}")

        return Image(url, self._http_client)

    async def colourify(self, image, colour="", background=""):
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")

        if colour is not None:
            if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
                raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

            colour = f"&c={colour}"

        if background is not None:
            if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', background):
                raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

            background = f"&b={background}"

        url = self._api_url(f"colourify?image={image}{colour}{background}")

        return Image(url, self._http_client)

    async def didyoumean(self, top, bottom):
        top = top.replace(" ", "%20").replace("#", "%23")
        bottom = bottom.replace(" ", "%20").replace("#", "%23")

        url = self._api_url(f"didyoumean?top={top}&bottom={bottom}")

        return Image(url, self._http_client)

    async def dogs(self):
        url = await self._http_client.get(self._api_url("dogs"), res_method = "json")

        return url['file']

    async def drake(self, top, bottom):
        top = top.replace(" ", "%20").replace("#", "%23")
        bottom = bottom.replace(" ", "%20").replace("#", "%23")
        url = self._api_url(f"drake?top={top}&bottom={bottom}")

        return Image(url, self._http_client)

    async def facts(self, text):
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self._api_url(f"facts?text={text}")

        return Image(url, self._http_client)

    async def filter(self, name, image: str):
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

    async def floor(self, text, image: str = None):
        text = text.replace(" ", "%20").replace("#", "%23")
        if image is not None:
            get_url = url_regex.UrlRegex(str(image))
            if not get_url.detect:
                raise BadRequest("String passed is not a valid URL.")
            image = f"&image={image}"
        url = self._api_url(f"floor?text={text}{image}")

        return Image(url, self._http_client)

    async def fml(self):
        url = await self._http_client.get(self._api_url("fml"), res_method = "json")

        return url.get("text")

    async def jokeoverhead(self, image: str):
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")
        url = self._api_url(f"jokeoverhead?image={image}")

        return Image(url, self._http_client)

    async def pornhub(self, text, text2):
        text = text.replace(" ", "%20").replace("#", "%23")
        text2 = text2.replace(" ", "%20").replace("#", "%23")
        url = self._api_url(f"pornhub?text={text}&text2={text2}")

        return Image(url, self._http_client)

    async def sadcat(self):
        url = await self._http_client.get(self._api_url("sadcat"), res_method = "json")

        return url['file']

    async def salty(self, image: str):
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")
        url = self._api_url(f"salty?image={image}")

        return Image(url, self._http_client)

    async def scroll(self, text):
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self._api_url(f"scroll?text={text}")

        return Image(url, self._http_client)

    async def ship(self, user: str, user2: str):
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

    async def steam(self, profile):
        try:
            response = await self._http_client.get(self._api_url(f"steam/user/{profile}"), res_method = "json")
        except aiohttp.ContentTypeError:
            raise NotFound("User not found on steam.")

        return Steam(response)

    async def supreme(self, text, dark=False, light=False):
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

    async def trash(self, face: str, trash: str):
        user_url = url_regex.UrlRegex(str(face))
        if not user_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if user_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        user2_url = url_regex.UrlRegex(str(trash))
        if not user2_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if user2_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self._api_url(f"trash?user={face}&user2={trash}")

        return Image(url, self._http_client)

    async def close(self):
        await self._http_client.close()

import io
import random
import re

import aiohttp
import url_regex

from . import http
from .colour import Colour
from .steam import SteamUser


class BadRequest(Exception):
    pass


class SteamUserNotFound(Exception):
    pass


class Client:
    _BASE_URL = "https://api.alexflipnote.dev/"

    def __init__(self):
        self._http_client = http

    def api_url(self, path):
        return self._BASE_URL + path

    async def to_bytes(self, url):
        read_url = await self._http_client.get(str(url), res_method = "read")
        bio = io.BytesIO(read_url)
        bio.seek(0)
        return bio

    async def achievement(self, text, icon: int = "", return_bytes=False):
        if icon is not None:
            icon = "&icon={}".format(icon)

        url = self.api_url("achievement?text={}{}".format(text, icon))

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def amiajoke(self, image: str, return_bytes=False):
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self.api_url("amiajoke?image={}".format(image))

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def bad(self, image: str, return_bytes=False):
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self.api_url("bad?image={}".format(image))

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    @property
    async def birb(self, return_bytes=False):
        url = await self._http_client.get(self.api_url("bad"), res_method = "json")

        if return_bytes:
            get_url = (await self._http_client.get(str(url), res_method = "read"))['file']
            read_url = await self._http_client.get(str(get_url), res_method = "read")
            bio = io.BytesIO(read_url)
            bio.seek(0)
            return bio

        return url['file']

    async def calling(self, text, return_bytes):
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self.api_url("calling?text={}".format(text))

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def captcha(self, text, return_bytes):
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self.api_url("captcha?text={}".format(text))

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    @property
    async def cats(self, return_bytes=False):
        url = await self._http_client.get(self.api_url("cats"), res_method = "json")

        if return_bytes:
            get_url = (await self._http_client.get(str(url), res_method = "read"))['file']
            image_bytes = await self.to_bytes(get_url)
            return image_bytes

        return url['file']

    async def challenge(self, text, icon: int = "", return_bytes=False):
        if icon is not None:
            icon = "&icon={}".format(icon)

        text = text.replace(" ", "%20").replace("#", "%23")
        url = self.api_url("challenge?text={}{}".format(text, icon))

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def colour(self, colour=None):
        if colour is None:
            colour = "%06x" % random.randint(0, 0xFFFFFF)

        if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        response = await self._http_client.get(
            str(self.api_url("colour/{}").format(colour)),
            res_method = "json"
        )
        return Colour(response)

    color = colour  # aliases to colour

    async def github_colours(self):

        url = self.api_url("color/github")

        return url

    github_colour = github_colour  # aliases to github_colour

    async def colour_image(self, colour=None, return_bytes=False):
        if colour is None:
            colour = "%06x" % random.randint(0, 0xFFFFFF)

        if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        url = self.api_url("colour/image/{}".format(colour))

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    color_image = colour_image  # aliases to colour_image

    async def colour_image_gradient(self, colour=None, return_bytes=False):
        if colour is None:
            colour = "%06x" % random.randint(0, 0xFFFFFF)

        if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        url = self.api_url("colour/image/gradient/{}".format(colour))

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def colourify(self, image, c="", b="", return_bytes=False):
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")

        if c is not None:
            if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', c):
                raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

            c = "&c={}".format(c)

        if b is not None:
            if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', b):
                raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

            b = "&b={}".format(b)

        url = self.api_url("colourify?image={}{}{}".format(image, c, b))

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def didyoumean(self, top, bottom):
        top = top.replace(" ", "%20").replace("#", "%23")
        bottom = bottom.replace(" ", "%20").replace("#", "%23")
        url = self.api_url("didyoumean?top={}&bottom={}".format(top, bottom))
        return url

    @property
    async def dogs(self):
        url = await self._http_client.get(self.api_url("dogs"), res_method = "json")
        return url['file']

    async def drake(self, top, bottom):
        top = top.replace(" ", "%20").replace("#", "%23")
        bottom = bottom.replace(" ", "%20").replace("#", "%23")
        url = self.api_url("drake?top={}&bottom={}".format(top, bottom))
        return url

    async def facts(self, text):
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self.api_url("facts?text={}".format(text))
        return url

    async def filter(self, name, image: str):
        options = ['blur', 'invert', 'b&w', 'deepfry', 'snow', 'gay',
                   'pixelate', 'jpegify', 'magik', 'communist']
        if name not in options:
            raise BadRequest(name + "is not a valid option! valid options: " + ", ".join(options))

        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self.api_url("filter/{}?image={}".format(name, image))
        return url

    async def floor(self, text, image: str = None):
        text = text.replace(" ", "%20").replace("#", "%23")
        if image is not None:
            get_url = url_regex.UrlRegex(str(image))
            if not get_url.detect:
                raise BadRequest("String passed is not a valid URL.")
            image = "&image={}".format(image)
        url = self.api_url("floor?text={}{}".format(text, image))
        return url

    @property
    async def fml(self):
        url = await self._http_client.get(self.api_url("fml"), res_method = "json")
        return url['text']

    async def jokeoverhead(self, image: str):
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")
        url = self.api_url("jokeoverhead?image={}".format(image))
        return url

    async def pornhub(self, text, text2):
        text = text.replace(" ", "%20").replace("#", "%23")
        text2 = text2.replace(" ", "%20").replace("#", "%23")
        url = self.api_url("pornhub?text={}&text2={}".format(text, text2))
        return url

    @property
    async def sadcat(self):
        url = await self._http_client.get(self.api_url("sadcat"), res_method = "json")
        return url['file']

    async def salty(self, image: str):
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")
        url = self.api_url("salty?image={}".format(image))
        return url

    async def scroll(self, text):
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self.api_url("scroll?text={}".format(text))
        return url

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

        url = self.api_url("ship?user={}&user2={}".format(user, user2))
        return url

    async def steam(self, profile):
        try:
            response = await self._http_client.get(self.api_url("steam/user/{}".format(profile)), res_method = "json")
        except aiohttp.ContentTypeError:
            raise SteamUserNotFound("SteamUser user not found.")

        return SteamUser(response)

    async def supreme(self, text, dark=False, light=False):
        text = text.replace(" ", "%20").replace("#", "%23")
        darkorlight = ""
        if dark:
            darkorlight = "&dark=true"
        if light:
            darkorlight = "&light=true"
        if dark and light:
            raise BadRequest("You can't choose both dark and light.")

        url = self.api_url("supreme?text={}{}".format(text, darkorlight))
        return url

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

        url = self.api_url("trash?user={}&user2={}".format(face, trash))
        return url

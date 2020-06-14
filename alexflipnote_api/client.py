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
    # SR API BASE PATH
    _BASE_URL = "https://api.alexflipnote.dev/"

    def __init__(self):
        self._http_client = http

    def api_url(self, path):
        return self._BASE_URL + path

    async def achievement(self, text, icon: int = None):
        icons = "https://i.alexflipnote.dev/9ZXAP35.png"
        if icon is not None:
            if icon > 39:
                raise BadRequest("There are only 39 icons, see them all here {}".format(icons))
        url = self.api_url("achievement?text={}&icon={}".format(text, icon))
        return url

    async def amiajoke(self, image: str):
        get_url = url_regex.UrlRegex(image)
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self.api_url("amiajoke?image={}".format(image))
        return url

    async def bad(self, image: str):
        get_url = url_regex.UrlRegex(image)
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self.api_url("bad?image={}".format(image))
        return url

    @property
    async def birb(self):
        url = await self._http_client.get(self.api_url("bad"), res_method = "json")
        return url['file']

    async def calling(self, text):
        url = self.api_url("calling?text={}".format(text))
        return url

    async def captcha(self, text):
        url = self.api_url("captcha?text={}".format(text))
        return url

    @property
    async def cats(self):
        url = await self._http_client.get(self.api_url("cats"), res_method = "json")
        return url['file']

    async def challenge(self, text, icon: int = None):
        url = self.api_url("challenge?text={}&icon={}".format(text, icon))
        return url

    async def colour(self, colour):
        if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")
        response = await self._http_client.get(str(self.api_url("colour/{}").format(colour)), res_method="json")
        return Colour(response)

    async def github_colour(self):
        url = await self._http_client.get(self.api_url("color/github"))
        return url

    async def colour_image(self, colour):
        url = self.api_url("colour/image/{}".format(colour))
        return url

    async def colour_image_gradient(self, colour):
        url = self.api_url("colour/image/gradient/{}".format(colour))
        return url

    async def colourify(self, image, c=None, b=None):
        get_url = url_regex.UrlRegex(image)
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")

        url = self.api_url("colourify?image={}&c={}&b={}".format(image, c, b))
        return url

    async def didyoumean(self, top, bottom):
        url = self.api_url("didyoumean?top={}&bottom={}".format(top, bottom))
        return url

    @property
    async def dogs(self):
        url = await self._http_client.get(self.api_url("dogs"), res_method = "json")
        return url['file']

    async def drake(self, top, bottom):
        url = self.api_url("drake?top={}&bottom={}".format(top, bottom))
        return url

    async def facts(self, text):
        url = self.api_url("facts?text={}".format(text))
        return url

    async def filter(self, name, image: str):
        options = ['blur', 'invert', 'b&w', 'deepfry', 'snow', 'gay',
                   'pixelate', 'jpegify', 'magik', 'communist']
        if name not in options:
            raise BadRequest(name + "is not a valid option! valid options: " + ", ".join(options))

        get_url = url_regex.UrlRegex(image)
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self.api_url("filter/{}?image={}".format(name, image))
        return url

    async def floor(self, text, image: str = None):
        if image is not None:
            get_url = url_regex.UrlRegex(image)
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
        get_url = url_regex.UrlRegex(image)
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")
        url = self.api_url("jokeoverhead?image={}".format(image))
        return url

    async def pornhub(self, text, text2):
        url = self.api_url("pornhub?text={}&text2={}".format(text, text2))
        return url

    @property
    async def sadcat(self):
        url = await self._http_client.get(self.api_url("sadcat"), res_method = "json")
        return url['file']

    async def salty(self, image: str):
        get_url = url_regex.UrlRegex(image)
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")
        url = self.api_url("salty?image={}".format(image))
        return url

    async def scroll(self, text):
        url = self.api_url("scroll?text={}".format(text))
        return url

    async def ship(self, user: str, user2: str):
        user_url = url_regex.UrlRegex(user)
        if not user_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if user_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        user2_url = url_regex.UrlRegex(user2)
        if not user2_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if user2_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self.api_url("ship?user={}&user2={}".format(user, user2))
        return url

    async def steam(self, profile):
        try:
            response = await self._http_client.get(self.api_url("steam/user/{}".format(profile)), res_method="json")
        except aiohttp.ContentTypeError:
            raise SteamUserNotFound("SteamUser user not found.")

        return SteamUser(response)

    async def supreme(self, text, dark=False, light=False):
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
        user_url = url_regex.UrlRegex(face)
        if not user_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if user_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        user2_url = url_regex.UrlRegex(trash)
        if not user2_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if user2_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self.api_url("ship?user={}&user2={}".format(face, trash))
        return url

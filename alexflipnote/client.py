import io
import random
import re

import aiohttp
import url_regex

from . import http
from .classes import Colour
from .classes import Steam


class BadRequest(Exception):
    pass

class NotFound(Exception):
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
            icon = f"&icon={icon}"

        url = self.api_url(f"achievement?text={text}{icon}")

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

        url = self.api_url("amiajoke?image={image}")

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

        url = self.api_url("bad?image={image}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    @property
    async def birb(self):
        url = await self._http_client.get(self.api_url("bad"), res_method = "json")
        return url['file']

    async def calling(self, text, return_bytes):
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self.api_url(f"calling?text={text}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def captcha(self, text, return_bytes):
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self.api_url(f"captcha?text={text}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    @property
    async def cats(self):
        url = await self._http_client.get(self.api_url("cats"), res_method = "json")
        return url['file']

    async def challenge(self, text, icon: int = "", return_bytes=False):
        if icon is not None:
            icon = f"&icon={icon}"

        text = text.replace(" ", "%20").replace("#", "%23")
        url = self.api_url(f"challenge?text={text}{icon}")

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
            str(self.api_url(f"colour/{colour}")),
            res_method = "json"
        )
        return Colour(response)

    color = colour  # aliases to colour

    async def github_colours(self):
        url = self.api_url("color/github")
        return url

    github_colour = github_colours  # aliases to github_colour

    async def colour_image(self, colour=None, return_bytes=False):
        if colour is None:
            colour = "%06x" % random.randint(0, 0xFFFFFF)

        if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        url = self.api_url(f"colour/image/colour")

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

        url = self.api_url(f"colour/image/gradient/{colour}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def colourify(self, image, colour="", background="", return_bytes=False):
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

        url = self.api_url(f"colourify?image={image}{colour}{background}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def didyoumean(self, top, bottom, return_bytes=False):
        top = top.replace(" ", "%20").replace("#", "%23")
        bottom = bottom.replace(" ", "%20").replace("#", "%23")

        url = self.api_url(f"didyoumean?top={top}&bottom={bottom}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    @property
    async def dogs(self):
        url = await self._http_client.get(self.api_url("dogs"), res_method = "json")
        return url['file']

    async def drake(self, top, bottom, return_bytes=False):
        top = top.replace(" ", "%20").replace("#", "%23")
        bottom = bottom.replace(" ", "%20").replace("#", "%23")
        url = self.api_url(f"drake?top={top}&bottom={bottom}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def facts(self, text, return_bytes=False):
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self.api_url(f"facts?text={text}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def filter(self, name, image: str, return_bytes=False):
        options = ['blur', 'invert', 'b&w', 'deepfry', 'snow', 'gay',
                   'pixelate', 'jpegify', 'magik', 'communist']
        if name not in options:
            raise NotFound("Filter not found. Valid options: " + ", ".join(options))

        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")

        url = self.api_url(f"filter/{name}?image={image}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def floor(self, text, image: str = None, return_bytes=False):
        text = text.replace(" ", "%20").replace("#", "%23")
        if image is not None:
            get_url = url_regex.UrlRegex(str(image))
            if not get_url.detect:
                raise BadRequest("String passed is not a valid URL.")
            image = f"&image={image}"
        url = self.api_url(f"floor?text={text}{image}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes
        return url

    @property
    async def fml(self):
        url = await self._http_client.get(self.api_url("fml"), res_method = "json")
        return url['text']

    async def jokeoverhead(self, image: str, return_bytes=False):
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")
        url = self.api_url(f"jokeoverhead?image={image}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def pornhub(self, text, text2, return_bytes=False):
        text = text.replace(" ", "%20").replace("#", "%23")
        text2 = text2.replace(" ", "%20").replace("#", "%23")
        url = self.api_url(f"pornhub?text={text}&text2={text2}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    @property
    async def sadcat(self):
        url = await self._http_client.get(self.api_url("sadcat"), res_method = "json")
        return url['file']

    async def salty(self, image: str, return_bytes=False):
        get_url = url_regex.UrlRegex(str(image))
        if not get_url.detect:
            raise BadRequest("String passed is not a valid URL.")
        if get_url.links[0].domain != "cdn.discordapp.com":
            raise BadRequest("Only Discord CDN URLs are allowed...")
        url = self.api_url(f"salty?image={image}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def scroll(self, text, return_bytes=False):
        text = text.replace(" ", "%20").replace("#", "%23")
        url = self.api_url(f"scroll?text={text}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def ship(self, user: str, user2: str, return_bytes=False):
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

        url = self.api_url(f"ship?user={user}&user2={user2}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def steam(self, profile):
        try:
            response = await self._http_client.get(self.api_url(f"steam/user/{profile}"), res_method = "json")
        except aiohttp.ContentTypeError:
            raise NotFound("User not found on steam.")

        return Steam(response)

    async def supreme(self, text, dark=False, light=False, return_bytes=False):
        text = text.replace(" ", "%20").replace("#", "%23")
        darkorlight = ""
        if dark:
            darkorlight = "&dark=true"
        if light:
            darkorlight = "&light=true"
        if dark and light:
            raise BadRequest("You can only choose either light or dark, not both.")

        url = self.api_url(f"supreme?text={text}{darkorlight}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

    async def trash(self, face: str, trash: str, return_bytes=False):
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

        url = self.api_url(f"trash?user={face}&user2={trash}")

        if return_bytes:
            image_bytes = await self.to_bytes(url)
            return image_bytes

        return url

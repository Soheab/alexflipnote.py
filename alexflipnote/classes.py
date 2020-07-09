import enum
from io import BytesIO

import typing
from alexflipnote.http import HTTPSession


class Image:
    __slots__ = ("url", "_http_client")

    def __init__(self, url: str, http_client) -> None:
        self.url = url
        self._http_client = http_client

    def __str__(self) -> str:
        return self.url if self.url is not None else ''

    async def read(self) -> BytesIO:
        _bytes = await self._http_client.get(str(self.url), res_method = "read")
        return BytesIO(_bytes)


class Colour:
    __slots__ = ("blackorwhite_text", "brightness", "hex", "image", "image_gradient",
                 "int", "name", "rgb", "rgb_values", "shade", "tint")

    def __init__(self, data: typing.Dict[str, typing.Any]) -> None:
        self.blackorwhite_text = data.get('blackorwhite_text')
        self.brightness = data['brightness']
        self.hex = data['hex']
        self.image = data['image']
        self.image_gradient = data['image_gradient']
        self.int = data['int']
        self.name = data['name']
        self.rgb = data['rgb']
        self.rgb_values = self.ColourRGB(data)
        self.shade = data['shade']
        self.tint = data['tint']

    class ColourRGB:
        __slots__ = ("all", "r", "g", "b")

        def __init__(self, data: typing.Dict[str, typing.Any]) -> None:
            self.all = data['rgb_values']
            self.r = self.all['r']
            self.g = self.all['g']
            self.b = self.all['b']


class Steam:
    __slots__ = ("id", "avatars", "profile")

    def __init__(self, data: typing.Dict[str, typing.Any]) -> None:
        self.id = self.SteamID(data)
        self.avatars = self.SteamAvatar(data)
        self.profile = self.SteamProfile(data)

    class SteamID:
        __slots__ = ("steamid3", "steamid32", "steamid64", "custom_url")

        def __init__(self, data: typing.Dict[str, typing.Any]) -> None:
            _data = data['id']
            self.steamid3 = _data['steamid3']
            self.steamid32 = _data['steamid32']
            self.steamid64 = _data['steamid64']
            self.custom_url = _data['customurl']

    class SteamAvatar:
        __slots__ = ("avatar", "avatar_medium", "avatar_full")

        def __init__(self, data: typing.Dict[str, typing.Any]) -> None:
            _data = data['avatars']
            self.avatar = _data['avatar']
            self.avatar_medium = _data['avatarmedium']
            self.avatar_full = _data['avatarfull']

    class SteamProfile:
        __slots__ = ("username", "real_name", "url", "summary", "background",
                     "location", "state", "privacy", "time_created", "vacbanned")

        def __init__(self, data: typing.Dict[str, typing.Any]) -> None:
            _data = data['profile']
            self.username = _data['username']
            self.real_name = _data['realname']
            self.url = _data['url']
            self.summary = _data['summary']
            self.background = _data['background']
            self.location = _data['location']
            self.state = _data['state']
            self.privacy = _data['privacy']
            self.time_created = _data['timecreated']
            self.vacbanned: bool = _data['vacbanned']


class Icon(enum.Enum):
    grass_block = 1
    diamond = 2
    diamond_sword = 3
    creeper = 4
    pig = 5
    tnt = 6
    cookie = 7
    heart = 8
    bed = 9
    cake = 10
    sign = 11
    rail = 12
    crafting_bench = 13
    redstone = 14
    fire = 15
    cobweb = 16
    chest = 17
    furnace = 18
    book = 19
    stone_block = 20
    wooden_plank_block = 21
    iron_ingot = 22
    gold_ingot = 23
    wooden_door = 24
    iron_door = 25
    diamond_chestplate = 26
    flint_and_steel = 27
    glass_bottle = 28
    splash_potion = 29
    creeper_spawnegg = 30
    coal = 31
    iron_sword = 32
    bow = 33
    arrow = 34
    iron_chestplate = 35
    bucket = 36
    bucket_with_water = 37
    bucket_with_lava = 38
    bucket_with_milk = 39
    diamond_boots = 40
    wooden_hoe = 41
    bread = 42
    wooden_sword = 43
    bone = 44

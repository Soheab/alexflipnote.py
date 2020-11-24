from enum import Enum
from io import BytesIO
from typing import Union

from aiohttp import ClientResponse


class Image:
    def __init__(self, url: str, session) -> None:
        self.url: str = url
        self.response: ClientResponse = session

    def __str__(self) -> str:
        return self.url if self.url is not None else ""

    async def read(self, bytesio = True) -> Union[bytes, BytesIO]:
        _bytes = await self.response.read()
        if bytesio is False:
            return _bytes

        return BytesIO(_bytes)


class Colour:
    __slots__ = (
        "blackorwhite_text",
        "brightness",
        "hex",
        "image",
        "image_gradient",
        "int",
        "name",
        "rgb",
        "rgb_values",
        "shade",
        "tint",
    )

    def __init__(self, data) -> None:
        self.blackorwhite_text: str = data.get("blackorwhite_text")
        self.brightness: int = data.get("brightness")
        self.hex: str = data.get("hex")
        self.image: str = data.get("image")
        self.image_gradient: str = data.get("image_gradient")
        self.int: int = data.get("int")
        self.name: str = data.get("name")
        self.rgb: str = data.get("rgb")
        self.rgb_values: Colour.ColourRGB = Colour.ColourRGB(data.get("rgb_values"))
        self.shade: list = data.get("shade")
        self.tint: list = data.get("tint")

    class ColourRGB:
        __slots__ = ("all", "r", "g", "b")

        def __init__(self, data) -> None:
            self.all: dict = data
            self.r: int = data.get("r")
            self.g: int = data.get("g")
            self.b: int = data.get("b")


class MinecraftIcons(Enum):
    GRASS_BLOCK = 1
    GRASSBLOCK = 1  # alias
    DIAMOND = 2
    DIAMOND_SWORD = 3
    DIAMONDSWORD = 3  # alias
    CREEPER = 4
    PIG = 5
    TNT = 6
    COOKIE = 7
    HEART = 8
    BED = 9
    CAKE = 10
    SIGN = 11
    RAIL = 12
    CRAFTING_BENCH = 13
    CRAFTINGBENCH = 13  # alias
    REDSTONE = 14
    FIRE = 15
    COBWEB = 16
    CHEST = 17
    FURNACE = 18
    BOOK = 19
    STONE_BLOCK = 20
    STONEBLOCK = 20  # alias
    WOODEN_PLANK_BLOCK = 21
    WOODENPLANKBLOCK = 21  # alias
    IRON_INGOT = 22
    IRONINGOT = 22  # alias
    GOLD_INGOT = 23
    GOLDINGOT = 23  # alias
    WOODEN_DOOR = 24
    WOODENDOOR = 24  # alias
    IRON_DOOR = 25
    IRONDOOR = 25  # alias
    DIAMOND_CHESTPLATE = 26
    DIAMONDCHESTPLATE = 26  # alias
    FLINT_AND_STEEL = 27
    FLINTANDSTEEL = 27  # alias
    GLASS_BOTTLE = 28
    GLASSBOTTLE = 28  # alias
    SPLASH_POTION = 29
    SPLASHPOTION = 29  # alias
    CREEPER_SPAWNEGG = 30
    CREEPERSPAWNEGG = 38  # alias
    COAL = 31
    IRON_SWORD = 32
    IRONSWORD = 32  # alias
    BOW = 33
    ARROW = 34
    IRON_CHESTPLATE = 35
    IRONCHESTPLATE = 35  # alias
    BUCKET = 36
    BUCKET_WITH_WATER = 37
    BUCKETWITHWATER = 37  # alias
    BUCKET_WITH_LAVA = 38
    BUCKETWITHLAVA = 38  # alias
    BUCKET_WITH_MILK = 39
    BUCKETWITHMILK = 39  # alias
    diamond_boots = 40
    DIAMONDBOOTS = 40  # alias
    WOODEN_HOE = 41
    WOODENHOE = 41  # alias
    BREAD = 42
    WOODEN_SWORD = 43
    WOORDENSWORD = 43  # alias
    BONE = 44
    OAK_LOG = 45
    OAKLOG = 45  # alias
    RANDOM = 46


class Filters(Enum):
    BLUR = 1
    INVERT = 2
    BLACK_AND_WHITE = 3  # b&w
    DEEPFRY = 4
    SEPIA = 5
    PIXELATE = 6
    MAGIK = 7
    JPEGIFY = 8
    WIDE = 9
    SNOW = 10
    GAY = 11
    COMMUNIST = 12
    RANDOM = 13

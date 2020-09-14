import enum
from io import BytesIO


class Image:

    def __init__(self, url: str, session) -> None:
        self.url = url
        self.session = session

    def __str__(self) -> str:
        return self.url if self.url is not None else ''

    async def read(self) -> BytesIO:
        _bytes = await (await self.session.get(str(self.url))).read()
        return BytesIO(_bytes)


class Colour:
    __slots__ = ("blackorwhite_text", "brightness", "hex", "image", "image_gradient",
                 "int", "name", "rgb", "rgb_values", "shade", "tint")

    def __init__(self, data) -> None:
        self.blackorwhite_text = data.get('blackorwhite_text')
        self.brightness = data.get('brightness')
        self.hex = data.get('hex')
        self.image = data.get('image')
        self.image_gradient = data.get('image_gradient')
        self.int = data.get('int')
        self.name = data.get('name')
        self.rgb = data.get('rgb')
        self.rgb_values = self.ColourRGB(data.get('rgb_values'))
        self.shade = data.get('shade')
        self.tint = data.get('tint')

    class ColourRGB:
        __slots__ = ("all", "r", "g", "b")

        def __init__(self, data) -> None:
            self.all = data
            self.r = data.get('r')
            self.g = data.get('g')
            self.b = data.get('b')


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
    oak_log = 45

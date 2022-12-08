from typing import Tuple, Optional, Union

from enum import Enum

from .utils import _try_enum

__all__: Tuple[str, ...] = (
    "Endpoint",
    "NFTSeason",
    "MinecraftIcon",
)


class _BaseEnum(Enum):
    def __str__(self):
        return self.value

    def _try_value(self, value: Union[str, int]) -> Optional[Enum]:
        return _try_enum(self.__class__, value)


class Endpoint(_BaseEnum):
    ACHIEVEMENT = "/achievement"
    CALLING = "/calling"
    CAPTCHA = "/captcha"
    CHALLENGE = "/challenge"
    DID_YOU_MEAN = "/didyoumean"
    DRAKE = "/drake"
    FACTS = "/facts"
    PORNHUB = "/pornhub"
    SCROLL = "/scroll"


class WithJsonEndpoint(_BaseEnum):
    COFFEE = "PLACEHOLDER"
    BIRB = "/birb"
    CATS = "/cats"
    SADCAT = "/sadcat"
    COLOR = "/color"
    DOGS = "/dogs"


class MinecraftEndpoint(_BaseEnum):
    ACHIEVEMENT = "/achievement"
    CHALLENGE = "/challenge"


class WithDocsEndpoint(_BaseEnum):
    NFT = "/nft"
    SILLYCAT = "/sillycat"


class MinecraftIcon(_BaseEnum):
    """Minecraft icons for the Minecraft endpoints. (achievement, challenge)"""

    GRASS_BLOCK = 1
    DIAMOND = 2
    DIAMOND_SWORD = 3
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
    REDSTONE = 14
    FIRE = 15
    COBWEB = 16
    CHEST = 17
    FURNACE = 18
    BOOK = 19
    STONE_BLOCK = 20
    WOODEN_PLANK_BLOCK = 21
    IRON_INGOT = 22
    GOLD_INGOT = 23
    WOODEN_DOOR = 24
    IRON_DOOR = 25
    DIAMOND_CHESTPLATE = 26
    FLINT_AND_STEEL = 27
    GLASS_BOTTLE = 28
    SPLASH_POTION = 29
    CREEPER_SPAWNEGG = 30
    COAL = 31
    IRON_SWORD = 32
    BOW = 33
    ARROW = 34
    IRON_CHESTPLATE = 35
    BUCKET = 36
    BUCKET_WITH_WATER = 37
    BUCKET_WITH_LAVA = 38
    BUCKET_WITH_MILK = 39
    DIAMOND_BOOTS = 40
    WOODEN_HOE = 41
    BREAD = 42
    WOODEN_SWORD = 43
    BONE = 44
    OAK_LOG = 45
    RANDOM = 46

    # ALIASES -------------------
    GRASSBLOCK = 1
    DIAMONDSWORD = 3
    CRAFTINGBENCH = 13
    STONEBLOCK = 20
    WOODENPLANKBLOCK = 21
    IRONINGOT = 22
    GOLDINGOT = 23
    WOODENDOOR = 24
    IRONDOOR = 25
    DIAMONDCHESTPLATE = 26
    FLINTANDSTEEL = 27
    GLASSBOTTLE = 28
    SPLASHPOTION = 29
    CREEPERSPAWNEGG = 38
    IRONSWORD = 32
    IRONCHESTPLATE = 35
    BUCKETWITHWATER = 37
    BUCKETWITHLAVA = 38
    BUCKETWITHMILK = 39
    DIAMONDBOOTS = 40
    WOODENHOE = 41
    WOORDENSWORD = 43
    OAKLOG = 45

    def __str__(self):
        return self.name.lower()


class NFTSeason(_BaseEnum):
    """Seasons for the NFT endpoint."""

    NONE = "none"
    APRIL = "april"
    AUTUMN = "autumn"
    CHRISTMAS = "christmas"
    HALLOWEEN = "halloween"
    NORWAY = "norway"
    SPRING = "spring"
    SUMMER = "summer"
    WINTER = "winter"
    RANDOM = "random"

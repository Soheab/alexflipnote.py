from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional, Tuple, Union

from dataclasses import dataclass

from .image import Image

if TYPE_CHECKING:
    from typing_extensions import Self

    from ..http import HTTPClient
    from .._types.colour import (
        Colour as ColourData,
        ColourWithWebsafe as ColourWithWebsafeData,
        ColourImages as ColourImagesData,
    )

__all__: Tuple[str, ...] = (
    "Colour",
    "ColourWebSafe",
    "RGBKeys",
    "StringKeyWithValues",
    "SafeTextColourRGB",
    "SafeTextColour",
    "Hex",
    "RGB",
    "HSL",
    "CMYK",
    "ColourImages",
)


@dataclass(frozen=True)
class RGBKeys:
    r: int
    g: int
    b: int


@dataclass(frozen=True)
class StringKeyWithValues:
    string: str
    values: List[Union[str, int]]


@dataclass(frozen=True)
class SafeTextColourRGB(RGBKeys):
    """Represents a class holding RGB values of a :class:`SafeTextColour`.

    Attributes
    ----------
    r: :class:`int`
        The red value of the colour.
    g: :class:`int`
        The green value of the colour.
    b: :class:`int`
        The blue value of the colour.
    values: List[:class:`int`]
        The RGB values of the colour as a list of integers.
    """

    values: List[int]


@dataclass(frozen=True)
class SafeTextColour:
    """Represents a class holding the "safe" version of a :class:`Colour`.

    Attributes
    ----------
    name: :class:`str`
        The name of the colour.
    hex: :class:`str`
        The hex value of the colour.
    rgb: :class:`RGBKeys`
        The RGB values of the colour.
    """

    name: str
    hex: str
    rgb: SafeTextColourRGB


@dataclass(frozen=True)
class Hex(StringKeyWithValues):
    """Represents a class holding information about a :class:`Colour`'s hex value.

    Attributes
    ----------
    string: :class:`str`
        The hex value of the colour.
    clean: :class:`str`
        The hex value of the colour without the ``#``.
    shorten: Optional[:class:`str`]
        The shortened hex value of the colour.
    values: List[:class:`str`]
        The hex value of the colour split into a list per two characters.
    """

    string: str
    clean: str
    shorten: Optional[str]
    values: List[str]


@dataclass(frozen=True)
class RGB(StringKeyWithValues, RGBKeys):
    """Represents a class holding RGB values of a :class:`Colour`.

    Attributes
    ----------
    string: :class:`str`
        The RGB value of the colour.
    r: :class:`int`
        The red value of the colour.
    g: :class:`int`
        The green value of the colour.
    b: :class:`int`
        The blue value of the colour.
    values: List[:class:`int`]
        The RGB values of the colour as a list of integers.
    """

    values: List[int]


@dataclass(frozen=True)
class HSL(StringKeyWithValues):
    """Represents a class holding HSL values of a :class:`Colour`.

    Attributes
    ----------
    string: :class:`str`
        The HSL value of the colour.
    h: :class:`int`
        The hue value of the colour.
    s: :class:`int`
        The saturation value of the colour.
    l: :class:`int`
        The lightness value of the colour.
    values: List[:class:`int`]
        The HSL values of the colour as a list of integers.
    """

    values: List[int]
    h: int
    s: int
    l: int


@dataclass(frozen=True)
class CMYK(StringKeyWithValues):
    """Represents a class holding the CMYK values of a :class:`Colour`.

    Attributes
    ----------
    string: :class:`str`
        The CMYK value of the colour.
    c: :class:`int`
        The cyan value of the colour.
    m: :class:`int`
        The magenta value of the colour.
    y: :class:`int`
        The yellow value of the colour.
    k: :class:`int`
        The black value of the colour.
    values: List[:class:`int`]
        The CMYK values of the colour as a list of integers.
    """

    values: List[int]
    c: int
    m: int
    y: int
    k: int


class ColourImages:
    """Represents a class holding the different images of a :class:.Colour`.

    Attributes
    ----------
    colour: :class:`Colour`
        The colour that this class is holding the images for.
    raw_square: :class:`str`
        The square image's URL.
    raw_gradient: :class:`str`
        The gradient image's URL.
    """

    __slots__: Tuple[str, ...] = ("colour", "raw_square", "raw_gradient")

    def __init__(self, original: Colour, data: ColourImagesData) -> None:
        self.colour: Colour = original
        self.raw_square: str = data["square"]
        self.raw_gradient: str = data["gradient"]

    def __str__(self) -> str:
        return self.raw_square

    def __repr__(self) -> str:
        return f"<ColourImages square={self.raw_square!r} gradient={self.raw_gradient!r}>"

    @property
    def square(self) -> Image:
        """:class:`Image`: Returns a square image of the colour."""
        return Image(self.raw_square, self.colour._http._session)  # type: ignore

    @property
    def gradient(self) -> Image:
        """:class:`Image`: Returns a image with all possible gradients of the colour."""
        return Image(self.raw_gradient, self.colour._http._session)  # type: ignore


class Colour:
    """Represents a colour from the API.

    Attributes
    ----------
    name: :class:`str`
        The name of the colour.
    int: :class:`int`
        The integer value of the colour.
    shades: List[:class:`str`]
        The shades of the colour.
    tints: List[:class:`str`]
        The tints of the colour.
    image: :class:`str`
        The image of the colour. This is an alias to :attr:`Colour.square`.
    """

    __slots__: Tuple[str, ...] = ("_http", "__data", "name", "int", "shades", "tints", "image")

    def __init__(self, http: HTTPClient, data: ColourWithWebsafeData) -> None:
        self._http: HTTPClient = http
        self.__data: ColourWithWebsafeData = data

        self.name: str = data["name"]
        self.int = data["int"]  # type: ignore # key is named int
        self.shades: List[str] = data["shade"]
        self.tints: List[str] = data["tint"]

        # aliases
        self.image = self.square

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Colour name={self.name!r} int={self.int!r} hex={self.hex.string!r} rgb={self.rgb!r}>"

    @property
    def images(self) -> ColourImages:
        """:class:`ColourImages`: Returns a class holding the different images of the colour.

        There are attributes on this class that can be used to get each image: :attr:`Colour.square` and :attr:`Colour.gradient`.
        """
        data = self.__data["images"]
        return ColourImages(self, data)

    @property
    def gradient(self) -> Image:
        """:class:`Image`: Returns a image with all possible gradients of the colour.

        This is an alias to :attr:`Colour.images.gradient`.
        """
        return self.images.gradient

    @property
    def square(self) -> Image:
        """:class:`Image`: Returns a square image of the colour.

        This is an alias to :attr:`Colour.images.square`.
        """
        return self.images.square

    @property
    def safe_text_colour(self) -> SafeTextColour:
        """:class:`SafeTextColour`: Returns a class holding the safe text colour of the colour.

        This can be used on images etc. to make sure the text is readable.
        """
        data = self.__data["safe_text_color"]
        rgb = SafeTextColourRGB(**data["rgb"])
        return SafeTextColour(name=data["name"], hex=data["hex"], rgb=rgb)

    @property
    def hex(self) -> Hex:
        """:class:`Hex`: Returns a class holding the hex value of the colour."""
        data = self.__data["hex"]
        return Hex(**data)

    @property
    def rgb(self) -> RGB:
        """:class:`RGB`: Returns a class holding the RGB values of the colour."""
        data = self.__data["rgb"]
        return RGB(**data)

    @property
    def hsl(self) -> HSL:
        """:class:`HSL`: Returns a class holding the HSL values of the colour."""
        data = self.__data["hsl"]
        return HSL(**data)

    @property
    def cmyk(self) -> CMYK:
        """:class:`CMYK`: Returns a class holding the CMYK values of the colour."""
        data = self.__data["cmyk"]
        return CMYK(**data)

    @property
    def websafe(self) -> Self:
        """:class:`Colour`: Returns a class holding the websafe version of the colour.

        This is for really old browsers that don't support the full colour range.
        """
        try:
            data = self.__data["websafe"]
            return ColourWebSafe(self._http, data)
        except KeyError:
            return self


class ColourWebSafe(Colour):
    """Represents a websafe version of a :class:`Colour`.

    The only difference between this and :class:`Colour` is that this class has a :attr:`websafe` attribute that returns itself.
    """

    def __init__(self, http: HTTPClient, data: ColourData) -> None:
        super().__init__(http, data)  # type: ignore # no websafe key

    @property
    def websafe(self) -> Self:
        """:class:`Colour`: Returns this class. This is to prevent an infinite loop when getting the websafe version of a websafe colour."""
        return self

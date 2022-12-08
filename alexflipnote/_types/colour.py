from typing import Optional, Tuple, TypedDict, List

__all__: Tuple[str, ...] = (
    "Colour",
    "ColourImages",
    "RGB",
    "Hex",
    "RGB",
    "CMYK",
    "HSL",
    "SafeTextColour",
    "SafeTextColourRGB",
    "HSLKeys",
    "CMYKKeys",
    "RGBKeys",
)


class RGBKeys(TypedDict):
    r: int
    g: int
    b: int


class HSLKeys(TypedDict):
    h: int
    s: int
    l: int


class CMYKKeys(TypedDict):
    c: int
    m: int
    y: int
    k: int


class HasStringKey(TypedDict):
    string: str


class StringWithValues(HasStringKey):
    values: List[int]


class SafeTextColourRGB(RGBKeys):
    values: List[int]


class SafeTextColour(TypedDict):
    name: str
    hex: str
    rgb: SafeTextColourRGB


class Hex(HasStringKey):
    clean: str
    shorten: Optional[str]
    values: List[str]


class RGB(StringWithValues, RGBKeys):
    ...


class HSL(StringWithValues, HSLKeys):
    ...


class CMYK(StringWithValues, CMYKKeys):
    ...


class ColourImages(TypedDict):
    square: str
    gradient: str


class Colour(TypedDict):
    name: str
    images: ColourImages
    _int: int  # actual name is int, but that's a reserved keyword
    brightness: int
    safe_text_color: SafeTextColour
    hex: Hex
    rgb: RGB
    hsl: HSL
    cmyk: CMYK
    shade: List[str]
    tint: List[str]


class ColourWithWebsafe(Colour):
    websafe: Colour

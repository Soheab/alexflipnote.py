from typing import List, Tuple, TypedDict

__all__: Tuple[str, ...] = ("Colour", "RGB")


class ColourDataRGB(TypedDict):
    r: int
    g: int
    b: int


class ColourData(TypedDict):
    blackorwhite_text: str
    brightness: int
    hex: str
    image: str
    image_gradient: str
    int: int
    name: str
    rgb: str
    rgb_values: ColourDataRGB
    shade: List[str]
    tint: List[str]


class Colour:
    __slots__: Tuple[str, ...] = (
        "black_or_white_text",
        "brightness",
        "hex",
        "image",
        "gradient",
        "int",
        "name",
        "rgb_string",
        "rgb",
        "shades",
        "tints",
    )

    def __init__(self, data: ColourData) -> None:
        self.black_or_white_text: str = data["blackorwhite_text"]
        self.brightness: int = data["brightness"]
        self.hex: str = data["hex"]
        self.image: str = data["image"]
        self.gradient: str = data["image_gradient"]
        self.int: int = data["int"]
        self.name: str = data["name"]
        self.rgb_string: str = data["rgb"]
        self.rgb: RGB = RGB(data["rgb_values"])
        self.shades: List[str] = data["shade"]
        self.tints: List[str] = data["tint"]

    def __str__(self) -> str:
        return self.hex

    def __int__(self) -> int:
        return self.int

    def __repr__(self) -> str:
        return f"<Colour name={self.name} hex={self.hex} image={self.image}>"


class RGB:
    __slots__: Tuple[str, ...] = ("raw", "r", "g", "b")

    def __init__(self, data: ColourDataRGB) -> None:
        self.raw: ColourDataRGB = data
        self.r: int = data["r"]
        self.g: int = data["g"]
        self.b: int = data["b"]

    def __str__(self) -> str:
        return f"{self.r}, {self.g}, {self.b}"

    def __repr__(self) -> str:
        return f"<RGB r={self.r} g={self.g} b={self.b}>"

from typing import TypedDict

from .http import BaseDocs


class SillycatVariables(TypedDict):
    HEX: str


class SillycatPosition(TypedDict):
    hex: str
    name: str


class SillycatImages(TypedDict):
    simple: str
    complex: str


class Sillycat(BaseDocs):
    _variables: SillycatVariables  # type: ignore
    left: SillycatPosition
    right: SillycatPosition
    images: SillycatImages

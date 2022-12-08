from typing import TypedDict, Literal, List

from .http import BaseDocs

NFTSeason = Literal["none", "april", "autumn", "christmas", "halloween", "norway", "spring", "summer", "winter"]


class NFTVariables(TypedDict):
    HEX: str
    SESSION: List[NFTSeason]


class NFT(BaseDocs):
    _variables: NFTVariables  # type: ignore
    hex: str
    season: NFTSeason
    name: str
    image: str

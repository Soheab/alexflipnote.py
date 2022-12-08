from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Tuple

from .image import Image
from ..enums import NFTSeason
from .. import utils as _utils

if TYPE_CHECKING:
    from ..http import HTTPClient
    from .._types.nft import NFT as NFTData

__all__: Tuple[str, ...] = ("NFT",)


class NFT:
    """Represents a NFT image.

    Attributes
    ----------
    season: :class:`NFTSeason`
        The season of the NFT.
    hex: :class:`str`
        The colour of the NFT.
    """

    __slots__: Tuple[str, ...] = ("__data", "__http", "hex", "season")

    def __init__(self, data: NFTData, http: HTTPClient) -> None:
        self.__data: NFTData = data
        self.__http: HTTPClient = http

        self.season: NFTSeason = _utils._try_enum(NFTSeason, data["season"])  # type: ignore
        self.hex: str = data["hex"]

    def __str__(self) -> str:
        return self.image.url

    def __repr__(self) -> str:
        return f"<NFT season={self.season!r} hex={self.hex!r} image.url={self.image.url}>"

    @property
    def image(self) -> Image:
        """:class:`Image`: The image of the NFT."""
        url = self.__data["image"]
        return Image(url, self.__http._session)  # type: ignore

    @property
    def colour_name(self) -> Optional[str]:
        """Optional[:class:`str`]: The name of the NFT's colour.

        This is only available if the season was set to ``NFTSeason.RANDOM``. Use :meth:`.fetch_colour_name` to call the `colour` endpoint for the name.
        """
        return self.__data["name"]

    async def fetch_colour_name(self) -> str:
        """|coro|

        Fetches the name of the NFT's colour from the `colour` endpoint.

        Returns
        -------
        str
            The name of the NFT's colour.
        """
        if self.__data["name"] is not None:
            return self.__data["name"]

        data = await self.__http.colour(self.hex)
        return data["name"]

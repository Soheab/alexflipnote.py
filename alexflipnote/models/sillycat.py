from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Tuple

from .image import Image

if TYPE_CHECKING:
    from ..http import HTTPClient
    from .._types.sillycat import Sillycat as SillyCatData, SillycatPosition

__all__: Tuple[str, ...] = ("SillyCat", "SillyCatPosition")


class SillyCatPosition:
    """Represents a class holding the colours of a :class:`SillyCat`.

    Attributes
    ----------
    hex: :class:`str`
        The hex code of the colour.
    """

    __slots__: Tuple[str, ...] = ("__data", "__http", "hex")

    def __init__(self, data: SillycatPosition, http: HTTPClient) -> None:
        self.__data: SillycatPosition = data
        self.__http: HTTPClient = http
        self.hex: str = data["hex"]

    def __str__(self) -> str:
        return self.hex

    def __repr__(self) -> str:
        return f"<SillyCatPosition hex={self.hex!r}>"

    @property
    def colour_name(self) -> Optional[str]:
        """Optional[:class:`str`]: The name of the colour.

        This is only available if `random` was set to ``True``. Use :meth:`.fetch_colour_name` to call the `colour` endpoint for the name.
        """
        return self.__data["name"]

    async def fetch_colour_name(self) -> str:
        """|coro|

        Fetches the name of the colour from the `colour` endpoint.

        Returns
        -------
        str
            The name of the colour.
        """
        if self.__data["name"] is not None:
            return self.__data["name"]

        data = await self.__http.colour(self.hex)
        return data["name"]


class SillyCat:
    """Represents a silly cat image.

    Attributes
    ----------
    url: :class:`str`
        The unparsed URL of the image.
    left_hex: :class:`SillyCatPosition`
        The left colour of the silly cat.
    right_hex: :class:`SillyCatPosition`
        The right colour of the silly cat.
    """

    __slots__: Tuple[str, ...] = ("__data", "__http", "url", "left_hex", "right_hex")

    def __init__(self, original_url: str, data: SillyCatData, http: HTTPClient) -> None:
        self.__data: SillyCatData = data
        self.__http: HTTPClient = http
        self.url: str = original_url
        self.left_hex: SillyCatPosition = SillyCatPosition(data["left"], http)
        self.right_hex: SillyCatPosition = SillyCatPosition(data["right"], http)

    def __str__(self) -> str:
        return self.url

    def __repr__(self) -> str:
        return f"<SillyCat url={self.url!r} left_hex={self.left_hex.hex!r} right_hex={self.right_hex.hex!r}>"

    @property
    def image(self) -> Optional[Image]:
        """:class:`Image`: Returns an :class:`Image` object constructed from the unparsed URL of the image."""
        return Image(self.url, self.__http._session)  # type: ignore

    @property
    def simple_image(self) -> Optional[Image]:
        """Optional[:class:`Image`]: The simple image of the sillycat if available.

        This is a url with only the left hex colour.
        """
        url = self.__data.get("images", {}).get("simple")
        if not url:
            return None
        return Image(url, self.__http._session)  # type: ignore

    @property
    def complex_image(self) -> Optional[Image]:
        """Optional[:class:`Image`]: The complex image of the sillycat if available.

        This is a url with both left and right hex colours.
        """
        url = self.__data.get("images", {}).get("complex")
        if url:
            return None
        return Image(url, self.__http._session)  # type: ignore

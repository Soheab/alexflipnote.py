from __future__ import annotations
from typing import TYPE_CHECKING, Literal, Union, overload, Optional, Tuple

from io import BytesIO

if TYPE_CHECKING:
    from typing_extensions import Self
    from typing import Any, Protocol
    from io import BufferedIOBase
    from os import PathLike
    from aiohttp import ClientSession

    class FileLike(Protocol):
        def __call__(
            self,
            fp: Union[str, bytes, PathLike[Any], BufferedIOBase],
            filename: Optional[str] = None,
            **kwargs: Any,
        ) -> Self:
            ...


__all__: Tuple[str, ...] = ("Image",)


class Image:
    """Represents a class for all image endpoints.

    Attributes
    ----------
    url: :class:`str`
        The URL of the image.
    """

    __slots__: Tuple[str, ...] = ("_session", "url")

    def __init__(self, url: str, session: ClientSession) -> None:
        self.url = url
        self._session = session

    def __str__(self) -> str:
        return self.url

    def __repr__(self) -> str:
        return f"<Image url={self.url!r}>"

    @overload
    async def read(self, bytesio: Literal[True] = ...) -> BytesIO:
        ...

    @overload
    async def read(self, bytesio: Literal[False] = ...) -> bytes:
        ...

    async def read(self, bytesio: bool = True) -> Union[bytes, BytesIO]:
        """Returns the image data.

        Parameters
        ----------
        bytesio: :class:`bool`
            Whether to return the data as a :class:`io.BytesIO` object. Defaults to ``True``.

        Returns
        -------
        Union[:class:`bytes`, :class:`io.BytesIO`]
            The image data.
        """
        async with self._session.get(self.url) as response:
            if bytesio:
                return BytesIO(await response.read())
            else:
                return await response.read()

    async def file(self, cls: FileLike, filename: str = "image.png", **kwargs) -> FileLike:
        """Converts the image to a file-like object.

        Parameters
        ----------
        cls: Any
            The file-like object to convert the image to.
            E,g, `discord.File` (discord.py)
        filename: str
            The filename to use.

        Returns
        -------
        Any
            An instance of the file-like object.
        """
        return cls(await self.read(), filename=filename, **kwargs)

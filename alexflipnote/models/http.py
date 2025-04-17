from __future__ import annotations

from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:
    from .._types.http_endpoint import HTTP as HTTPData


__all__: Tuple[str, ...] = ("HTTPResult",)


class HTTPResult:
    """Represents an HTTP result.

    Attributes
    ----------
    code: :class:`int`
        The HTTP status code.
    name: :class:`str`
        The name of the HTTP status code.
    description: :class:`str`
        The description of the HTTP status code.
    """

    __slots__: Tuple[str, ...] = ("__data", "code", "name", "description")

    def __init__(self, data: HTTPData) -> None:
        self.__data: HTTPData = data
        self.code: int = data["code"]
        self.name: str = data["name"]
        self.description: str = data["description"]

    def __str__(self) -> str:
        return f"{self.name} ({self.code})"

    def __int__(self) -> int:
        return self.code

    def __repr__(self) -> str:
        return f"<HTTPResult code={self.code!r} name={self.name!r} description={self.description!r}>"

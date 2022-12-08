from __future__ import annotations
from typing import TYPE_CHECKING, Any, Literal, Optional, Tuple, Union, overload

import random

from .models import Colour, Image, NFT, SillyCat
from .errors import BadRequest
from .http import HTTPClient as _HTTPClient
from .enums import Endpoint, MinecraftIcon, NFTSeason, WithJsonEndpoint, MinecraftEndpoint

from . import utils as _utils

if TYPE_CHECKING:
    from aiohttp import ClientSession


__all__: Tuple[str, ...] = ("Client",)


class Client:
    """Represents a client for the AlexFlipnote API.

    Parameters
    ----------
    session: Optional[:class:`aiohtttp.ClientSession`]
        The session to use for the HTTPClient.
    """

    __slots__: Tuple[str, ...] = ("__http",)

    def __init__(
        self,
        *,
        session: Optional[ClientSession] = None,
    ) -> None:
        self.__http = _HTTPClient(self, session)

    def __str__(self) -> str:
        return f"<AlexFlipnote.py Client __str__>"

    def __repr__(self) -> str:
        return f"<AlexFlipnote.py Client __repr__>"

    # Animals / JSON

    async def birb(self) -> str:
        """Returns a random birb image.

        Returns
        -------
        str
            The URL of the image.
        """
        data = await self.__http.with_file(WithJsonEndpoint.BIRB)
        return data["file"]

    @_utils._alias_of(birb)
    async def bird(self) -> str:
        ...

    async def cats(self) -> str:
        """Returns a random cat image.

        Returns
        -------
        str
            The URL of the image.
        """
        data = await self.__http.with_file(WithJsonEndpoint.CATS)
        return data["file"]

    @_utils._alias_of(cats)
    async def cat(self) -> str:
        ...

    async def sadcat(self) -> str:
        """Returns a random sadcat image.

        Returns
        -------
        str
            The URL of the image.
        """
        data = await self.__http.with_file(WithJsonEndpoint.SADCAT)
        return data["file"]

    async def dogs(self) -> str:
        """Returns a random dog image.

        Returns
        -------
        str
            The URL of the image.
        """
        data = await self.__http.with_file(WithJsonEndpoint.DOGS)
        return data["file"]

    @_utils._alias_of(dogs)
    async def dog(self) -> str:
        ...

    async def coffee(self) -> str:
        """Returns a random coffee image.

        Returns
        -------
        str
            The URL of the image.
        """
        data = await self.__http.with_file(WithJsonEndpoint.COFFEE)
        return data["file"]

    # Colour

    async def colour(self, colour: Optional[Union[str, int]] = None) -> Colour:
        """Returns a :class:`.Colour` object.

        Parameters
        ----------
        colour: Optional[Union[:class:`str`, :class:`int`]]
            The colour to get information about.

        Returns
        -------
        :class:`.Colour`
            The colour object.
        """
        checked_colour = _utils._check_colour_value(colour)
        if not checked_colour:
            raise BadRequest("Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)")

        data = await self.__http.colour(checked_colour)
        return Colour(self.__http, data)

    @_utils._alias_of(colour)
    async def color(self, colour: Optional[Union[str, int]] = None) -> Colour:
        ...

    # Images

    # minecraft

    async def __gen_minecraft_image(
        self, endpoint: MinecraftEndpoint, text: str, icon: Union[str, int, MinecraftIcon] = MinecraftIcon.RANDOM
    ) -> Image:
        """Returns a minecraft image.

        Parameters
        ----------
        text: :class:`str`
            The text to display on the image.
        icon: Union[:class:`str`, :class:`int`, :class:`.MinecraftIcon]
            The icon to display on the image. Defaults to :attr:`.MinecraftIcon.RANDOM`.

        Returns
        -------
        :class:`.Image`
            The image object.
        """
        get_icon = _utils._try_enum(MinecraftIcon, icon)
        if get_icon is MinecraftIcon.RANDOM or not get_icon:
            icon = random.choice(list(MinecraftIcon))

        url = await self.__http.with_minecraft(endpoint, text, icon)  # type: ignore
        return Image(url, self.__http._session)  # type: ignore

    async def achievement(self, text: str, icon: Union[str, int, MinecraftIcon] = MinecraftIcon.RANDOM) -> Image:
        """Returns an achievement image.

        Parameters
        ----------
        text: :class:`str`
            The text to display on the image.
        icon: Union[:class:`str`, :class:`int`, :class:`.MinecraftIcon]
            The icon to display on the image. Defaults to :attr:`.MinecraftIcon.RANDOM`.

        Returns
        -------
        :class:`.Image`
            The image object.
        """
        return await self.__gen_minecraft_image(MinecraftEndpoint.ACHIEVEMENT, text, icon)

    async def challenge(self, text: str, icon: Union[str, int, MinecraftIcon] = MinecraftIcon.RANDOM) -> Image:
        """Returns an challenge image.

        Parameters
        ----------
        text: :class:`str`
            The text to display on the image.
        icon: Union[:class:`str`, :class:`int`, :class:`.MinecraftIcon]
            The icon to display on the image. Defaults to :attr:`.MinecraftIcon.RANDOM`.

        Returns
        -------
        :class:`.Image`
            The image object.
        """
        return await self.__gen_minecraft_image(MinecraftEndpoint.CHALLENGE, text, icon)

    async def calling(self, text: str) -> Image:
        """Returns a calling image.

        Parameters
        ----------
        text: :class:`str`
            The text to display on the image.

        Returns
        -------
        :class:`.Image`
            The image object.
        """
        url = await self.__http.with_image(Endpoint.CALLING, text=text)
        return Image(url, self.__http._session)  # type: ignore

    async def captcha(self, top: str, bottom: str) -> Image:
        """Returns a captcha image.

        Parameters
        ----------
        top: :class:`str`
            The text to display on the image.
        bottom: :class:`str`
            The text to display on the image.

        Returns
        -------
        :class:`.Image`
            The image object.
        """
        url = await self.__http.with_image(Endpoint.CAPTCHA, top=top, bottom=bottom)
        return Image(url, self.__http._session)  # type: ignore

    async def drake(self, top: str, bottom: str) -> Image:
        """Returns a drake meme image.

        Parameters
        ----------
        top: :class:`str`
            The text to display on the image.
        bottom: :class:`str`
            The text to display on the image.

        Returns
        -------
        :class:`.Image`
            The image object.
        """
        url = await self.__http.with_image(Endpoint.DRAKE, top=top, bottom=bottom)
        return Image(url, self.__http._session)  # type: ignore

    async def facts(self, text: str) -> Image:
        """Returns a facts image.

        Parameters
        ----------
        text: :class:`str`
            The text to display on the image.

        Returns
        -------
        :class:`.Image`
            The image object.
        """
        url = await self.__http.with_image(Endpoint.FACTS, text=text)
        return Image(url, self.__http._session)  # type: ignore

    async def pornhub(self, text: str, text2: str) -> Image:
        """Returns a pornhub image.

        Parameters
        ----------
        text: :class:`str`
            The text to display on the image.

        Returns
        -------
        :class:`.Image`
            The image object.
        """
        url = await self.__http.with_image(Endpoint.PORNHUB, text=text, text2=text2)
        return Image(url, self.__http._session)  # type: ignore

    @_utils._alias_of(pornhub)
    async def ph(self, text: str, text2: str) -> Image:
        ...

    async def scroll(self, text: str) -> Image:
        """Returns a scroll message.

        Parameters
        ----------
        text: :class:`str`
            The text to display on the image.

        Returns
        -------
        :class:`str`
            The message.
        """
        url = await self.__http.with_image(Endpoint.SCROLL, text=text)
        return Image(url, self.__http._session)  # type: ignore

    async def did_you_mean(self, top: str, bottom: str) -> Image:
        """Returns a did you mean message.

        Parameters
        ----------
        top: :class:`str`
            The text to display on the image.
        bottom: :class:`str`
            The text to display on the image.

        Returns
        -------
        :class:`str`
            The message.
        """
        url = await self.__http.with_image(Endpoint.DID_YOU_MEAN, top=top, bottom=bottom)

        return Image(url, self.__http._session)  # type: ignore

    @_utils._alias_of(did_you_mean)
    async def didyoumean(self, top: str, bottom: str) -> Image:
        ...

    # Sillycat and NFT

    async def nft(
        self,
        hex: Optional[str] = None,
        season: NFTSeason = NFTSeason.RANDOM,
        *,
        seed: Optional[Any] = None,
        return_image: bool = False,
    ) -> NFT:
        """Generates an NFT of the Xela discord Bot.

        Parameters
        ----------
        hex: :class:`str`
            The hex code of the colour to use. This is required if ``season`` is not :attr:`.NFTSeason.RANDOM`.
        season: :class:`.NFTSeason`
            The season to use. Defaults to :attr:`.NFTSeason.RANDOM`.
        seed: Optional[:class:`Any`]
            The unique seed to use. Defaults to ``None``. With this you can get the same NFT every time.
        return_image: :class:`bool`
            Whether to return an :class:`.Image` object instead of an :class:`.NFT` object.
            `season` cannot be :attr:`.NFTSeason.RANDOM` if this is ``True``.
            Defaults to ``False``.

        Returns
        -------
        :class:`.NFT`
            An object representing the NFT.
        """
        if hex is not None and season is NFTSeason.RANDOM:
            season = NFTSeason.NONE

        if return_image and season is NFTSeason.RANDOM:
            raise ValueError("Cannot return an image if season is random.")

        if hex:
            checked_colour = _utils._check_colour_value(hex)
            if not checked_colour:
                raise BadRequest("Invalid hex value. You're only allowed to enter HEX (0-9 & A-F)")

        data = await self.__http.handle_nft(hex, season, seed)  # type: ignore
        if return_image:
            return Image(data, self.__http._session)  # type: ignore

        if season is NFTSeason.RANDOM:
            return NFT(data, self.__http)

        payload = {"hex": hex, "season": season.value, "name": None, "image": data}
        return NFT(
            payload,  # type: ignore
            self.__http,
        )

    async def sillycat(
        self,
        left_hex: Optional[str] = None,
        right_hex: Optional[str] = None,
        *,
        random: bool = True,
        seed: Optional[Any] = None,
        return_image: bool = False,
    ) -> SillyCat:
        """Generates a SillyCat image

        Parameters
        ----------
        left_hex: :class:`str`
            The hex code of the colour to use on the left side. This is required if ``random`` is ``False``.
        right_hex: :class:`str`
            The hex code of the colour to use on the right side. This is required if ``random`` is ``False``.
        random: bool
            Whether to use random colours or not. Defaults to ``True`` if both ``left_hex`` and ``right_hex`` are ``None``.
        seed: Optional[:class:`Any`]
            The unique seed to use. Defaults to ``None``. With this you can get the same sillycat every time.
        return_image: bool
            Whether to return an :class:`.Image` object only or the full :class:`.SillyCat` object.
            either ``left_hex`` or ``right_hex`` must not be ``None`` if this is ``True``.
            Defaults to ``False``.

        Returns
        -------
        :class:`.SillyCat`
            An object representing the image.
        """
        if return_image and not (left_hex or right_hex):
            raise BadRequest("You need to provide at least one hex value to return an image.")

        if left_hex or right_hex:
            random = False

        if not random and not (left_hex or right_hex):
            raise BadRequest("You need to enter at least one hex value or set random to True.")

        if right_hex and not left_hex:
            raise BadRequest("You need to enter a left hex value first.")

        if left_hex:
            checked_colour = _utils._check_colour_value(left_hex)
            if not checked_colour:
                raise BadRequest("Invalid left_hex value. You're only allowed to enter HEX (0-9 & A-F)")

        if right_hex:
            checked_colour = _utils._check_colour_value(right_hex)
            if not checked_colour:
                raise BadRequest("Invalid right_hex value. You're only allowed to enter HEX (0-9 & A-F)")

        if random and not (left_hex or right_hex):
            left_hex = None
            right_hex = None

        data = await self.__http.handle_sillycat(left_hex, right_hex, seed)  # type: ignore

        if return_image:
            return Image(data, self.__http._session)  # type: ignore

        if random is True:
            url = data["images"]["complex"]
            return SillyCat(url, data, self.__http)

        parsed_url = tuple(data.split("sillycat"))  # type: ignore
        url, hexes = parsed_url
        parsed_hexes = tuple(hexes.split("/"))
        left_hex, right_hex, url = None, None, None
        if len(parsed_hexes) == 2:
            left_hex = parsed_hexes[1]
            url = f"{url}sillycat/{left_hex}"
        elif len(parsed_hexes) == 3:
            left_hex = parsed_hexes[1]
            right_hex = parsed_hexes[2]

        simple, complex = None, None
        if left_hex:
            simple = f"{url}sillycat/{left_hex}"
        if left_hex and right_hex:
            complex = f"{url}sillycat/{left_hex}/{right_hex}"

        payload = {
            "left": {
                "hex": f"#{left_hex}",
                "name": None,
            },
            "right": {
                "hex": f"#{right_hex}",
                "name": None,
            },
            "images": {
                "simple": simple,
                "complex": complex,
            },
        }
        return SillyCat(data, payload, self.__http)  # type: ignore

    # Other

    @overload
    async def support_server(self, *, creator: Literal[False] = ...) -> str:
        ...

    @overload
    async def support_server(self, *, creator: Literal[True] = ...) -> Tuple[str, str]:
        ...

    async def support_server(self, *, creator: bool = False) -> Union[str, Tuple[str, str]]:
        """Returns an invite to the API's support server.

        Parameters
        ----------
        creator: Optional[:class:`bool`]
            Whether to also return the wrapper creator's support server invite.

        Returns
        -------
        Union[:class:`str`, :class:`Tuple[:class:`str`, :class:`str`]`]
            The invites.
        """
        data = await self.__http.support_server()
        discord_server = data["support_server"]
        if creator is True:
            return discord_server, "https://discord.gg/yCzcfju"

        return discord_server

    # Session

    async def close(self) -> None:
        """Closes the session."""
        await self.__http.close()

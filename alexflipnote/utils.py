from __future__ import annotations
from typing import Any, Callable, Optional, TYPE_CHECKING, TypeVar, Union, Match, Type

import functools
import random
import re

if TYPE_CHECKING:
    from enum import Enum

    from typing_extensions import ParamSpec


if TYPE_CHECKING:
    P = ParamSpec("P")
else:
    P = TypeVar("P")

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound="Enum")


def _gen_colour(numbers: Optional[int] = None) -> str:
    random_number = numbers or random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    return hex_number[2:]


def _check_colour_value(hex_input: Optional[Union[str, int]]) -> Optional[str]:
    if not hex_input or isinstance(hex_input, int):
        hex_input = _gen_colour(int(hex_input) if hex_input else None)

    match: Optional[Match[str]] = re.search(r"^#?(?:[0-9a-fA-F]{3}){1,2}$", str(hex_input))
    if not match:
        return None

    return match.string.strip("#")


def _try_enum(enum_class: Type[EnumT], value: Union[EnumT, str, int]) -> Optional[EnumT]:
    try:
        if isinstance(value, str):
            val = enum_class[str(value.upper())]
        elif isinstance(value, int):
            val = enum_class(int(value))
        else:
            val = value

        return val
    except (KeyError, ValueError):
        return None


def _alias_of(alias_to: Callable[P, T]) -> Callable[[Callable[P, T]], Callable[P, T]]:
    @functools.wraps(alias_to)
    def inner(func: Callable[..., Any]) -> Callable[P, T]:
        if getattr(func, "__is_alias__", False):
            raise TypeError("Cannot alias an alias")
        else:
            func.__is_alias__ = True

        func.__alias_of__ = alias_to
        try:
            alias_to.__aliases__.append(func)
        except AttributeError:
            alias_to.__aliases__ = [func]

        return alias_to

    return inner

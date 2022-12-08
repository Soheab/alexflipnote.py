from typing import Any, Dict, Literal, List, TypedDict


ImageTypes = Literal["cats", "dogs", "sadcat", "birb", "coffee"]


class Wrapper(TypedDict):
    author: str
    url: str


class Image(TypedDict):
    file: str


class BaseDocs(TypedDict):
    _docs: List[str]
    _variables: Dict[str, Any]


class Raw(TypedDict):
    support_server: str
    endpoints: List[str]
    wrappers: Dict[str, Dict[str, Wrapper]]

# Models // NFT

## NFT
Represents a NFT image.

### Attributes
- colour_name [str] - This is only available if the season was set to [NFTSeason]``.RANDOM``. Use [fetch_colour_name](nft.md#await-fetch_colour_name---str) to call the ``colour`` endpoint for the name.
- hex [str] - The colour of the NFT.
- image [Image](image.md#image) - The image of the NFT.
- seeason [NFTSeason] - The season of the NFT.

### Methods
---

### await fetch_colour_name() -> [str]
Fetches the name of the NFT's colour from the ``colour`` endpoint.


[str]: https://docs.python.org/3/library/stdtypes.html#str
[int]: https://docs.python.org/3/library/functions.html#int
[dict]: https://docs.python.org/3/library/functions.html#func-dict
[list]: https://docs.python.org/3/library/functions.html#func-list
[bool]: https://docs.python.org/3/library/functions.html#bool
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
[Optional]: https://docs.python.org/3/library/typing.html#typing.Optional
[Union]: https://docs.python.org/3/library/typing.html#typing.Union
[NFTSeason]: enums.md#nftseason
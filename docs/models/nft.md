# NFT

Represents an NFT image.

## Attributes
- **colour_name** ([`str`][str]):
    The name of the NFT's colour. Available only if the season is [`NFTSeason.RANDOM`][NFTSeason]. To retrieve this value, use the [`fetch_colour_name`](#await-fetch_colour_name---str) method.
- **hex** ([`str`][str]):
    The hexadecimal representation of the NFT's colour.
- **image** ([`Image`][Image]):
    The image object associated with the NFT.
- **season** ([`NFTSeason`][NFTSeason]):
    The season associated with the NFT.

## Methods

- ### `await fetch_colour_name()`
    Fetches the name of the NFT's colour from the API.

    #### Returns

    - [`str`][str]: The name of the colour.


[str]: https://docs.python.org/3/library/stdtypes.html#str  
[NFTSeason]: enums.md#nftseason  
[Image]: image.md#image
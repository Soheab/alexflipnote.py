# Minecraft

- ### `await achievement(text: str, icon: str | int | MinecraftIcon = MinecraftIcon.RANDOM)`
    Generates a Minecraft achievement image.
    #### Parameters
    - **text** ([`str`][str]): The text to display on the achievement image.
    - **icon** ([`Optional`][Optional][[`str`][str] | [`int`][int] | [`MinecraftIcon`][int]]): The icon to display. Defaults to [`MinecraftIcon.RANDOM`][MinecraftIcon].
    #### Returns
    [`Image`][Image]: The generated achievement image.


- ### `await challenge(text: str, icon: str | int | MinecraftIcon = MinecraftIcon.RANDOM)`
    Generates a Minecraft challenge image.
    #### Parameters
    - **text** ([`str`][str]): The text to display on the challenge image.
    - **icon** ([`Optional`][Optional][[`str`][str] | [`int`][int] | [`MinecraftIcon`][int]]): The icon to display. Defaults to [`MinecraftIcon.RANDOM`][MinecraftIcon].
    #### Returns
    [`Image`][Image]: The generated challenge image.


# Animals

- ### `await alex_api.birb()`
    Returns a random birb image.  
    **Aliases:** `bird`
    
    #### Returns
    [`str`][str] : The URL of the random birb image.

- ### `await alex_api.cats()`
    Returns a random cat image.  
    **Aliases:** `cat`

    #### Returns
    [`str`][str] : The URL of the random cat image.

- ### `await alex_api.dogs()`
    Returns a random dog image.  
    **Aliases:** `dog`

    #### Returns
    [`str`][str] : The URL of the random dog image.

- ### `await alex_api.sadcat()`
    Returns a random sad cat image.

    #### Returns
    [`str`][str] : The URL of a random sad cat image.

# Images

- ### `await alex_api.calling(text: str) -> Image`
    Generates a "calling" meme image.

    #### Parameters
    - **text** ([`str`][str]): The text to display on the image.

    #### Returns
    [`Image`][Image]: The generated image.

- ### `await alex_api.captcha(top: str, bottom: str)`
    Generates a captcha-style image.

    #### Parameters
    - **top** ([`str`][str]): The top text.
    - **bottom** ([`str`][str]): The bottom text.
  
    #### Returns
    [`Image`][Image]: The generated image.

- ### `await alex_api.coffee()`

    Returns a random coffee image.
    
    #### Returns
    [`str`][str]: The URL of the random coffee image.

- ### `await alex_api.did_you_mean(top: str, bottom: str)`
    Generates a "Did you mean?" meme image.  
    **Aliases:** `didyoumean`

    #### Parameters

    - **top** ([`str`][str]): The suggested text.
    - **bottom** ([`str`][str]): The mistaken text.

    #### Returns
    [`Image`][Image]: The generated image.


- ### `await alex_api.drake(top: str, bottom: str)`
    Generates a Drake meme image.

    #### Parameters

    - **top** ([`str`][str]): The top text.
    - **bottom** ([`str`][str]): The bottom text.

    #### Returns
    [`Image`][Image]: The generated Drake meme image.

- ### `await alex_api.facts(text: str)`
    Generates a "facts" meme image.

    #### Parameters

    - **text** ([`str`][str]): The fact to display.

    #### Returns
    [`Image`][Image]: The generated image.

- ### `await alex_api.http_code(code: int)`
    Returns information and an image for the given HTTP status code.

    #### Parameters

    - **code** ([`int`][int]): The HTTP status code.

    #### Returns
    [`HTTPResult`][HTTPResult]: The result object containing the code, name, and description.


- ### `await alex_api.nft(hex: Optional[str] = None, season: NFTSeason = NFTSeason.RANDOM, *, seed: Optional[Any] = None, return_image: bool = False) -> NFT`
    Generates an NFT image of the Xela Discord bot.

    #### Parameters

    - **hex** ([`Optional`][Optional][[`str`][str]]): The hex color code. Required if `season` is not [`NFTSeason.RANDOM`][NFTSeason].
    - **season** ([`Optional`][Optional][`NFTSeason`][NFTSeason]]): The NFT season. Defaults to [`NFTSeason.RANDOM`][NFTSeason].
    - **seed** ([`Optional`][Optional][`Any`]): Unique seed for deterministic output.
    - **return_image** ([`Optional`][Optional][[`bool`][bool]]): If `True`, returns an [Image] object instead of an [NFT] object.  
        Note: `season` cannot be [`NFTSeason.RANDOM`][NFTSeason] if this is `True`. Defaults to `False`.

    #### Returns
    - If `return_image` is `True`: [`Image`][Image]: The generated image.
    - Otherwise: [`NFT`][NFT]: The generated NFT object containing the image and color information.

- ### `await alex_api.pornhub(text: str)`
    Generates a Pornhub-style meme image.  
    **Aliases:** `ph`

    #### Parameters

    - **text** ([`str`][str]): The text to display.

    #### Returns
    [`Image`][Image]: The generated image.

- ### `await alex_api.scroll(text: str)`
    Generates a scroll message image.

    #### Parameters
    - **text** ([`str`][str]): The text to display.

    #### Returns
    [`Image`][Image]: The generated image.

- ### `await alex_api.supreme(text: str)`
    Generates a Supreme-style meme image.

    #### Parameters

    - **text** ([`str`][str]): The text to display.

    #### Returns
    [`Image`][Image]: The generated image.

- ### `await alex_api.sillycat(left_hex: Optional[str] = None, right_hex: Optional[str] = None, *, random: bool = True, seed: Optional[Any] = None, return_image: bool = False)`

    Generates a SillyCat image.

    #### Parameters

    - **left_hex** ([`Optional`][Optional][[`str`][str]]: Hex color for the left side. Required if `random` is `False`.
    - **right_hex** ([`Optional`][Optional][[`str`][str]]): Hex color for the right side. Required if `random` is `False`.
    - **random** ([`Optional`][Optional][[`bool`][bool]]: Use random colors. Defaults to `True` if both hex values are `None`.
    - **seed** ([`Optional`][Optional][`Any`]): Unique seed for deterministic output.
    - **return_image** ([`Optional`][Optional][[`bool`][bool]]): If `True`, returns an [Image] object only.  
        Note: Either `left_hex` or `right_hex` must not be `None` if this is `True`. Defaults to `False`.

    #### Returns
    [`SillyCat`][SillyCat]: The generated SillyCat object containing the image and color information.
    If `return_image` is `True`, returns an [Image] object instead.

# Colour

- ### `await alex_api.colour(colour: Optional[str] = None)`
    Returns a [Colour] object for the given color.  
    **Aliases:** `color`

    #### Parameters
    - **colour** ([`Optional`][Optional][[`str`][str]]): The color to get information about.
  
    #### Returns
    [`Colour`][Colour]: The [Colour] object containing information about the color.

# Misc

- ### `await alex_api.close()`
    Closes the API session.

- ### `await alex_api.support_server(*, creator: bool = False)`
    Returns an invite link to the API's support server.

    #### Parameters
    - **creator** ([`Optional`][Optional][[`bool`][bool]]): If `True`, also returns the wrapper creator's support server invite.
    
    #### Returns
    if `creator` is `True`: [`tuple`][tuple]: A tuple containing the API support server invite and the wrapper creator's support server invite. \
    else: [`str`][str]: The API support server invite. 

<!-- Reference Links -->
[str]: https://docs.python.org/3/library/stdtypes.html#str
[int]: https://docs.python.org/3/library/functions.html#int
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
[bool]: https://docs.python.org/3/library/functions.html#bool
[Optional]: https://docs.python.org/3/library/typing.html#typing.Optional
[Image]: models/image.md
[NFT]: models/nft.md
[Colour]: models/colour.md
[NFTSeason]: enums.md#nftseason
[MinecraftIcon]: enums.md#minecrafticon
[SillyCat]: models/sillycat.md
[HTTPResult]: models/httpresult.md

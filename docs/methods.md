# AlexFlipnote.py Docs | Methods

## Minecraft
---

### await alex_api.achievement(text: [str], icon: [Union]\[[str], [int], [MinecraftIcon]] = [MinecraftIcon]``.RANDOM``) -> [Image]
Returns an achievement image.

#### Parameters
- text ([str]) - The text to display on the image.
- icon ([Union]\[[str], [int], [MinecraftIcon]]) - The icon to display on the image. Defaults to [MinecraftIcon]``.RANDOM``.

---

### await alex_api.challenge(text: [str], icon: [Union]\[[str], [int], [MinecraftIcon]] = [MinecraftIcon]``.RANDOM``) -> [Image]
Returns an challenge image.


#### Parameters
- text ([str]) - The text to display on the image.
- icon ([Union]\[[str], [int], [MinecraftIcon]]) - The icon to display on the image. Defaults to [MinecraftIcon]``.RANDOM``.


## Animals
---

### await alex_api.birb() -> [str]
Returns a random birb image.
**Aliases:** bird

---

### await alex_api.cats() -> [str]
Returns a random cat image. \
**Aliases:** cat

---

### await alex_api.dogs() -> [str]
Returns a random dog image. \
**Aliases:** dog

---

### await alex_api.sadcat() -> [str]
Returns a random sadcat image.

---

## Images
---

### await alex_api.calling(text: [str]) -> [Image]
Returns a calling image.

#### Parameters
- text ([str]) - The text to display on the image. 

---

### await alex_api.captcha(top: [str], bottom: [str]) -> [Image]
Returns a captcha image.

#### Parameters
- top ([str]) - The text to display on the image.
- bottom ([str]) - The text to display on the image.

---

### await alex_api.coffee() -> [str]
Returns a random coffee image.

---

### await alex_api.did_you_mean(top: [str], bottom: [str]) -> [Image]
Returns a did you mean message. \
**Aliases:** didyoumean

#### Parameters
- top ([str]) - The text to display on the image.
- bottom ([str]) - The text to display on the image.

---

### await alex_api.drake(top: [str], bottom: [str]) -> [Image]
Returns a drake meme image.

#### Parameters
- top ([str]) - The text to display on the image.
- bottom ([str]) - The text to display on the image.

---


### await alex_api.facts(text: [str]) -> [Image]
Returns a facts image.

#### Parameters
- text ([str]) - The text to display on the image.

---

### await alex_api.http_code(code: [int]) -> [HTTPResult]
Returns the HTTP result for the given status code.

#### Parameters
- code ([int]) - The HTTP code to get information about.

---

### await alex_api.nft(hex: [Optional]\[[str]] = None, season: [NFTSeason] = [NFTSeason]``.RANDOM``, *, seed: [Optional]\[[Any]] = None, return_image: [bool] = ``False``) -> [NFT]
Generates an NFT of the Xela discord bot.

#### Parameters
- hex ([Optional]\[[str]]) - The hex code of the colour to use. This is required if ``season`` is not :attr:`.NFTSeason.RANDOM`.
- season ([NFTSeason]) - The season to use. Defaults to [NFTSeason]``.RANDOM``
- seed ([Optional][[Any]]) - The unique seed to use. Defaults to ``None``. With this you can get the same NFT every time.
- return_image ([bool]) - Whether to return an [image] object instead of an :class:`.NFT` object.
    `season` cannot be [NFTSeason]``.RANDOM`` if this is ``True``.
    Defaults to ``False``.

---

### await alex_api.pornhub(text: [str]) -> [Image]
Returns a pornhub image. \
**Aliases:** ph

#### Parameters
- text ([str]) - The text to display on the image.

---

### await alex_api.scroll(text: [str]) -> [Image]
Returns a scroll message.

#### Parameters
- text ([str]) - The text to display on the image.

---

### await alex_api.supreme(text: [str]) -> [Image]
Returns a supreme message.

#### Parameters
- text ([str]) - The text to display on the image.

---

### await alex_api.sillycat(left_hex: [Optional]\[[str]] = ``None``, right_hex: [Optional]\[[str]] = ``None``, *, random: [bool] = ``True``, seed: [Optional]\[[Any]] = None, return_image: [bool] = ``False``) -> [SillyCat]
Generates a SillyCat image

#### Parameters
- left_hex ([Optional]\[[str]]) - The hex code of the colour to use on the left side. This is required if ``random`` is ``False``.
- right_hex ([Optional]\[[str]]) - The hex code of the colour to use on the right side. This is required if ``random`` is ``False``.
- random ([bool]) - Whether to use random colours or not. Defaults to ``True`` if both ``left_hex`` and ``right_hex`` are ``None``.
- seed ([Optional][[Any]]) - The unique seed to use. Defaults to ``None``. With this you can get the same sillycat every time.
- return_image ([bool]) - Whether to return an [image] object only or the full [SillyCat] object.
    either ``left_hex`` or ``right_hex`` must not be ``None`` if this is ``True``.
    Defaults to ``False``.

---

## Colour
---

### await alex_api.colour(colour: [Optional]\[[str]] = ``None``) -> [Colour]

Returns a [Colour] object.\
**Aliases:** color

#### Parameters
- colour ([Optional]\[[str]]) - The colour to get information about.

## Misc
---

### await alex_api.close() -> ``None``:
Closes the session.

---

### await alex_api.support_server(*, creator: [bool] = ``False``) -> [Union]\[[str], [Tuple][tuple][[str], [str]]]:
Returns an invite to the API's support server.

#### Parameters
- creator ([bool]) - Whether to also return the wrapper creator's support server invite.


[str]: https://docs.python.org/3/library/stdtypes.html#str
[int]: https://docs.python.org/3/library/functions.html#int
[dict]: https://docs.python.org/3/library/functions.html#func-dict
[list]: https://docs.python.org/3/library/functions.html#func-list
[bool]: https://docs.python.org/3/library/functions.html#bool
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
[Optional]: https://docs.python.org/3/library/typing.html#typing.Optional
[Any]: https://docs.python.org/3/library/typing.html#typing.Any
[Union]: https://docs.python.org/3/library/typing.html#typing.Union
[Image]: models/image.md
[NFT]: models/nft.md
[SillyCat]: models/sillycat.md
[Colour]: models/colour.md
[NFTSeason]: enums.md#nftseason
[MinecraftIcon]: enums.md#minecrafticon
[HTTPResult]: models/httpresult.md
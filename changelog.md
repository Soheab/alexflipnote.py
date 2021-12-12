## AlexFlipnote.py | Changelog

See here what changed or broke each version.

---
### v3.0.0 - December 12, 2021

- Python version bumped to >=3.8
- Addeed typings.
- Removed token argument.
- Removed `loop` kwarg from `Client()` constructor.	
- Removed following methods: `achievement, amiajoke, bad, calling, captcha, challenge, colour_image, colour_image_gradient, colourify, did_you_mean, drake, facts, filter, floor, fml, joke_overhead, pornhub, salty, shame, scroll, ship, supreme, trash, what`.
- Removed the following classes: `Image, MinecraftIcons, Filters, MissingTokens`
- Added the following classes: `RGB`
- `Colour.image_gradient` renamed to `Colour.gradient`.
- `Colour.blackorwhite_text` renamed to `Colour.black_or_white_text`.
- `Colour.shade` renamed to `Colour.shades`.
- `Colour.tint` renamed to `Colour.tints`.
- `Colour.rgb` now returns a `RGB` object.
- `Colour.rgb_values` renamed to `Colour.rgb`.
- Added `Colour.rgb_string` this returns a string in the format `rgb(r, g, b)` which was previously returned by `Colour.rgb`.
- Rewritten `HTTPSession` to `HTTPClient`.
- Rewritten the docs.

### v2.4.0 - May 4, 2021

- Added new method: [`.coffee()`](docs.md#await-alex_apicoffee) . Makes a request to https://coffee.alexflipnote.dev
  which then returns a random coffee image URL.
- Token is no longer required due to the following method not requiring a token anymore:
  `colour, colour_image, colour_image_gradient, birb, dogs, sadcat, cats, coffee`.
- New Exception added: `MissingToken`, this is raised when a method that is not listed above is used with a token being
  present in the constructor.
- Removed `.github_colours()` since the endpoint it used is gone.
- `.colour()` `.colour_image()` and `.colour_image_gradient()` now accepts a "python like hex". E.g, 0x9a6b48. Also, it
  can take a # now.


- Suggestions are as always welcome, you can ping me in the [AlexFlipnote server](https://discord.gg/DpxkY3x),
  #general_developers channel.

### v2.3.0 - February 12, 2021

- Added support for new [Filter](docs.md#await-alex_apifiltername-image): **mirror**
- Added [colourify](docs.md#await-alex_apicolourifyimage-colour--none-background--none) to the docs. For some reason
  this wasn't there since the beginning.
- Rewritten the docs to be easier to read and understand. [Go To Docs](docs.md)

### v2.2.0 - February 10, 2021

- Added support for new [Filter](docs.md#await-alex_apifiltername-image): **flip**

### v2.1.1 - January 9, 2021

- Fixed hyperlinks to docs and others for PyPi's description.

### v2.1.0 - January 3, 2021

- Added support for a new endpoint: `.shame()` [See more in docs](docs.md#await-alex_apishameimage)

### v2.0.2 - November 24, 2020

- Push better README to PyPi
- Fixes `.pornhub()` having the same value for text2.

### v2.0.1 - November 23, 2020

- Fixed `.drake()` returning a weird image.

### v2.0.0 - November 23, 2020

This introduced the required token in the constructor to be up to date with the api.

### v1.7.0 - November 1, 2020

- Added support for a new endpoint: `.what()` [See more in docs](docs.md#await-alex_apiwhatimage)
- Now using urllib.parse to parse text.
- Added `bytesio=True` to `Image.read()` set it to False if you want the bytes returned instead of an io.BytesIO object.
- Removed `.steam()`.
- Added alias for `.colourify()` -> `colorify`
- Added alias for `.colour_image_gradient()` -> `color_image_gradient`
- Added [Filters enum](docs.md#filters) for `.filter()`
- Changed Icon enum for `.achievement()` and `.challenge()` to [MinecraftIcons](docs.md#minecrafticons) with better
  docs.
- Added an optional `loop` param to `alexflipnote.Client()`

### v1.6.0 - September 6, 2020

- Removed `.steam()`. Reason: ratelimited too much - AlexFlipnote
- All errors now have text, finally json errors!
- Added "User-Agent"
- Added `__author__` & `__license__` next to `__version__`
- Better README.md
- Added examples to docs.md and fixed typo
- Added dates to changelog.md

### v1.5.4 - August 18, 2020

- Added missing `.lower()` for `.filter()`

### v1.5.3 - August 12, 2020

- docs.md and README.md improvements. New version to update it on PyPi.

### v1.5.2 - August 8, 2020

- Added an optional `session` param to `alexflipnote.Client()`.
- Renamed `_session` to `session`

### v1.5.1 - August 4, 2020

- Now these: `"`, `'`, `(`, `)`, `+`, `,`, `-`, `.`, `/` also get replaced for methods that require text.

### v1.5.0 - August 4, 2020

- Added support for the new `sepia` filter.
- `snow` filter is more appealing (according to AlexFlipnote)
- Added `random` choice for `.filter()`.
- Added new Exception `InternalServerError` to handle.. internal server errors.
- Exceptions don't return any message anymore since it's impossible to get, for now.

### v1.4.0 - August 1, 2020

- Added support for the new `wide` filter.

### v1.3.1 - July 26, 2020

- Fixed `alexflipnote.Image.read()` raising a TypeError instead of returning BytesIO.

### v1.3.0 - July 13, 2020

A complete rewrite which also removed the required package "url_regex".

- New icon for `.achievement()` and `.challenge()` "Oak log" at number 45,
- Added new support_server method to get an invitation to the AlexFlipnote's server,
- Added changelog and docs look a little better,
- Removed unnecessary things to make code smaller,
- Added type annotations & typehints for autocomplete things..?, better error handeling.
- Passing an Icon object to achievement and challenge now actually works.

I hope its faster and easier to use than ever with no breaking changes (hopefully)

### v1.2.6 - July 1, 2020

- Fixed `.trash()` having the wrong url format.

### v1.2.5 - June 30, 2020

- Fixed `.colourify()` not checking properly if color and background were `None`

### v1.2.4 - June 21, 2020

- Link to docs.md fix on PyPi

### v1.2.3 - June 20, 2020

- Added missing f-strings for `.amiajoke()`, `.bad()` and `.colour_image()`

### v1.2.2 - June 20, 2020

- Added back `Steam.SteamProfile.vacbanned`

### v1.2.1 - June 19, 2020

- Enum for `.achievement()` & `.challenge()`
- Removed `.Steam.SteamProfile.vacbanned`

### v1.2 - June 17, 2020

This was almost a rewrite.

- Remove `return_bytes`
- Most methods now return a `alexlfipnote.Image` object.
- Added docs.md

### v1.0.1.2 - June 15, 2020

- Added `.Colour.rgb_values` to get r/g/b values separate for Color

### v1.0.1.1 - June 15, 2020

- c and b parameters of `.color()` change to colour and background

### v1.0.1 - June 15, 2020

- `.steam()` and `.filter()` now raise `alexflipnote.NotFound` when user or filter isn't found

### v1.0.0 - June 15, 2020

Let's not talk about this one

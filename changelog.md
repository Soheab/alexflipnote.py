## AlexFlipnote.py | Changelog
See here what changed or broke each version.

---

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

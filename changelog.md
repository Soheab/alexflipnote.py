# AlexFlipnote.py | Changelog
See here what changed or broke each version.

## v1.5.3
- docs.md and README.md improvements. New version to update it on PyPi.

## v1.5.2
- Added an optional `session` param to `alexflipnote.Client()`.
- Renamed `_session` to `session`

## v1.5.1
- Now these: `"`, `'`, `(`, `)`, `+`, `,`, `-`, `.`, `/` also get replaced for methods that require text.

## 1.5.0
- Added support for the new `sepia` filter.
- `snow` filter is more appealing (according to AlexFlipnote)
- Added `random` choice for `.filter()`.
- Added new Exception `InternalServerError` to handle.. internal server errors.
- Exceptions don't return any message anymore since it's impossible to get, for now.

## 1.4.0
- Added support for the new `wide` filter.

## 1.3.1
This one fixed `alexflipnote.Image.read()` raising a TypeError instead of returning BytesIO.
 
## 1.3.0
A complete rewrite which also removed the required package "url_regex". 

New icon for `.achievement()` and `.challenge()` "Oak log" at number 45,
Added new support_server method to get an invitation to the AlexFlipnote's server,
Added changelog and docs look a little better,
Removed unnecessary things to make code smaller, 
Added type annotations & typehints for autocomplete things..?, better error handeling.

oh, and passing an Icon object to achievement and challenge now actually works.

I hope its faster and easier to use than ever with no breaking changes (hopefully)

## 1.2.6
This one fixed `.trash()` having the wrong url format.

## 1.2.5
This fixed `.colourify()` not checking properly if color and background were `None`

## 1.2.4
This fixed the link to docs from the long description on pypi.

## 1.2.3
Some missing f-strings were added for `.amiajoke()`, `.bad()` and `.colour_image()` oops.

## v1.2.2
`Steam.SteamProfile.vacbanned` was added back.

## v1.2.1
In here `alexflipnote.Icon` enum was added for the icons for `.achievement()` & `.challenge()`
to easily give an icon. Oh, and `.Steam.SteamProfile.vacbanned` was accidentally 
removed in this version.

## v1.2 
This was almost a rewrite. `return_bytes` which was added in 1.0.0 is removed so 
almost everything now returns a `alexflipnote.Image` object now. 

And docs were added in this one.

## v1.0.1.2
In this version `.Colour.rgb_values` was introduced to get r/g/b values separate for Color.
 
## v1.0.1.1
c and b parameters of `.color()` change to colour and background.

## v1.0.1
`.steam()` and `.filter()` now raise `alexflipnote.NotFound` when user or filter isn't found.

## v1.0.0
Let's not talk about this one.

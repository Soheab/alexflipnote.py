# Models // Colour (Or Color)

## Colour
Represents a colour from the API.

### Attributes
- cmyk ([CMYK](colour.md#cmyk)) - Returns a class holding the CMYK values of the colour.
- gradient ([Image](image.md#Image)) - Returns a image with all possible gradients of the colour. This is an alias to [ColourImages](colour.md#colourimages)``.gradient``
- hex ([Hex](colour.md#hex)) - Returns a class holding the hex value of the colour.
- hsl ([HSL](colour.md#hsl)) - Returns a class holding the HSL values of the colour.
- image ([str]) - The image of the colour. This is an alias to [ColourImages](colour.md#colourimages)``.square``.
- images ([ColourImages](colour.md#colourimages)) - Returns a class holding the different images of the colour. There are attributes on this class that can be used to get each image: ``.square`` and ``.gradient``.
- int ([int]) - The integer value of the colour.
- name ([str]) - The name of the colour.
- rgb [RGB](colour.md#rgb) - Returns a class holding the RGB values of the colour.
- safe_text_colour ([SafeTextColour](colour.md#safetextcolour)) - Returns a class holding the safe text colour of the colour. This can be used on images etc. to make sure the text is readable.
- shades ([List][list][[str]]) - The shades of the colour.
- square ([Image](image.md#Image)) - Returns a square image of the colour. This is an alias to [ColourImages](colour.md#colourimages)``.square``.
- tints ([List][list][[str]]) - The tints of the colour.
- websafe ([Colour](colour.md#colour)) - Returns a class holding the websafe version of the colour. This is for really old browsers that don't support the full colour range.


---

## ColourImages
Represents a class holding the different images of a [Colour](colour.md#colour)

### Attributes

- colour ([Colour](colour.md#colour)) - The colour that this class is holding the images for.
- gradient ([Image](image.md#Image)) - Returns a image with all possible gradients of the colour.
- square ([Image](image.md#Image)) - Returns a square image of the colour.

---

## ColourWebSafe
Represents a websafe version of a [Colour](colour.md#colour)

### Attributes
- cmyk [CMYK](colour.md#cmyk) - Returns a class holding the CMYK values of the colour.
- gradient ([Image](image.md#Image)) - Returns a image with all possible gradients of the colour. This is an alias to [ColourImages](colour.md#colourimages)``.gradient``
- hex ([Hex](colour.md#hex)) - Returns a class holding the hex value of the colour.
- hsl ([HSL](colour.md#hsl)) - Returns a class holding the HSL values of the colour.
- image ([str]) - The image of the colour. This is an alias to [ColourImages](colour.md#colourimages)``.square``.
- images ([ColourImages](colour.md#colourimages)) - Returns a class holding the different images of the colour. There are attributes on this class that can be used to get each image: ``.square`` and ``.gradient``.
- int ([int]) - The integer value of the colour.
- name ([str]) - The name of the colour.
- rgb [RGB](colour.md#rgb) - Returns a class holding the RGB values of the colour.
- safe_text_colour ([SafeTextColour](colour.md#safetextcolour)) - Returns a class holding the safe text colour of the colour. This can be used on images etc. to make sure the text is readable.
- shades ([List][list][[str]]) - The shades of the colour.
- square ([Image](image.md#Image)) - Returns a square image of the colour. This is an alias to [ColourImages](colour.md#colourimages)``.square``.
- tints ([List][list][[str]]) - The tints of the colour.
- websafe ([Colour](colour.md#colour)) - Returns this class. This is to prevent an infinite loop when getting the websafe version of a websafe colour.

---

## CMYK
Represents a class holding the CMYK values of a [Colour](colour.md#colour)

### Attributes
- string ([str]) - The CMYK value of the colour.
- values ([List][list][[int]]) - The CMYK values of the colour as a list of integers.
- c ([int]) - The cyan value of the colour.
- m ([int]) - The magenta value of the colour.
- y ([int]) - The yellow value of the colour.
- k ([int]) - The black value of the colour.


---

## RGB
Represents a class holding RGB values of a [Colour](colour.md#colour)

### Attributes
- r ([int]) - The red value of the colour.
- g ([int]) - The green value of the colour.
- b ([int]) - The blue value of the colour.
- string ([str]) - The RGB value of the colour.
- values ([List][list][[int]]) - 
    The RGB values of the colour as a list of integers.

---

## Hex
Represents a class holding information about a :class:`Colour`'s hex value.

### Attributes
- string ([str]) - The hex value of the colour.
- values (List[[str]]) - The hex value of the colour split into a list per two characters.
- clean ([str]) - The hex value of the colour without the ``#``.
- shorten ([Optional]\[[str]]) - The shortened hex value of the colour.

---

## HSL
Represents a class holding HSL values of a [Colour](colour.md#colour)

### Attributes
- string ([str]) - The HSL value of the colour.
- values ([List][list][[int]]) - The HSL values of the colour as a list of integers.
- h ([int]) - The hue value of the colour.
- s ([int]) - The saturation value of the colour.
- l ([int]) - The lightness value of the colour.


---

## SafeTextColour
Represents a class holding the "safe" version of a [Colour](colour.md#colour)

### Attributes
- name ([str]) - The name of the colour.
- hex ([str]) - The hex value of the colour.
- rgb [SafeTextColourRGB](colour.md#safetextcolourrgb) - The RGB values of the colour.

---

## SafeTextColourRGB
Represents a class holding RGB values of a [SafeTextColour](colour.md#safetextcolour)

### Attributes
- r ([int]) - The red value of the colour.
- g ([int]) - The green value of the colour.
- b ([int]) - The blue value of the colour.
- values ([List][list][[int]]) - The RGB values of the colour as a list of integers.




[str]: https://docs.python.org/3/library/stdtypes.html#str
[int]: https://docs.python.org/3/library/functions.html#int
[dict]: https://docs.python.org/3/library/functions.html#func-dict
[list]: https://docs.python.org/3/library/functions.html#func-list
[bool]: https://docs.python.org/3/library/functions.html#bool
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
[Optional]: https://docs.python.org/3/library/typing.html#typing.Optional

# Colour

Represents a colour from the API.

### Attributes

- **cmyk** ([`CMYK`](#cmyk))  
    Returns a class holding the CMYK values of the colour.
- **gradient** ([`Image`](image.md#image))  
    Returns an image showing all possible gradients of the colour. Alias for [`ColourImages`](#colourimages).gradient.
- **hex** ([`Hex`](#hex))  
    Returns a class holding the hex value of the colour.
- **hsl** ([`HSL`](#hsl))  
    Returns a class holding the HSL values of the colour.
- **image** ([`str`][str])
    The image of the colour. Alias for [`ColourImages`](#colourimages).square.
- **images** ([`ColourImages`](#colourimages))  
    Returns a class holding different images of the colour. Use `.square` and `.gradient` attributes to access each image.
- **int** ([`int`][int])
    The integer value of the colour.
- **name** ([`str`][str])  
    The name of the colour.
- **rgb** ([`RGB`](#rgb))  
    Returns a class holding the RGB values of the colour.
- **safe_text_colour** ([`SafeTextColour`](#safetextcolour))  
    Returns a class holding the safe text colour for readability on images, etc.
- **shades** ([`List`][list][[`str`][str]])
    The shades of the colour.
- **square** ([`Image`](image.md#image))  
    Returns a square image of the colour. Alias for [`ColourImages`](#colourimages).square.
- **tints** ([`List`][list][[`str`][str]]) 
    The tints of the colour.
- **websafe** ([`Colour`](#colour))  
    Returns a class holding the websafe version of the colour (for legacy browser support).

# ColourImages

Represents a class holding different images of a [Colour](#colour).

### Attributes

- **colour** ([`Colour`](#colour))
    The colour this class is associated with.
- **gradient** ([`Image`](image.md#image))  
    Returns an image with all possible gradients of the colour.
- **square** ([`Image`](image.md#image))  
    Returns a square image of the colour.

# ColourWebSafe

Represents a websafe version of a [Colour](#colour) but with the `websafe` attribute returning the same class for infinite recursion reasons.

# CMYK

Represents a class holding the CMYK values of a [Colour](#colour).

### Attributes

- **string** ([`str`][str]) 
    The CMYK value as a string.
- **values** ([`List`][list][[`int`][int]])  
    The CMYK values as a list of integers.
- **c** ([`int`][int])
    The cyan value.
- **m** ([`int`][int])
    The magenta value.
- **y** ([`int`][int])
    The yellow value.
- **k** ([`int`][int])
    The black value.

# RGB

Represents a class holding RGB values of a [Colour](#colour).

### Attributes

- **r** ([`int`][int]))  
    The red value.
- **g** ([`int`][int]))  
    The green value.
- **b** ([`int`][int]))  
    The blue value.
- **string** ([`str`][str]))  
    The RGB value as a string.
- **values** ([`List`][list][[`int`][int]])  
    The RGB values as a list of integers.

# Hex

Represents a class holding information about a colour's hex value.

### Attributes

- **string** ([`str`][str]) 
    The hex value as a string.
- **values** ([`List`][list][[`str`][str]])  
    The hex value split into a list (two characters per item).
- **clean** ([`str`][str])
    The hex value without the `#`.
- **shorten** ([`Optional`][Optional][[`str`][str]])
    The shortened hex value, if available.

# HSL

Represents a class holding HSL values of a [Colour](#colour).

### Attributes

- **string** ([`str`][str])
    The HSL value as a string.
- **values** ([`List`][list][[`int`][int]])
    The HSL values as a list of integers.
- **h** ([`int`][int]) 
    The hue value.
- **s** ([`int`][int])  
    The saturation value.
- **l** ([`int`][int])
    The lightness value.

# SafeTextColour

Represents a class holding the "safe" version of a [Colour](#colour) for text readability.

### Attributes

- **name** ([`str`][str]): The name of the colour.
- **hex** ([`str`][str]): The hex value of the colour.
- **rgb** ([`SafeTextColourRGB`](#safetextcolourrgb)): The RGB values of the colour.

# SafeTextColourRGB

Represents a class holding RGB values of a [SafeTextColour](#safetextcolour).

### Attributes

- **r** ([`int`][int])
    The red value.
- **g** ([`int`][int])
    The green value.
- **b** ([`int`][int])  
    The blue value.
- **values** ([`List`][list][[`int`][int]])  
    The RGB values as a list of integers.

---

[str]: https://docs.python.org/3/library/stdtypes.html#str  
[int]: https://docs.python.org/3/library/functions.html#int  
[dict]: https://docs.python.org/3/library/functions.html#func-dict  
[list]: https://docs.python.org/3/library/functions.html#func-list  
[bool]: https://docs.python.org/3/library/functions.html#bool  
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple  
[Optional]: https://docs.python.org/3/library/typing.html#typing.Optional

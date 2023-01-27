# Models // SillyCat
---

## SillyCat
Represents a silly cat image.

### Attribute
- url [str] - The unparsed URL of the image.
- left_hex [SillyCatPosition](sillycat.md#sillycatposition) - The left colour of the silly cat.
- right_hex [SillyCatPosition](sillycat.md#sillycatposition) - The right colour of the silly cat.

---

## SillyCatPosition
Represents a class holding the colours of a [SillyCat](sillycat.md#sillycat).

### Attributes
- hex [str] - The hex code of the colour.
- colour_name [str] - The name of the colour. This is only available if ``random``was set to ``True``. Use [fetch_colour_name](sillycat.md#await-fetch_colour_name---str) to call the ``colour`` endpoint for the name.
- image [Image](image.md#image) - Returns an [Image](image.md#image) object constructed from the unparsed URL of the image.
- simple_image [Image](image.md#image) - The simple image of the sillycat if available. This is a url with only the left hex colour.
- complex_image [Image](image.md#image) - The complex image of the sillycat if available. This is a url with both left and right hex colours.

### Methods
---

### await fetch_colour_name() -> [str]
Fetches the name of the colour from the ``colour`` endpoint.


[str]: https://docs.python.org/3/library/stdtypes.html#str
[int]: https://docs.python.org/3/library/functions.html#int
[dict]: https://docs.python.org/3/library/functions.html#func-dict
[list]: https://docs.python.org/3/library/functions.html#func-list
[bool]: https://docs.python.org/3/library/functions.html#bool
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
[Optional]: https://docs.python.org/3/library/typing.html#typing.Optional
[Union]: https://docs.python.org/3/library/typing.html#typing.Union
# Models // Image

## Image
Represents a class for all image endpoints.

### Attributes
- url [str] - The URL of the image.

### Methods
---

### await read(bytesio: [bool] = True) -> [Union]\[[bytes], [io.BytesIO][BytesIO]]

Returns the image data. If ``bytesio`` is ``True``, it will return a [io.BytesIO][BytesIO] object. Otherwise, it will return the raw [bytes].

#### Parameters
- bytesio ([bool]) - Whether to return the data as a :class:`io.BytesIO` object. Defaults to ``True``.

---

### await file(cls: ``FileLike``, filename: [str] = ``"image.png"``) -> ``FileLike``:
Converts the image to a file-like object.

#### Parameters
- cls (``FileLike``) - The file-like object to convert the image to. E,g, `discord.File` (discord.py)
- filename ([str]) - The filename to use.



[str]: https://docs.python.org/3/library/stdtypes.html#str
[int]: https://docs.python.org/3/library/functions.html#int
[dict]: https://docs.python.org/3/library/functions.html#func-dict
[list]: https://docs.python.org/3/library/functions.html#func-list
[bool]: https://docs.python.org/3/library/functions.html#bool
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
[Optional]: https://docs.python.org/3/library/typing.html#typing.Optional
[Any]: https://docs.python.org/3/library/typing.html#typing.Any
[Union]: https://docs.python.org/3/library/typing.html#typing.Union
[bytes]: https://docs.python.org/3/library/stdtypes.html#bytes
[BytesIO]: https://docs.python.org/3/library/io.html#io.BytesIO
# Image

Represents a class for all image endpoints.

## Attributes

- **url** ([`str`][str]): The URL of the image.

## Methods

### `await read(bytesio: bool = True) -> bytes | io.BytesIO`
Retrieves the image data asynchronously.

- If `bytesio` is `True` (default), returns an [`io.BytesIO`][BytesIO] object containing the image data.
- If `bytesio` is `False`, returns the raw image data as [`bytes`][bytes].
    
#### Parameters

- **bytesio** ([`Optional`][Optional][[`bool`][bool]]): Whether to return the data as an [`io.BytesIO`][BytesIO] object. Defaults to `True`.

#### Returns

- [`io.BytesIO`][BytesIO] or [`bytes`][bytes]: The image data in the requested format.

---

### `await file(cls: FileLike, filename: str = "image.png") -> FileLike`
Converts the image into a file-like object, suitable for uploading or further processing.

#### Parameters

- **cls** (`FileLike`): The file-like class or object to use (e.g., `discord.File` from discord.py).
- **filename** ([`Optional`][Optional][[`str`][str]]): The filename to assign to the image. Defaults to `"image.png"`.

#### Returns

- `FileLike`: The image wrapped in the specified file-like object.

---

[str]: https://docs.python.org/3/library/stdtypes.html#str  
[int]: https://docs.python.org/3/library/functions.html#int  
[bool]: https://docs.python.org/3/library/functions.html#bool  
[Optional]: https://docs.python.org/3/library/typing.html#typing.Optional  
[bytes]: https://docs.python.org/3/library/stdtypes.html#bytes  
[BytesIO]: https://docs.python.org/3/library/io.html#io.BytesIO  
# SillyCat
Represents a silly cat image.

## Attributes

- **url** ([`str`][str]):
    The unparsed URL of the image.
- **left_hex** ([`SillyCatPosition`](sillycat.md#sillycatposition)): 
    The left colour of the silly cat.
- **right_hex** ([`SillyCatPosition`](sillycat.md#sillycatposition)):
    The right colour of the silly cat.


# SillyCatPosition

Represents a class holding the colours of a [`SillyCat`](sillycat.md#sillycat).

## Attributes

- **hex** ([`str`][str]):  
    The hexadecimal code representing the colour.

- **colour_name** ([`str`][str]):  
    The human-readable name of the colour. This is only set if `random` was `True`. To retrieve the name, use [`fetch_colour_name`](sillycat.md#await-fetch_colour_name---str).

- **image** ([`Image`](image.md#image)):  
    An [`Image`](image.md#image) object created from the unparsed image URL.

- **simple_image** ([`Image`](image.md#image)):  
    The simple image of the silly cat, available as a URL using only the left hex colour.

- **complex_image** ([`Image`](image.md#image)):  
    The complex image of the silly cat, available as a URL using both left and right hex colours.

## Methods

- ### `await fetch_colour_name()`
    Fetches the name of the colour from the `colour` endpoint.

    #### Returns
    - [`str`][str]: The name of the colour.


[str]: https://docs.python.org/3/library/stdtypes.html#str  
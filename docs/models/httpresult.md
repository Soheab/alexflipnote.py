# HTTPResult

Represents the result returned from the `/http` endpoint.

## Attributes

- **code** ([`int`][int]):
    The HTTP status code returned by the endpoint.

- **name** ([`str`][str]):
    The standard name associated with the HTTP status code.

- **description** ([`str`][str]):
    A brief explanation of the HTTP status code.

## Example

```python
result = await alex_api.http_code(200)
print(result.code)        # 200
print(result.name)        # OK
print(result.description) # Indicates that the request has succeeded.
```

[int]: https://docs.python.org/3/library/functions.html#int
[str]: https://docs.python.org/3/library/stdtypes.html#str
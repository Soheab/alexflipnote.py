# AlexFlipnote.py Docs | Models/HTTPResult

## HTTPResult
Represents the result from the /http endpoint.

### Attributes
- code [int] - The HTTP status code.
- name [str] - The name of the HTTP status code.
- description [str] - The description of the HTTP status code.

### Example

```python
result = await alex_api.http_code(200)
print(result.code) # 200
print(result.name) # OK
print(result.description) # Indicates that the request has succeeded.
```


[str]: https://docs.python.org/3/library/stdtypes.html#str
[int]: https://docs.python.org/3/library/functions.html#int
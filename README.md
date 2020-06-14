# alexflipnote_api
 Wrapper for api: https://api.alexflipnote.dev/

# installation
> pip install alexflipnote-api

# Examples

### Get random cat pics:
```py
import alexflipnote_api

afa = alexflipnote-api.Client()

print(await afa.cats)
>>> https://api.alexflipnote.dev/cats/grRlHyi-AL8_cats.jpg
``` 

### Get dark supreme logo
```py
import alexflipnote_api

afa = alexflipnote-api.Client()

print(await afa.supreme("some text, yes", dark=True)
>>> https://api.alexflipnote.dev/cats/grRlHyi-AL8_cats.jpg
``` 
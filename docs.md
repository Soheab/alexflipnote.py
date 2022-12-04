# AlexFlipnote.py | Docs

An easy-to-use Python Wrapper for the [AlexFlipnote API](https://api.alexflipnote.dev)\
For any questions and support, you can join the [AlexFlipnote server](https://discord.gg/Alexflipnote)

## Getting Started:

To begin with, you'll have to install the package by doing one of the following commands:

- `pip install -U alexflipnote.py`
- `python -m pip -U install alexflipnote.py`

After that, you will have to create the client:

```python
import alexflipnote

alex_api = alexflipnote.Client()
```

For future reference in this documentation: when referring to 'alex_api' we refer to that above.

## Using the wrapper:

All available methods you can use.

### await alex_api.birb() -> [str]
Get a random birb (bird) picture or gif.

### await alex_api.cats() -> [str]
Get random cat picture or gif.

### await alex_api.coffee() -> [str]
Get a random coffee image. `This uses the coffee.alexflipnote.dev API.`

### await alex_api.colour(colour=None) -> [Colour]
Returns info on random or provided hex colour.\
**Aliases**: color

#### Parameters
- colour (Optional[[str]]) - HEX colour value

### await alex_api.dogs() -> [str]
Returns random dog picture or gif.

### await alex_api.support_server(creator = False) -> Union[[str], [tuple]]

Returns an invitation to the AlexFlipnote server + the creator of this wrapper.
#### Parameters
- creator ([bool]) - To also get an invitation to the server of creator of this wrapper.

--- 

## Colour

The object returned from [alex_api.colour()](#await-alex_apicolourcolournone)

**.black_or_white_text** -> [str] \
Whether the colour can be viewed on a black or white background.
Returns either `#000000` or `#FFFFFF`. 

**.brightness** -> [int] \
The colour's brightness value

**.hex** -> [str] \
The colour's HEX value

**.image** -> [str] \
Image of the colour

**.gradient** -> [str] \
Image with the colour's gradients

**.int** -> [int] \
The INT value of colour

**.name** -> [str] \
The name of colour

**.rgb_string** -> [str] \
The RGB values of colour

**.rgb** -> [RGB] \
A [RGB](#rgb) object

**.shades** -> [list] \
List of shades

**.tints** -> [list] \
The colour's tints

---

## RGB
The object returned from [Colour](#colour).rgb

**.raw** -> [dict] \
Dict of R, G, B values.

**.r** -> [int] \
The R value

**.g** -> [int] \
The G value

**.b** -> [int] \
The B value

---

# Examples
See here some examples

##### Get a random cat picture of gif:

```python
import asyncio
import alexflipnote

alex_api: alexflipnote.Client = alexflipnote.Client("YOUR-API-TOKEN")


async def get_cat() -> None:
    url = await alex_api.cats()
    print(url)
    await alex_api.close()  # preventing the "Unclosed client session" warning.


asyncio.run(get_cat())
``` 

##### Get a random sadcat picture or gif using [discord.py](https://github.com/Rapptz/discord.py):

```python
from discord.ext import commands

import alexflipnote

bot = commands.Bot("!")
# just a example, the client doesn't have to be under bot
alex_api = alexflipnote.Client()


@bot.command()
async def sadcat(ctx):
    url = await alex_api.sadcat()
    await ctx.send(f"Requested by {ctx.author}\n{url}")


# invoke: !sadcat

bot.run("TOKEN")
```


[str]: https://docs.python.org/3/library/stdtypes.html#str
[int]: https://docs.python.org/3/library/functions.html#int
[dict]: https://docs.python.org/3/library/functions.html#func-dict
[list]: https://docs.python.org/3/library/functions.html#func-list
[bool]: https://docs.python.org/3/library/functions.html#bool
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
[Colour]: docs.md#colour
[RGB]: docs.md#rgb
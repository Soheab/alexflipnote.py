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
All available methods and classes that are available in the wrapper are listed below.

### Methods:

- [achivement](docs/methods.md#await-alex_apiachievementtext-str-icon-unionstr-int-minecrafticon--minecrafticonrandom---image)
- [birb](docs/methods.md#await-alex_apibirb---str) (alias: bird)
- [calling](docs/methods.md#await-alex_apicallingtext-str---image)
- [captcha](docs/methods.md#await-alex_apicaptchatop-str-bottom-str---image)
- [cats](docs/methods.md#await-alex_apicats---str) (alias: cat)
- [challenge](docs/methods.md#await-alex_apichallengetext-str-icon-unionstr-int-minecrafticon--minecrafticonrandom---image)
- [close](docs/methods.md#await-alex_apiclose---none)
- [coffee](docs/methods.md#await-alex_apicoffee---str)
- [colour](docs/methods.md#await-alex_apicolourcolour-optionalstr--none---colour) (alias: color)
- [did_you_mean](docs/methods.md#await-alex_apidid_you_meantop-str-bottom-str---image) (alias: didyoumean)
- [dogs](docs/methods.md#await-alex_apidogs---str)
- [drake](docs/methods.md#await-alex_apidraketop-str-bottom-str---image)
- [facts](docs/methods.md#await-alex_apifactstext-str---image)
- [nft](docs/methods.md#await-alex_apinfthex-optionalstr--none-season-nftseason--nftseasonrandom--seed-optionalany--none-return_image-bool--false---nft)
- [pornhub](docs/methods.md#await-alex_apipornhubtext-str---image) (alias: ph)
- [sadcat](docs/methods.md#await-alex_apisadcat---str)
- [scroll](docs/methods.md#await-alex_apiscrolltext-str---image)
- [sillycat](docs/methods.md#await-alex_apisillycatleft_hex-optionalstr--none-right_hex-optionalstr--none--random-bool--true-seed-optionalany--none-return_image-bool--false---sillycat)
- [support_server](docs/methods.md#await-alex_apisupport_server-creator-bool--false---unionstr-tuplestr-str)

### Classes:

- [Colour](docs/models:colour.md)
- [NFT](docs/models/nft.md)
- [Image](docs/models/image.md)
- [SillyCat](docs/models/sillycat.md)

### Enums:

- [MinecraftIcon](docs/enums.md#minecrafticon)
- [NFTSeason](docs/enums#nftseason)


# Examples
See here some examples

##### Get a random cat picture of gif:

```python
import asyncio
import alexflipnote

alex_api: alexflipnote.Client = alexflipnote.Client()


async def get_cat() -> None:
    url = await alex_api.cat()
    print(url)
    await alex_api.close()  # preventing the "Unclosed client session" warning.


asyncio.run(get_cat())
``` 

##### Get a phub logo using [discord.py](https://github.com/Rapptz/discord.py):

```python
from discord.ext import commands

import alexflipnote

bot = commands.Bot("!")
# just a example, the client doesn't have to be under bot
alex_api = alexflipnote.Client()


@bot.command(aliases=["ph"])
async def phublogo(ctx, *, texts: str):
    white, yellow = texts.split(" | ")
    url = await alex_api.phub(white, yellow)
    await ctx.send(f"Requested by {ctx.author}\n{url}")


# invoke: !ph Epic Gamer | Moment

bot.run("TOKEN")
```
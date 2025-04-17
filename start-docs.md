# AlexFlipnote.py Documentation

An easy-to-use Python Wrapper for the [AlexFlipnote API](https://api.alexflipnote.dev).

For questions or support, join the [AlexFlipnote Discord server](https://discord.gg/Alexflipnote).

---

## 🚀 Getting Started

Install the package:

```sh
pip install -U alexflipnote.py
# or
python -m pip install -U alexflipnote.py
# or
python -m pip install -U git+https://github.com/soheab/alexflipnote.py
```

Create a client instance:

```python
import alexflipnote

alex_api = alexflipnote.Client()
```

Throughout this documentation, `alex_api` refers to your client instance.

---

## 📚 API Reference

### Methods

| Method                                                                                                                                                                                   | Description                            | Aliases      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------ |
| [`achievement`](docs/methods.md#await-alex_apiachievementtext-str-icon-unionstr-int-minecrafticon--minecrafticonrandom---image)                                                          | Generate a Minecraft achievement image |              |
| [`birb`](docs/methods.md#await-alex_apibirb---str)                                                                                                                                       | Get a random bird image                | `bird`       |
| [`calling`](docs/methods.md#await-alex_apicallingtext-str---image)                                                                                                                       | Generate a "calling" meme image        |              |
| [`captcha`](docs/methods.md#await-alex_apicaptchatop-str-bottom-str---image)                                                                                                             | Generate a fake captcha image          |              |
| [`cats`](docs/methods.md#await-alex_apicats---str)                                                                                                                                       | Get a random cat image or gif          | `cat`        |
| [`challenge`](docs/methods.md#await-alex_apichallengetext-str-icon-unionstr-int-minecrafticon--minecrafticonrandom---image)                                                              | Generate a Minecraft challenge image   |              |
| [`close`](docs/methods.md#await-alex_apiclose---none)                                                                                                                                    | Close the API client session           |              |
| [`coffee`](docs/methods.md#await-alex_apicoffee---str)                                                                                                                                   | Get a random coffee image              |              |
| [`colour`](docs/methods.md#await-alex_apicolourcolour-optionalstr--none---colour)                                                                                                        | Get colour information                 | `color`      |
| [`did_you_mean`](docs/methods.md#await-alex_apidid_you_meantop-str-bottom-str---image)                                                                                                   | Generate a "Did You Mean" meme image   | `didyoumean` |
| [`dogs`](docs/methods.md#await-alex_apidogs---str)                                                                                                                                       | Get a random dog image                 |              |
| [`drake`](docs/methods.md#await-alex_apidraketop-str-bottom-str---image)                                                                                                                 | Generate a Drake meme image            |              |
| [`facts`](docs/methods.md#await-alex_apifactstext-str---image)                                                                                                                           | Generate a random fact image           |              |
| [`nft`](docs/methods.md#await-alex_apinfthex-optionalstr--none-season-nftseason--nftseasonrandom--seed-optionalany--none-return_image-bool--false---nft)                                 | Generate a random NFT image            |              |
| [`pornhub`](docs/methods.md#await-alex_apipornhubtext-str---image)                                                                                                                       | Generate a Pornhub-style logo          | `ph`         |
| [`sadcat`](docs/methods.md#await-alex_apisadcat---str)                                                                                                                                   | Get a random sad cat image             |              |
| [`scroll`](docs/methods.md#await-alex_apiscrolltext-str---image)                                                                                                                         | Generate a scroll meme image           |              |
| [`sillycat`](docs/methods.md#await-alex_apisillycatleft_hex-optionalstr--none-right_hex-optionalstr--none--random-bool--true-seed-optionalany--none-return_image-bool--false---sillycat) | Generate a silly cat NFT               |              |
| [`support_server`](docs/methods.md#await-alex_apisupport_server-creator-bool--false---unionstr-tuplestr-str)                                                                             | Get the support server invite          |              |

### Classes

- [`Colour`](docs/models/colour.md)
- [`NFT`](docs/models/nft.md)
- [`Image`](docs/models/image.md)
- [`SillyCat`](docs/models/sillycat.md)

### Enums

- [`MinecraftIcon`](docs/enums.md#minecrafticon)
- [`NFTSeason`](docs/enums.md#nftseason)

---

## 💡 Examples

### Get a Random Cat Image

```python
import asyncio
import alexflipnote

alex_api = alexflipnote.Client()

async def get_cat():
    url = await alex_api.cat()
    print(url)
    await alex_api.close()  # Prevent "Unclosed client session" warning

asyncio.run(get_cat())
```

---

### Generate a Pornhub Logo with [discord.py](https://github.com/Rapptz/discord.py)

```python
from discord.ext import commands
import alexflipnote

bot = commands.Bot(command_prefix="!")
alex_api = alexflipnote.Client()

@bot.command(aliases=["ph"])
async def phublogo(ctx, *, texts: str):
    white, yellow = texts.split(" | ")
    url = await alex_api.phub(white, yellow)
    await ctx.send(f"Requested by {ctx.author}\n{url}")

# Usage: !ph Epic Gamer | Moment

bot.run("TOKEN")
```

---

## 📎 Additional Resources

- [Full Method Documentation](docs/methods.md)
- [Model Reference](docs/models)
- [Enum Reference](docs/enums.md)

---

**AlexFlipnote.py** makes it easy to integrate fun image generation and data endpoints into your Python projects and Discord bots!
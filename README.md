[![PyPi Version](https://img.shields.io/pypi/v/alexflipnote.py.svg)](https://pypi.python.org/pypi/alexflipnote.py/)
[![Downloads](https://pepy.tech/badge/alexflipnote-py)](https://pepy.tech/project/alexflipnote-py)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)


# AlexFlipnote.py
An easy to use Python Wrapper for the AlexFlipnote API

<img src="https://alexflipnote.dev/branding/assets/avatar.png" alt="drawing" width="300"/>

# Requirements
- Python 3.6 or above
- aiohttp (python3 -m pip install -U aiohttp)

# Documentation
See the full and detailed [docs here](https://github.com/Soheab/alexflipnote.py/blob/master/docs.md)

# Installation
Install the package by doing one of the following commands:

##### Using pip (recommended):
- `pip install alexflipnote.py -U`
- `python -m pip install alexflipnote.py -U`

# Changelog
See the changelog for each [version here](changelog.md)

# Examples

Make a custom [supreme](docs.md#await-alex_apisupremetext-dark-light) logo:
```python
import asyncio
import alexflipnote

alex_api = alexflipnote.Client()


async def custom_supreme_logo(text, dark=False, light=False):
    supreme = await alex_api.supreme(text, dark, light)
    print(supreme)
    # prints: https://api.alexflipnote.dev/supreme?text=%23some%20text,%20yes&dark=true
    await alex_api.close()  # preventing the "Unclosed client session" warning.


asyncio.get_event_loop().run_until_complete(custom_supreme_logo('#some text, yes', dark=True))
``` 

Minecraft [achievement](docs.md#await-alex_apiachievementtext-icon) using [discord.py](https://github.com/Rapptz/discord.py):
```python
import discord
import alexflipnote
from discord.ext import commands
from typing import Union


bot = commands.Bot(command_prefix="!")
alex_api = alexflipnote.Client() # just a example, the client doesn't have to be under bot.

@bot.command()
async def achievement(ctx, text: str, icon: Union[int, str] = None): 
    image = await (await alex_api.achievement(text=text, icon=icon)).read() # BytesIO
    await ctx.send(f"Rendered by {ctx.author}", file=discord.File(image, filename="achievement.png"))
    
# have this where you close the bot or somewhere to close the session and prevent the "Unclosed client session" warning.
await alex_api.close()

# we did a Union[int, str] since the wrapper accepts a number or string for the icon, see the icon section in docs to see what it accepts.

# invoke: !achievement "nice job!" diamond_sword
# see output here: https://i.imgur.com/l9OcQNw.png

bot.run("TOKEN")
```


# Made by

This wrapper is made by **Soheab#6240**, DM me on Discord or [join my Server](https://discord.gg/yCzcfju) for anything 
related to this wrapper.
 
You can join AlexFlipnote's [server here](https://discord.gg/DpxkY3x) to suggests something for the API.

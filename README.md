[![PyPi Version](https://img.shields.io/pypi/v/alexflipnote.py.svg)](https://pypi.python.org/pypi/alexflipnote.py/)
[![Downloads](https://pepy.tech/badge/alexflipnote-py)](https://pepy.tech/project/alexflipnote-py)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)


# Alexflipnote.py
An easy to use Python Wrapper for the AlexFlipnote API

![image](https://alexflipnote.dev/branding/assets/avatar.png)

# Requirements
- Python 3.6 or above
- aiohttp (python3 -m pip install -U aiohttp)
- url_regex (python3 -m pip install -U url_regex)

# Installation
Install the package by doing one of the following commands:

- `pip install alexflipnote.py`
- `python -m pip -U install alexflipnote.py`

# Documentation
See the full and detailed [docs here](https://github.com/Soheab/alexflipnote.py/blob/master/docs.md)

# Examples

Get a random cat pic:
```python
import alexflipnote

afa = alexflipnote.Client()

print(await afa.cats())
# output: https://api.alexflipnote.dev/cats/grRlHyi-AL8_cats.jpg
``` 

Make a custom supreme logo:
```python
import alexflipnote

afa = alexflipnote.Client()

print(await afa.supreme('#some text, yes', dark=True)) # making it dark, there is also light option.
# output: https://api.alexflipnote.dev/supreme?text=%23some%20text,%20yes&dark=true
```

Minecraft achievement using [discord.py](https://github.com/Rapptz/discord.py):
```python
import discord
import alexflipnote
from discord.ext import commands
from typing import Union
# just a example, alexflipnote client doesn't have to be under bot.

bot = commands.Bot(command_prefix="!")
alex_api = alexflipnote.Client()

@bot.command()
async def achievement(ctx, text, icon: Union[int, str] = None): 
    image = await (await alex_api.achievement(text=text, icon=icon)).read() # BytesIO
    await ctx.send(f"Rendered by {ctx.author}", file=discord.File(image, filename="achievement.png"))

# we did a Union[int, str] since the wrapper accepts a number or string for the icon, see the icon section in docs to see what it accepts.

# invoke: !achievement "nice job!" diamond_sword
# output: https://api.alexflipnote.dev/achievement?text=nice%20job&icon=3
bot.run("TOKEN")
```

# Made by

This wrapper is made Soheab_#6240, contact me on discord for anything related to this wrapper.

You can join my [discord server here](https://discord.gg/yCzcfju) or 
AlexFlipnote's [server here](https://discord.gg/alexflipnote) (recommended)

Please report any bugs in the servers above or dm.

Suggestions are also welcome.


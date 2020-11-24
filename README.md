![Downloads](https://static.pepy.tech/personalized-badge/alexflipnote-py?period=total&units=none&left_color=black&right_color=red&left_text=Total+Downloads)
[![PyPi Version](https://img.shields.io/pypi/v/alexflipnote.py.svg)](https://pypi.python.org/pypi/alexflipnote.py/)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

# AlexFlipnote.py
An easy to use Python Wrapper for the AlexFlipnote API

<img src="https://alexflipnote.dev/branding/assets/avatar.png" alt="drawing" width="200"/>

## 2.0.0
A recent (November 22) change to API has made an Authorization header with a personal token required for ALL endpoints. \
ALL previous versions of this wrapper will no longer work and are considered to be deprecated!

Wondering how to get an Auth token to use the API ? Join the API's support server here: https://discord.gg/DpxkY3x to request one.

You can pass your token in the constructor like so, `alexflipnote.Client("YOUR-API-TOKEN")`.

#### Embed
For embedding links see [this](https://github.com/Soheab/alexflipnote.py/blob/master/docs.md#embed)

## Requirements
- Python 3.6 or above
- aiohttp (python3 -m pip install -U aiohttp)

## Installation
Install the package by doing one of the following commands:

**Using pip (recommended)**:
- `pip install alexflipnote.py -U`
- `python -m pip install alexflipnote.py -U`

## Documentation
See the full and detailed [docs here](docs.md)

## Links
[API](https://api.alexflipnote.dev) | [Changelogs](changelog.md) | [Examples](docs.md#examples)

## Made by

This wrapper is made by **Soheab#6240**, DM me on Discord or join [my server here](https://discord.gg/yCzcfju) for anything 
related to this wrapper.
 
You can join [AlexFlipnote's server here](https://discord.gg/DpxkY3x) to suggest or report anything on the API.

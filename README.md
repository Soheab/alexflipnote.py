[![PyPi Version](https://img.shields.io/pypi/v/alexflipnote.py.svg)](https://pypi.python.org/pypi/alexflipnote.py/)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

# Alexflipnote.py
 An easy to use Python Wrapper for the AlexFlipnote API


# Requirements
- Python 3.6 or above
- aiohttp (python3 -m pip install -U aiohttp)
- url_regex (python3 -m pip install -U url_regex)

# installation

### Using pip (recommended):
Install the package by doing one of the following commands:

- `pip install alexflipnote.py`
- `python -m pip -U install alexflipnote.py`

# Documentation
---
See the full and detailed [docs here](docs.md)
# Examples

#### Get a random cat pic:

```py
import alexflipnote

afa = alexflipnote.Client()

print(await afa.cats())
>>> https://api.alexflipnote.dev/cats/grRlHyi-AL8_cats.jpg
``` 

#### Get supreme logo:

```py
import alexflipnote

afa = alexflipnote.Client()

print(await afa.supreme("#some text, yes", dark=True)) # making it dark, there is also light = True.
>>> https://api.alexflipnote.dev/supreme?text=%23some%20text,%20yes&dark=true
``` 

# Made by

This wrapper is made Soheab_#6240, contact me for anything related to this wrapper.

You can join my discord [server here](https://discord.gg/yCzcfju) or 
AlexFlipnote's [server here](https://discord.gg/alexflipnote) (recommended)

Please report any bugs in the servers above or dm.

Suggestions are also welcome.


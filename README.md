[![Downloads Total](https://pepy.tech/badge/alexflipnote-py)](https://pepy.tech/project/alexflipnote-py)
[![Downloads Month](https://pepy.tech/badge/alexflipnote-py/month)](https://pepy.tech/project/alexflipnote-py)
[![Downloads Week](https://pepy.tech/badge/alexflipnote-py/week)](https://pepy.tech/project/alexflipnote-py)
[![PyPi Version](https://img.shields.io/pypi/v/alexflipnote.py.svg)](https://pypi.python.org/pypi/alexflipnote.py/)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

# AlexFlipnote.py

An easy-to-use Python Wrapper for the AlexFlipnote API

<img src="https://alexflipnote.dev/branding/assets/avatar.png" alt="drawing" width="200"/>

## 2.0.0

A recent (November 22) change to API has made an Authorization header with a personal token required for ALL
endpoints. \
ALL previous versions of this wrapper will no longer work and are considered to be deprecated!

Wondering how to get an Auth token to use the API ? Join the API's support server here: https://discord.gg/DpxkY3x to
request one.

You can pass your token in the constructor like so, `alexflipnote.Client("YOUR-API-TOKEN")`.

#### Embed

For embedding links see [this][embed_example]

## Requirements

- Python 3.6 or above
- aiohttp (python3 -m pip install -U aiohttp)

## Installation

Install the package by doing one of the following commands:

**Using pip (recommended)**:

- `pip install alexflipnote.py -U`
- `python -m pip install alexflipnote.py -U`

## Documentation

See the full and detailed [docs here][docs]

## Links

[API][base_url] | [Changelogs][changelog] | [Examples][examples] | [Github][github] | [PyPi][pypi]

## Made by

This wrapper is made by **Soheab#6240**, DM me on Discord or join my server [here][discord_mine] for anything related to
this wrapper.

You can join AlexFlipnote's server [here][discord_alexflipnote] to suggest or report anything on the API.

## Other Wrappers

- **C#:** [GitHub][wrappers_c#-github] | [Nuget][wrappers_c#-nuget]
- **Javascript:** [GitHub][wrappers_js-github] | [Npm][wrapper_js-npm]


[docs]: https://github.com/Soheab/alexflipnote.py/blob/master/docs.md
[changelog]: https://github.com/Soheab/alexflipnote.py/blob/master/changelog.md
[examples]: https://github.com/Soheab/alexflipnote.py/blob/master/docs.md#examples
[embed_example]: https://github.com/Soheab/alexflipnote.py/blob/master/docs.md#embed
[base_url]: https://api.alexflipnote.dev
[github]: https://github.com/Soheab/alexflipnote.py
[pypi]: https://pypi.org/project/alexflipnote.py/
[discord_alexflipnote]: https://discord.gg/DpxkY3x
[discord_mine]: https://discord.gg/yCzcfju
[wrappers_c#-github]: https://github.com/VACEfron/AlexFlipnote.NET
[wrappers_c#-nuget]: https://www.nuget.org/packages/AlexFlipnote.NET/
[wrappers_js-github]: https://github.com/HarutoHiroki/alexflipnote.js
[wrapper_js-npm]: https://www.npmjs.com/package/alexflipnote.js

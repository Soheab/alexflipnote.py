from re import MULTILINE, search

from setuptools import setup  # type: ignore

with open("README.md") as f:
    readme = f.read()

# source: https://github.com/Rapptz/discord.py/blob/master/setup.py
with open("alexflipnote/__init__.py") as f:
    content = f.read()
    version = search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content, MULTILINE).group(1)
    author = search(r'^__author__\s*=\s*[\'"]([^\'"]*)[\'"]', content, MULTILINE).group(1)
    _license = search(r'^__license__\s*=\s*[\'"]([^\'"]*)[\'"]', content, MULTILINE).group(1)

setup(
    name="alexflipnote.py",
    description="An easy to use Python Wrapper for the AlexFlipnote API",
    long_description=readme,
    long_description_content_type="text/markdown",
    version=version,
    packages=["alexflipnote"],
    url="https://github.com/Soheab/alexflipnote.py/tree/2.x",
    download_url=f"https://github.com/Soheab/alexflipnote.py/archive/v{version}.tar.gz",
    license=_license,
    author=author,
    install_requires=["aiohttp"],
    keywords=[
        "alexflipnote",
        "discord",
        "api",
        "wrapper",
        "discord.py",
    ],
    project_urls={
        "Discord": "https://discord.gg/DpxkY3x",
        "Documentation": "https://github.com/Soheab/alexflipnote.py/blob/2.x/docs.md",
    },
    python_requires=">=3.8",
)

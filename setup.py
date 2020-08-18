from re import search, MULTILINE

from setuptools import setup  # type: ignore

with open('README.md') as f:
    readme = f.read()

# source: https://github.com/Rapptz/discord.py/blob/master/setup.py#L9-L10
with open('alexflipnote/__init__.py') as f:
    version = search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), MULTILINE).group(1)

setup(
    name = 'alexflipnote.py',
    description = 'An easy to use Python Wrapper for the AlexFlipnote API',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    version = version,
    packages = ['alexflipnote'],
    url = 'https://github.com/Soheab/Alexflipnote.py',
    download_url = f'https://github.com/Soheab/alexflipnote.py/archive/v{version}.tar.gz',
    license = 'MIT',
    author = 'Soheab_',
    install_requires = ['aiohttp'],
    keywords = ['alexflipnote', 'discord', 'api'],
    project_urls = {
        "Discord": "https://discord.gg/DpxkY3x",
        "Source": "https://github.com/Soheab/alexflipnote.py",
        "Documentation": "https://github.com/Soheab/alexflipnote.py/blob/master/docs.md",
        "Issue tracker": "https://github.com/Soheab/alexflipnote.py/issues",
    },

    python_requires = '>=3.6',
)

from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name = 'alexflipnote.py',
    version = '1.0.0',
    packages = ['alexflipnote'],
    url = 'https://github.com/Soheab/Alexflipnote.py',
    download_url = 'https://github.com/Soheab/alexflipnote.py/archive/1.0.0.tar.gz',
    license = 'MIT',
    author = 'Soheab',
    author_email = '',
    install_requires=['aiohttp', 'url_regex'],
    description = 'An easy to use Python Wrapper for the AlexFlipnote API',
    long_description=readme,
    python_requires='>=3.6',
)

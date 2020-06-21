from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name = 'alexflipnote.py',
    version = '1.2.4',
    packages = ['alexflipnote'],
    url = 'https://github.com/Soheab/Alexflipnote.py',
    download_url = 'https://github.com/Soheab/alexflipnote.py/archive/1.2.4.tar.gz',
    license = 'MIT',
    author = 'Soheab',
    author_email = '',
    install_requires=['aiohttp', 'url_regex'],
    description = 'An easy to use Python Wrapper for the AlexFlipnote API',
    long_description=readme,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
)

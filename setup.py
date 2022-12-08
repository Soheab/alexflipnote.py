import re

from setuptools import setup  # type: ignore

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

readme = ""
with open("README.md") as f:
    readme = f.read()

# source: https://github.com/Rapptz/discord.py/blob/master/setup.py
version = ""
with open("alexflipnote/__init__.py") as f:
    content = f.read()
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)  # type: ignore
    author = re.search(r'^__author__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)  # type: ignore
    license = re.search(r'^__license__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)  # type: ignore
    description = re.search(r'^__description__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)  # type: ignore

if not version:
    raise RuntimeError("version is not set")

_GITHUB_URL: str = "https://github.com/Soheab/alexflipnote.py"
_CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Framework :: aiohttp",
    "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Internet",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
    "Typing :: Typed",
]
_KEYWORDS = [
    "alexflipnote",
    "discord",
    "api",
    "wrapper",
    "discord.py",
]
_URLS = {
    "Discord": "https://discord.gg/yCzcfju",
    "Documentation": "https://github.com/Soheab/alexflipnote.py/blob/master/start-docs.md",
    "Issue tracker": f"{_GITHUB_URL}/issues",
}
_PACKAGES = [
    "alexflipnote",
    "alexflipnote._types",
    "alexflipnote.models",
]
setup(
    author=author,
    name="alexflipnote.py",
    url=_GITHUB_URL,
    description=description,
    license=license,
    long_description=readme,
    long_description_content_type="text/markdown",
    version=version,
    packages=_PACKAGES,
    download_url=f"{_GITHUB_URL}/archive/refs/tags/v{version}.tar.gz",
    install_requires=requirements,
    keywords=_KEYWORDS,
    project_urls=_URLS,
    python_requires=">=3.8",
    classifiers=_CLASSIFIERS,
)

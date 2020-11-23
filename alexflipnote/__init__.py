from .classes import Colour, MinecraftIcons, Image, Filters
from .client import BadRequest, Client, InternalServerError, NotFound
from .errors import BadRequest, HTTPException, InternalServerError, NotFound

Icon = MinecraftIcons  # if anyone was using the enum directly for some reason..

__license__ = "MIT"
__author__ = "Soheab_"
__version__ = "2.0.1"

# source: https://raw.githubusercontent.com/AlexFlipnote/discord_bot.py/master/utils/http.py

import asyncio

import aiohttp


# Removes the aiohttp ClientSession instance warning.
class HTTPSession(aiohttp.ClientSession):
    """ Abstract class for aiohttp. """

    def __init__(self, loop=None):
        self.my_loop = asyncio.get_event_loop()
        super().__init__(loop = loop or self.my_loop)


session = HTTPSession()

#try:
  #  session.my_loop.run_until_complete(session.close())
#except RuntimeError:
   # pass


async def query(url, method="get", res_method="text", *args, **kwargs):
    async with getattr(session, method.lower())(url, *args, **kwargs) as res:
        return await getattr(res, res_method)()


async def get(url, *args, **kwargs):
    return await query(url, "get", *args, **kwargs)


async def post(url, *args, **kwargs):
    return await query(url, "post", *args, **kwargs)


async def close():
    if not session.closed:
        await session.close()
    return

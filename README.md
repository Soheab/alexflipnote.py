# alexflipnote_api
 Wrapper for api: https://api.alexflipnote.dev/

# installation
> pip install alexflipnote-api

# Examples

### Get random cat pics:
```py
import alexflipnote_api

afa = alexflipnote-api.Client()

print(await afa.cats)
>>> https://api.alexflipnote.dev/cats/grRlHyi-AL8_cats.jpg
``` 

### Get supreme logo
```py
import alexflipnote_api

afa = alexflipnote-api.Client()

print(await afa.supreme("some text, yes", dark=True) # making it dark, there is also light = True.
>>> https://api.alexflipnote.dev/supreme?text=%23some%20text,%20yes&dark=true
``` 

### Color info command in a discord.py Bot

```py

import alexflipnote_api as ap
from discord.ext import commands

bot = commands.Bot(command_prefix="!"
colour_api = ap.Client()

# source: https://github.com/AlexFlipnote/discord_bot.py/blob/6d1adc72e9c19bb4ca90718e5f6d335faf842dd9/cogs/fun.py#L114-L147

@bot.command(aliases=['color'])
async def colourinfo(ctx, colour: str)):
    """ View the colour HEX details """
    async with ctx.channel.typing():
        if not permissions.can_embed(ctx):
            return await ctx.send("I can't embed in this channel ;-;")

        if colour == "random":
            colour = "%06x" % random.randint(0, 0xFFFFFF)

        if colour[:1] == "#":
            colour = colour[1:]

        if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', colour):
            return await ctx.send("You're only allowed to enter HEX (0-9 & A-F)")

        try:
            get_color = color_api.colour(colour)
        except aiohttp.ClientConnectorError:
            return await ctx.send("The API seems to be down...")
        except aiohttp.ContentTypeError:
            return await ctx.send("The API returned an error or didn't return JSON...")

        embed = discord.Embed(colour=r["int"])
        embed.set_thumbnail(url=r["image"])
        embed.set_image(url=r["image_gradient"])

        embed.add_field(name="HEX", value=r['hex'], inline=True)
        embed.add_field(name="RGB", value=r['rgb'], inline=True)
        embed.add_field(name="Int", value=r['int'], inline=True)
        embed.add_field(name="Brightness", value=r['brightness'], inline=True)

        await ctx.send(embed=embed, content=f"{ctx.invoked_with.title()} name: **{r['name']}**")


```
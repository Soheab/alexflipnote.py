# AlexFlipnote.py | Docs
An easy to use Python Wrapper for the [AlexFlipnote API](https://api.alexflipnote.dev)\
For any questions and support, you can join the [AlexFlipnote server](https://discord.gg/DpxkY3x)

## Getting Started:

To begin with, you'll have to install the package by doing one of the following commands:
- `pip install -U alexflipnote.py`
- `python -m pip -U install alexflipnote.py`
 
After that, you will have to create the client:

```python
import alexflipnote

alex_api = alexflipnote.Client()
```

For future reference in this documentation: when referring to 'alex_api' we refer to that above.
 
  
## Using the wrapper:
All available endpoints you can use.

### await alex_api.achievement(text, icon)
Generate a Minecraft achievement with custom text.

**Parameters**:
- text `string` | Text for the achievement.
- icon `string, int, Icon` | The icon you want, ignored if invalid.

**Return type**: [Image](docs.md#image "Image object attributes")

---
### await alex_api.amiajoke(image)
Get an "am i a joke" picture with your image.
  
**Parameters**:
- image `string` | URL of the image you want.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.birb()
Get a random birb picture.

**Return type:** String

---
### await alex_api.calling(text)
Get a calling meme image with your text.

**Parameters**:
- text `string` | Your text for the image.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.captcha(text)
Make a ~~fake~~ captcha with your text.

**Parameters**:
- text `string` | Your text for the image.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.cats()
Get a random cat picture.

**Return type:** String

---
### await alex_api.challenge(text, icon)
Generate a Minecraft challenge with custom text.

**Parameters**:
- text `string` | our text for the challenge.
- icon `string, int, Icon` | The icon you want, ignored if invalid.

**Return type**: [Image](docs.md#image "Image object attributes")

---
### await alex_api.colour(colour)
Get info on provided colour.

**Aliases**: color

**Parameters**:
- text `string` | The Colour. Defaults to random colour.

**Return type:** [Colour](docs.md#colour "Image object attributes")

---
### await alex_api.github_colours()
Get all github colours, per language.

**Return type:** JSON

---
### await alex_api.colour_image(colour)
Get an image of provided colour.

**Parameters**:
- text `string` | The Colour. Defaults to random colour.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.colour_image_gradient(colour)
Get an image gradients of provided colour.

**Parameters**:
- text `string` | The Colour. Defaults to random colour.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.didyoumean(top, bottom)
Get a custom google "Did you mean" suggestion thing.

**Parameters**:
- top `string` | What you search for.
-bottom `string` | The suggested search.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.dogs()
Get a random dog picture.

**Return type:** String

---
### await alex_api.drake(top, bottom)
Make a custom drake meme image.

**Parameters**:
- top `string` | Bad thing.
- bottom `string` | Good thing.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.facts(text)
Get the facts book.

**Parameters**:
- text `url` | The fact.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.filter(name, image)
Put a filter on an image.

**Available options:** `blur`, `invert`, `b&w`, `deepfry`, `sepia`, `pixelate`,
                    `magik`, `jpegify`, `wide`, `snow`, `gay`, `communist`, `random`
  
**Parameters**:
- name `string` | The filter name, see **Available options**. `random` will be a random filter from options above.
- image `string` | The image to put the filter on.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.floor(text, image)
Get a "Don't touch the floor" meme with your text and image.

**Parameters**:
- text `string` | The text you want.
- image `string` | The image you want.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.fml()
Get a random fu*k my life text.

**Return type:** String

---
### await alex_api.jokeoverhead(image)
When da jokes goes over da head.

**Parameters**:
- image `url` | The person's avatar.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.pornhub(text, text2)
Make a custom Pornhub logo!

**Parameters**:
- text `string` | The white part. ~~Porn~~
- text2 `string` | The yellow part. ~~Hub~~

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.sadcat()
Get a random sadcat picture.

**Return type:** String

---
### await alex_api.salty(image)
When someone is being salty.

**Parameters**:
- image `string` | The person's avatar.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.scroll(text)
Make that scroll meme with your text.

**Parameters**:
- text `string` | The scroll text.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.ship(user, user2)
Ship someone or yourself with someone else.

**Parameters**:
- user `string` | The user's avatar.
- user2 `string` | Someone else's avatar.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.supreme(text, dark, light)
Make a custom supreme logo.

**Parameters**:
- text `string` | Text for the logo.
- dark `boolean` | Make the background dark.
- light `boolean` | Make the background light.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.trash(face, trash)
Throw someone in the trash bin 🚮

**Parameters**:
- face `url` | Your avatar.
- trash `url` | Someone else's avatar.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await alex_api.support_server(creator)
Get an invitation to the AlexFlipnote server (or and the creator of this wrapper.)

**Parameters**:
- creator `boolean` | To also get an invitation to the server of creator of this wrapper.

**Return type**: string or tuple when `creator` is True

# Examples
See here some examples

##### Make a custom [supreme](docs.md#await-alex_apisupremetext-dark-light) logo:
```python
import asyncio
import alexflipnote

alex_api = alexflipnote.Client()


async def custom_supreme_logo(text, dark=False, light=False):
    supreme = await alex_api.supreme(text, dark, light)
    print(supreme)
    # prints: https://api.alexflipnote.dev/supreme?text=%23some%20text,%20yes&dark=true
    await alex_api.close()  # preventing the "Unclosed client session" warning.


asyncio.get_event_loop().run_until_complete(custom_supreme_logo('#some text, yes', dark=True))
``` 

##### Minecraft [achievement](docs.md#await-alex_apiachievementtext-icon) using [discord.py](https://github.com/Rapptz/discord.py):
```python
import discord
import alexflipnote
from discord.ext import commands
from typing import Union


bot = commands.Bot(command_prefix="!")
alex_api = alexflipnote.Client() # just a example, the client doesn't have to be under bot.

@bot.command()
async def achievement(ctx, text: str, icon: Union[int, str] = None): 
    image = await (await alex_api.achievement(text=text, icon=icon)).read() # BytesIO
    await ctx.send(f"Rendered by {ctx.author}", file=discord.File(image, filename="achievement.png"))
    
# have this where you close the bot or somewhere to close the session and prevent the "Unclosed client session" warning.
await alex_api.close()

# we did a Union[int, str] since the wrapper accepts a number or string for the icon, see the icon section in docs to see what it accepts.

# invoke: !achievement "nice job!" diamond_sword
# see output here: https://i.imgur.com/l9OcQNw.png

bot.run("TOKEN")
```

# Objects
Here is explained what attributes the returned objects have

## Image
The object returned from `alex_api.achievement()`, `alex_api.amiajoke()`, `alex_api.bad()`, `alex_api.calling()`, `alex_api.captcha()`,
    `alex_api.challenge()`, `alex_api.colour_image()`, `alex_api.colour_image_gradient()`, `alex_api.colourify()`, `alex_api.didyoumean()`,
    `alex_api.drake()`, `alex_api.facts()`, `alex_api.filter()`, `alex_api.floor()`, `alex_api.jokeoverhead()`, `alex_api.pornhub()`,
    `alex_api.salty()`, `alex_api.scroll()`, `alex_api.ship()`, `alex_api.supreme()` and `alex_api.trash()`
    
#### Image.url
The url of the image

#### await Image.read()
This will return a BytesIO object, which can be passed to discord.File() with a filename 
for [discord.py](https://github.com/Rapptz/discord.py):
```py
supreme_logo = await alex_api.supreme("ah yes")
supreme_bytes = await supreme_logo.read() # <_io.BytesIO object at 0x0438DFC8> - BytesIO object.
await ctx.send(file=discord.File(supreme_bytes, filename="supreme.png"))
```

## Colour
The object returned from `alex_api.colour()`

#### Colour.blackorwhite_text
The colour's blackorwhite_text hex

#### Colour.brightness
The colour's brightness value

#### Colour.hex
The colour's HEX value

#### Colour.image
An image of the colour

#### Colour.image_gradient
An image of the colour's gradient

#### Colour.int
The INT value of colour

#### Colour.name
The name of colour

#### Colour.rgb
The RGB values of colour

#### Colour.rgb_values
A [ColourRGB](docs.md#colourrgb) object

#### Colour.shade
The colour's shades

#### Colour.tint
The colour's tints

## ColourRGB
The object returned from `alex_api.colour().rgb_values`

#### ColourRGB.all
All RGB values of the colour in a dict 

#### ColourRGB.r
The R values of the colour

#### ColourRGB.g
The G values of the colour

#### ColourRGB.b
The B values of the colour

## Icon
---
The objects you can pass to the icon param for `alex_api.achievement()` and `alex_api.challenge()`

#### int:

**1:** `grass_block`, **2:** `diamond`, **3:** `diamond_sword`, **4:** `creeper`, **5:** `pig`, \
**6:** `tnt`, **7:** `cookie`, **8:** `heart`, **9:** `bed`, **10:** `cake`, \
**11:** `sign` **12:** `rail` **13:** `crafting_bench` **14:** `redstone`, **15:** `fire`, \
**16:** `cobweb`, **17:** `chest`, **18:** `furnace`, **19:** `book`, **20:** `stone_block`, \
**21:** `wooden_plank_block`, **22:** `iron_ingot`, **23:** `gold_ingot`, **24:** `wooden_door`, **25:** `iron_door`, \
**26:** `diamond_chestplate`, **27:** `flint_and_steel`, **28:** `glass_bottle`, **29:** `splash_potion`, **30:** `creeper_spawnegg`, \
**31:** `coal`, **32:** `iron_sword`, **33:** `bow`, **34:** `arrow`, **35:** `iron_chestplate`, \
**36:** `bucket`, **37:** `bucket_with_water`, **38:** `bucket_with_lava`, **39:** `bucket_with_milk`, **40:** `diamond_boots`, \
**41:** `wooden_hoe`, **42:** `bread`, **43:** `wooden_sword`, **44:** `bone`, **45:** `oak_log`

#### str:

`grass_block`, `diamond`, `diamond_sword`, `creeper`, `pig`, `tnt`, `cookie`, `heart`, `bed`, `cake`,
`sign`, `rail`, `crafting_bench`, `redstone`, `fire`, `cobweb`, `chest`, `furnace`, `book`, `stone_block`,
`wooden_plank_block`, `iron_ingot`, `gold_ingot`, `wooden_door`, `iron_door`, `diamond_chestplate`, `flint_and_steel`, `glass_bottle`, `splash_potion`, `creeper_spawnegg`,
`coal`, `iron_sword`, `bow`, `arrow`, `iron_chestplate`, `bucket`, `bucket_with_water`, `bucket_with_lava`, `bucket_with_milk`, `diamond_boots`,
`wooden_hoe`, `bread`, `wooden_sword`, `bone`, `oak_log`

#### object:

`Icon.grass_block`, `Icon.diamond`, `Icon.diamond_sword`, `Icon.creeper`, `Icon.pig`, `Icon.tnt`,
`Icon.cookie`, `Icon.heart`, `Icon.bed`, `Icon.cake`, `Icon.sign`, `Icon.rail`,
`Icon.crafting_bench`, `Icon.redstone`, `Icon.fire`, `Icon.cobweb`, `Icon.chest`, `Icon.furnace`,
`Icon.book`, `Icon.stone_block`, `Icon.wooden_plank_block`, `Icon.iron_ingot`, `Icon.gold_ingot`, `Icon.wooden_door`,
`Icon.iron_door`, `Icon.diamond_chestplate`, `Icon.flint_and_steel`, `Icon.glass_bottle`, `Icon.splash_potion`, `Icon.creeper_spawnegg`,
`Icon.coal`, `Icon.iron_sword`, `Icon.bow`, `Icon.arrow`, `Icon.iron_chestplate`, `Icon.bucket`,
`Icon.bucket_with_water`, `Icon.bucket_with_lava`, `Icon.bucket_with_milk`, `Icon.diamond_boots`, `Icon.wooden_hoe`, `Icon.bread`,
`Icon.wooden_sword`, `Icon.bone`, `Icon.oak_log`

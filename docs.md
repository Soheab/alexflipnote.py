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

alex_api = alexflipnote.Client("YOUR-API-TOKEN")
```

For future reference in this documentation: when referring to 'alex_api' we refer to that above.

## Using the wrapper:

All available endpoints you can use.

### await alex_api.achievement(text, icon = MinecraftIcons.RANDOM)

Generate a Minecraft achievement with custom text and icon.

**Parameters**:

- text `string` | Text for the achievement.
- icon `string, int or MinecraftIcons` | The icon you want from [here](docs.md#MinecraftIcons). `defaults to random`

**Return type**: [Image](docs.md#image "Image object attributes")

---

### await alex_api.amiajoke(image)

Get an "am i a joke" picture with your avatar.

**Parameters**:

- image `string` | URL of the avatar.

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

### await alex_api.challenge(text, icon = MinecraftIcons.RANDOM)

Generate a Minecraft challenge with custom text.

**Parameters**:

- text `string` | Text for the challenge.
- icon `string, int or MinecraftIcons` | The icon you want from [here](docs.md#MinecraftIcons). `defaults to random`

**Return type**: [Image](docs.md#image "Image object attributes")

---

### await alex_api.colour(colour = None)

Get info on provided colour.

**Aliases**: color

**Parameters**:

- text `string` | The Colour. `Defaults to random colour.`

**Return type:** [Colour](docs.md#colour "Image object attributes")

---

### await alex_api.github_colours()

Get all github colours, per language.

**Aliases**: github_color

**Return type:** JSON

---

### await alex_api.colour_image(colour = None)

Get an image of provided colour.

**Aliases**: color_image

**Parameters**:

- text `string` | The Colour. `Defaults to random colour.`

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await alex_api.colour_image_gradient(colour = None)

Get an image gradients of provided colour.

**Aliases**: color_image_gradient

**Parameters**:

- text `string` | The Colour. `Defaults to random colour.`

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await alex_api.didyoumean(top, bottom)

Get a custom google "Did you mean" suggestion thing.

**Parameters**:

- top `string` | What you search for. -bottom `string` | The suggested search.

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
`magik`, `jpegify`, `wide`, `flip`, `snow`, `gay`, `communist`, `random`,
[Filters enum](docs.md#Filters), number from 1 to 14.

**Parameters**:

- name `string, int or Filters` | The filter name from [here](docs.md#Filters) or see Available options. `random` will
  be a random filter from options above.
- image `string` | The image to put the filter on.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await alex_api.floor(text, image = None)

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

### await alex_api.shame(image)

Make that "Dock Of Shame" picture with your own image.

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

### await alex_api.supreme(text, dark = False, light = False)

Make a custom supreme logo.

**Parameters**:

- text `string` | Text for the logo.
- dark `boolean` | Make the background dark. `Defaults to False`
- light `boolean` | Make the background light. `Defaults to False`

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await alex_api.trash(face, trash)

Throw someone in the trash bin 🚮

**Parameters**:

- face `url` | Your avatar.
- trash `url` | Someone else's avatar.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await alex_api.what(image)

Create an image with "what" and an image.

**Parameters**:

- image `url` | A discord avatar URL.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await alex_api.support_server(creator = False)

Get an invitation to the AlexFlipnote server (or and the creator of this wrapper.)

**Parameters**:

- creator `boolean` | To also get an invitation to the server of creator of this wrapper.

**Return type**: string or tuple when `creator` is True. `Defaults to False`

# Examples

See here some examples

##### Make a custom [supreme](docs.md#await-alex_apisupremetext-dark-light) logo:

[Output](https://api.alexflipnote.dev/supreme?text=%23some%20text,%20yes&dark=true)

```python
import asyncio
import alexflipnote

alex_api = alexflipnote.Client("YOUR-API-TOKEN")


async def custom_supreme_logo(text, dark=False, light=False):
    supreme = await alex_api.supreme(text, dark, light)
    print(supreme)
    await alex_api.close()  # preventing the "Unclosed client session" warning.


asyncio.get_event_loop().run_until_complete(custom_supreme_logo('#some text, yes', dark=True))
``` 

##### Minecraft [achievement](docs.md#await-alex_apiachievementtext-icon) (same for `alex_api.challenge()`) using [discord.py](https://github.com/Rapptz/discord.py):

[Output](https://api.alexflipnote.dev/achievement?text=nice%20job&icon=3)

```python
import discord
import alexflipnote
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
alex_api = alexflipnote.Client("YOUR-API-TOKEN") # just a example, the client doesn't have to be under bot.

@bot.command()
async def achievement(ctx, text: str, icon = None): 
    image = await alex_api.achievement(text=text, icon=icon)
    image_bytes = await image.read()
    file = discord.File(image_bytes, "achievement.png")
    await ctx.send(f"Rendered by {ctx.author}", file=file)


# have this where you close the bot or somewhere to close the session and prevent the "Unclosed client session" warning.
await alex_api.close()

# invoke: !achievement "nice job!" diamond_sword

bot.run("TOKEN")
```

##### Embed

Since the API now requires a token for all endpoints, you can't embed a link from the API anymore.. but here is how to
embed it via a file using [discord.py](https://github.com/Rapptz/discord.py):

```python
import discord
import alexflipnote
from discord.ext import commands

bot = commands.Bot(command_prefix = "!!")
alex_api = alexflipnote.Client("YOUR-API-TOKEN")  # just a example, the client doesn't have to be under bot.


@bot.command()
async def supreme(ctx, text: str):
  # Embed
  embed = discord.Embed(title = f"Rendered by {ctx.author}")  # this is a example, everything is optional.
  embed.set_image(url = "attachment://supreme.png")  # attaching file image to embed.
  # Wrapper
  image = await alex_api.supreme(text = text)  # get Image object
  image_bytes = await image.read()  # get io.BytesIO object
    # Sending
    file = discord.File(image_bytes, "supreme.png") # pass io.BytesIO object to discord.File with a filename.
    await ctx.send(embed=embed, file=file) # send both the embed and file, the file will attach to the embed.
    
    # Or ----
    
    # Oneline, because oneline = best
    embed = discord.Embed(title = f"Rendered by {ctx.author}").set_image(url="attachment://supreme.png")
    image = discord.File(await (await alex_api.supreme(text=text)).read(), "supreme.png")
    await ctx.send(embed=embed, file=image)
    
# have this where you close the bot or somewhere to close the session and prevent the "Unclosed client session" warning.
await alex_api.close()

# invoke: !supreme Supreme

bot.run("TOKEN")
```

# Objects

Here is explained what attributes the returned objects have

## Image

The object returned from `alex_api.achievement()`, `alex_api.amiajoke()`, `alex_api.bad()`, `alex_api.calling()`
, `alex_api.captcha()`,
`alex_api.challenge()`, `alex_api.colour_image()`, `alex_api.colour_image_gradient()`, `alex_api.colourify()`
, `alex_api.didyoumean()`,
`alex_api.drake()`, `alex_api.facts()`, `alex_api.filter()`, `alex_api.floor()`, `alex_api.jokeoverhead()`
, `alex_api.pornhub()`,
`alex_api.salty()`, `alex_api.scroll()`, `alex_api.ship()`, `alex_api.supreme()`, `alex_api.trash()`, `alex_api.what()`

#### Image.url

The url of the image

#### await Image.read(bytesio = True)

This will return a [io.BytesIO](https://docs.python.org/3/library/io.html#binary-i-o) object, which can be passed to
discord.File() with a filename for [discord.py](https://github.com/Rapptz/discord.py):

```py
supreme_logo = await alex_api.supreme("ah yes")
supreme_bytes = await supreme_logo.read()  # <_io.BytesIO object at 0x0438DFC8> - BytesIO object.
await ctx.send(file = discord.File(supreme_bytes, filename = "supreme.png"))
```

\
You can set `bytesio` to `False` if you want raw bytes instead of an `io.BytesIO` object.

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

### Colour.rgb

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

## MinecraftIcons

Enum for [`.achievement()`](#await-alex_apiachievementtext-icon--minecrafticonsrandom)
and [`.challenge()`](#await-alex_apichallengetext-icon--minecrafticonsrandom).

#### 1 or grass_block (or grassblock)

Grass Block icon for the achievement or challenge.

#### 2 or diamond

Diamond icon for the achievement or challenge.

#### 3 or diamond_sword (or diamondsword)

Diamond Sword icon for the achievement or challenge.

#### 4 or creeper

Creeper icon for the achievement or challenge.

#### 5 or pig

Pig icon for the achievement or challenge.

#### 6 or tnt

Tnt icon for the achievement or challenge.

#### 7 or cookie

Cookie icon for the achievement or challenge.

#### 8 or heart

Heart icon for the achievement or challenge.

#### 9 or bed

Bed icon for the achievement or challenge.

#### 10 or cake

Cake icon for the achievement or challenge.

#### 11 or sign

Sign icon for the achievement or challenge.

#### 12 or rail

Rail icon for the achievement or challenge.

#### 13 or crafting_bench (or craftingbench)

Crafting Bench icon for the achievement or challenge.

#### 14 or redstone

Redstone icon for the achievement or challenge.

#### 15 or fire

Fire icon for the achievement or challenge.

#### 16 or cobweb

Cobweb icon for the achievement or challenge.

#### 17 or chest

Chest icon for the achievement or challenge.

#### 18 or furnace

Furnace icon for the achievement or challenge.

#### 19 or book

Book icon for the achievement or challenge.

#### 20 or stone_block (or stoneblock)

Stone Block icon for the achievement or challenge.

#### 21 or wooden_plank_block (or woodenplankblock)

Wooden Plank Block icon for the achievement or challenge.

#### 22 or iron_ingot (or ironingot)

Iron Ingot icon for the achievement or challenge.

#### 23 or gold_ingot (or goldingot)

Gold Ingot icon for the achievement or challenge.

#### 24 or wooden_door (or woodendoor)

Wooden Door icon for the achievement or challenge.

#### 25 or iron_door (or irondoor)

Iron Door icon for the achievement or challenge.

#### 26 or diamond_chestplate (or diamondchestplate)

Diamond Chestplate icon for the achievement or challenge.

#### 27 or flint_and_steel (or flintandsteel)

Flint And Steel icon for the achievement or challenge.

#### 28 or glass_bottle (or glassbottle)

Glass Bottle icon for the achievement or challenge.

#### 29 or splash_potion (or splashpotion)

Splash Potion icon for the achievement or challenge.

#### 30 or creeper_spawnegg (or creeperspawnegg)

Creeper Spawnegg icon for the achievement or challenge.

#### 38 or creeperspawnegg

Creeperspawnegg icon for the achievement or challenge.

#### 31 or coal

Coal icon for the achievement or challenge.

#### 32 or iron_sword (or ironsword)

Iron Sword icon for the achievement or challenge.

#### 33 or bow

Bow icon for the achievement or challenge.

#### 34 or arrow

Arrow icon for the achievement or challenge.

#### 35 or iron_chestplate (or ironchestplate)

Iron Chestplate icon for the achievement or challenge.

#### 36 or bucket

Bucket icon for the achievement or challenge.

#### 37 or bucket_with_water (or bucketwithwater)

Bucket With Water icon for the achievement or challenge.

#### 39 or bucket_with_milk (or bucketwithmilk)

Bucket With Milk icon for the achievement or challenge.

#### 40 or diamond_boots (or diamondboots)

Diamond Boots icon for the achievement or challenge.

#### 41 or wooden_hoe (or woodenhoe)

Wooden Hoe icon for the achievement or challenge.

#### 42 or bread

Bread icon for the achievement or challenge.

#### 43 or wooden_sword (or woodensword)

Wooden Sword icon for the achievement or challenge.

#### 44 or bone

Bone icon for the achievement or challenge.

#### 45 or oak_log (or oaklog)

Oak Log icon for the achievement or challenge.

#### 46 or random

Random icon from above for the achievement or challenge.

## Filters

Enum for [`.filter()`](#await-alex_apifiltername-image).

#### 1 or blur

Blur filter.

#### 2 or invert

Invert filter.

#### 3 or b&w or black_and_white

Black and White filter.

#### 4 or deepfry

Deepfry filter.

#### 5 or sepia

Sepia filter.

#### 6 or pixelate

Pixelate filter.

#### 7 or magik

Magik filter.

#### 8 or jpegify

Jpegify filter.

#### 9 or wide

Wide filter.

#### 10 or flip

flip filter.

#### 11 or snow

Snow filter.

#### 12 or gay

Gay filter.

#### 13 or communist

Communist filter.

#### 14 or random

Random filter from above.


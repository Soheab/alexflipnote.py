# AlexFlipnote.py | Docs
An easy to use Python Wrapper for the [AlexFlipnote API](https://api.alexflipnote.dev)\
For any questions and support, you can join the [AlexFlipnote server](https://discord.gg/alexflipnote)

## Getting Started:

To begin with, you'll have to install the package by doing one of the following commands:
- `pip install -U alexflipnote.py`
- `python -m pip -U install alexflipnote.py`
 
After that, you will have to create the client:

```python
import alexflipnote

alex_api = alexflipnote.Client()
```
For future reference in this documentation: when referring to 'alex_api' we refer to that above!
 
  
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

**Available options:** `blur`, `invert`, `b&w`, `deepfry`, `snow`, `gay`, `pixelate`, `jpegify`, `magik`, `communist`
  
**Parameters**:
- name `string` | The filter name, see **Available options**.
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
### await alex_api.facts(text)
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
### await alex_api.steam(profile)
Get someones steam profile.

**Parameters**:
- profile `string` | The user to look for.

**Return type:** [Steam](docs.md#steam "Image object attributes")

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

**Return type**: string or tuple

# Objects
Here is explained what attributes the returned objects have

## Image
The object returned from almost every endpoint.

#### Image.url
The url of the image

#### await Image.read()
This will return BytesIO object, which can be passed to discord.File() 
with a filename. **Here's an example**:
```py
supreme_logo = await alex_api.supreme("ah yes")
supreme_bytes = await supreme_logo.read()
await ctx.send(file=discord.File(cat_bytes, filename="supreme.png"))
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
The object returned from `alex_api.colour()`

#### ColourRGB.all
All RGB values of the colour in a dict 

#### ColourRGB.r
The R values of the colour

#### ColourRGB.g
The G values of the colour

#### ColourRGB.b
The B values of the colour


## Steam
The object returned from `alex_api.steam()`

#### Steam.id
A [SteamID](docs.md#steamid-1 "SteamID object attributes") object

#### Steam.avatars
A [SteamAvatar](docs.md#steamavatar "SteamID object attributes") object

#### Steam.profile
A [SteamProfile](docs.md#steamprofile-1 "SteamID object attributes") object

## SteamID
The object returned from `Steam.id`

#### SteamID.steamid3
The steam id3 of user

#### SteamID.steamid32
The steam id32 of user

#### SteamID.steamid64
The steam id64 of user

#### SteamID.custom_url
The custom url of user


## SteamAvatar
The object returned from `Steam.avatar`

#### SteamAvatar.avatar
The avatar of user

#### SteamAvatar.avatar_medium
The medium version of user's avatar

#### SteamAvatar.avatar_full
The full version of user's avatar


## SteamProfile
The object returned from `Steam.profile`. Some things can be None.

#### SteamProfile.username
The username of user

#### SteamProfile.real_name
The real name of user

#### SteamProfile.summary
A link to user's profile

#### SteamProfile.background
User profile's background

#### SteamProfile.location
User's provided location

#### SteamProfile.privacy
User's privacy type, Public or Private

#### SteamProfile.time_created
Time when user profile was created.

#### SteamProfile.vacbanned
True or False if user is VAC Banned


## Icon
---
The object you pass to the icon param for `alex_api.achievement()` and `alex_api.challenge()`

#### int:

**1:** `grass_block`, **2:** `diamond`, **3:** `diamond_sword`, **4:** `creeper`, **5:** `pig`, \
**6:** `tnt`, **7:** `cookie`, **8:** `heart`, **9:** `bed`, **10:** `cake`, \
**11:** `sign` **12:** `rail` **13:** `crafting_bench` **14:** `redstone`, **15:** `fire`, \
**16:** `cobweb`, **17:** `chest`, **18:** `furnace`, **19:** `book`, **20:** `stone_block`, \
**21:** `wooden_plank_block`, **22:** `iron_ingot`, **23:** `gold_ingot`, **24:** `wooden_door`, **25:** `iron_door`, \
**26:** `diamond_chestplate`, **27:** `flint_and_steel`, **28:** `glass_bottle`, **29:** `splash_potion`, **30:** `creeper_spawnegg`, \
**31:** `coal`, **32:** `iron_sword`, **33:** `bow`, **34:** `arrow`, **35:** `iron_chestplate`, \
**36:** `bucket`, **37:** `bucket_with_water`, **38:** `bucket_with_lava`, **39:** `bucket_with_milk`, **40:** `diamond_boots`, \
**41:** `wooden_hoe`, **42:** `bread`, **43:** `wooden_sword`, **44:** `bone`

#### str:

`grass_block`, `diamond`, `diamond_sword`, `creeper`, `pig`, `tnt`, `cookie`, `heart`, `bed`, `cake`,
`sign`, `rail`, `crafting_bench`, `redstone`, `fire`, `cobweb`, `chest`, `furnace`, `book`, `stone_block`,
`wooden_plank_block`, `iron_ingot`, `gold_ingot`, `wooden_door`, `iron_door`, `diamond_chestplate`, `flint_and_steel`, `glass_bottle`, `splash_potion`, `creeper_spawnegg`,
`coal`, `iron_sword`, `bow`, `arrow`, `iron_chestplate`, `bucket`, `bucket_with_water`, `bucket_with_lava`, `bucket_with_milk`, `diamond_boots`,
`wooden_hoe`, `bread`, `wooden_sword`, `bone`

#### object:

`Icon.grass_block`, `Icon.diamond`, `Icon.diamond_sword`, `Icon.creeper`, `Icon.pig`, `Icon.tnt`,
`Icon.cookie`, `Icon.heart`, `Icon.bed`, `Icon.cake`, `Icon.sign`, `Icon.rail`,
`Icon.crafting_bench`, `Icon.redstone`, `Icon.fire`, `Icon.cobweb`, `Icon.chest`, `Icon.furnace`,
`Icon.book`, `Icon.stone_block`, `Icon.wooden_plank_block`, `Icon.iron_ingot`, `Icon.gold_ingot`, `Icon.wooden_door`,
`Icon.iron_door`, `Icon.diamond_chestplate`, `Icon.flint_and_steel`, `Icon.glass_bottle`, `Icon.splash_potion`, `Icon.creeper_spawnegg`,
`Icon.coal`, `Icon.iron_sword`, `Icon.bow`, `Icon.arrow`, `Icon.iron_chestplate`, `Icon.bucket`,
`Icon.bucket_with_water`, `Icon.bucket_with_lava`, `Icon.bucket_with_milk`, `Icon.diamond_boots`, `Icon.wooden_hoe`, `Icon.bread`,
`Icon.wooden_sword`, `Icon.bone`
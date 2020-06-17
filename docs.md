# AlexFlipnote.py Official Docs

For any questions and support for the wrapper, you can visit the [AlexFlipnote server](https://discord.gg/alexflipnote "AlexFlipnote")
 
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

**Parameters:**\
**- text** `string` - Your text for the achievement.\
**- icon** `integer` - Icon number, 1-39. [See them here](https://i.alexflipnote.dev/9ZXAP35.png)
   
**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.amiajoke(image)

Get an "am i a joke" picture with your image.
  
**Parameters:**\
**- image** `url` - URL of image you want.
   
**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.birb()

Get a random birb picture.

**Return type:** String

---

### await alex_api.calling(text)

Get a calling meme image with your text.

**Parameters:**\
**- text** `string` - Your text for the image.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.captcha(text)

Make a ~~fake~~ captcha with your text.

**Parameters:**\
**- text** `string` - Your text for the image.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.cats()

Get a random cat picture.

**Return type:** String

---

### await alex_api.challenge(text, icon)

Generate a Minecraft challenge with custom text.

**Parameters:**\
**- text** `string` - Your text for the achievement.\
**- icon** `integer` - Icon number.
   
**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.colour(colour)

Get info on provided colour.

**Parameters:**\
**- text** Optional[`string`] - The Colour. Defaults to random colour.

**Aliases**: color

**Return type:** [Colour](docs.md#-colour "Image object attributes")

---

### await alex_api.github_colours()

Get all github colours.

**Return type:** JSON

---

### await alex_api.colour_image(colour)

Get an image of provided colour.

**Parameters:**\
**- text** Optional[`string`] - The Colour. Defaults to random colour.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.colour_image_gradient(colour)

Get an image gradients of provided colour.

**Parameters:**\
**- text** Optional[`string`] - The Colour. Defaults to random colour.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.didyoumean(top, bottom)
---
Get a custom google "Did you mean" suggestion thing.

**Parameters:**\
**- top** `string` - What you search for.\
**- bottom** `string` - The suggested search.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.dogs()

Get a random dog picture.

**Return type:** String

---

### await alex_api.drake(top, bottom)

Make a custom drake meme image.

**Parameters:**\
**- top** `string` - Bad thing.\
**- bottom** `string` - Good thing.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.facts(text)

Get the facts book.

**Parameters:**\
**- text** `url` - The fact.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.filter(name, image)

Put a filter on an image.

**Available options:** `blur`, `invert`, `b&w`, `deepfry`, `snow`, `gay`, `pixelate`, `jpegify`, `magik`, `communist`
  
**Parameters:**\
**- name** `string` - The filter name, see **Available options**.\
**- image** `url` - The image to put the filter on.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.floor(text, image)

Get a "Don't touch the floor" meme with your text and image.

**Parameters:**\
**- text** `string` - The filter name, see **Available options**.\
**- image** Optional[`url`] - The image to put the filter on.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.fml()

Get a random fu*k my life text.

**Return type:** String

---

### await alex_api.jokeoverhead(image)

When da jokes goes over da head.

**Parameters:**\
**- image** `url` - The person's avatar.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.pornhub(text, text2)

Make a custom Pornhub logo!

**Parameters:**\
**- text** `string` - The white part. ~~Porn~~\
**- text2** `string` - The yellow part. ~~Hub~~

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.sadcat()

Get a random sadcat picture.

**Return type:** String

---

### await alex_api.salty(image)

When someone is being salty.

**Parameters:**\
**- image** `url` - The person's avatar.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.facts(text)

Make that scroll meme with your text.

**Parameters:**\
**- text** `url` - The scroll text.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.ship(user, user2)

Ship someone or yourself with someone else.

**Parameters:**\
**- user** `url` - The user's avatar. \
**- user2** `url` - Someone else's avatar.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.steam(profile)

Get someones steam profile.

**Parameters:**\
**- profile** `string` - The user to look for.

**Return type:** [Colour](docs.md#-steam "Image object attributes")

---

### await alex_api.steam(text, dark, light)

Make a custom supreme logo.

**Parameters:**\
**- text** `string` - Text for the logo. \
**- dark** `bool` - Make the background dark. Defaults to False. \
**- light** `bool` - Make the background light. Default to False.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

### await alex_api.trash(face, trash)

Throw someone in the trash bin 🚮

**Parameters:**\
**- face** `url` - Your avatar. \
**- trash** `url` - Someone else's avatar.

**Return type:** [Image](docs.md#-image "Image object attributes")

---

## Objects
Here is explained what attributes the returned objects have


### Image
---
The object returned from `client.get_image()` and `client.get_gif()`

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


### Colour
---
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
A [ColourRGB](docs.md#-colourrgb "ColourRGB object attributes") object

#### Colour.shade
The colour's shades

#### Colour.tint
The colour's tints

---

### ColourRGB
---
The object returned from `alex_api.colour()`

#### ColourRGB.all
All RGB values of the colour in a dict 

#### ColourRGB.r
The R values of the colour

#### ColourRGB.g
The G values of the colour

#### ColourRGB.b
The B values of the colour

---


### Steam
---
The object returned from `alex_api.steam()`

#### Steam.id
A [SteamID](docs.md#-steamid "SteamID object attributes") object

#### Steam.avatars
A [SteamAvatar](docs.md#-steamavatar "SteamID object attributes") object

#### Steam.profile
A [SteamProfile](docs.md#-steamprofile "SteamID object attributes") object

---

### SteamID
---
The object returned from `Steam.id`

#### SteamID.steamid3
The steam id3 of user

#### SteamID.steamid32
The steam id32 of user

#### SteamID.steamid64
The steam id64 of user

#### SteamID.custom_url
The custom url of user

---

### SteamAvatar
---
The object returned from `Steam.avatar`

#### SteamAvatar.avatar
The avatar of user

#### SteamAvatar.avatar_medium
The medium version of user's avatar

#### SteamAvatar.avatar_full
The full version of user's avatar

---

### SteamProfile
---
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
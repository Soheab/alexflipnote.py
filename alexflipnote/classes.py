class Colour:
    __slots__ = ("blackorwhite_text", "brightness", "hex", "image", "image_gradient",
                 "int", "name", "rgb", "rgb_values", "shade", "tint")

    def __init__(self, data):
        self.blackorwhite_text = data.get('blackorwhite_text')
        self.brightness = int(data.get('brightness'))
        self.hex = data.get('hex')
        self.image = data.get('image')
        self.image_gradient = data.get('image_gradient')
        self.int = int(data.get('int'))
        self.name = data.get('name')
        self.rgb = data.get('rgb')
        self.rgb_values = self.ColourRGB(data.get('rgb_values'))
        self.shade = data.get('shade')
        self.tint = data.get('tint')

    class ColourRGB:
        __slots__ = ("all", "r", "g", "b")

        def __init__(self, values):
            self.all = values
            self.r = values.get('r')
            self.g = values.get('g')
            self.b = values.get('b')


class Steam:
    __slots__ = ("id", "avatars", "profile")

    def __init__(self, data):
        self.id = self.SteamID(data.get('id'))
        self.avatars = self.SteamAvatar(data.get('avatars'))
        self.profile = self.SteamProfile(data.get('profile'))

    class SteamID:
        __slots__ = ("steamid3", "steamid32", "steamid64", "custom_url")

        def __init__(self, data):
            self.steamid3 = data.get('steamid3')
            self.steamid32 = data.get('steamid32')
            self.steamid64 = data.get('steamid64')
            self.custom_url = data.get('customurl')

    class SteamAvatar:
        __slots__ = ("avatar_small", "avatar_medium", "avatar_full")

        def __init__(self, data):
            self.avatar_small = data.get('avatar')
            self.avatar_medium = data.get('avatarmedium')
            self.avatar_full = data.get('avatarfull')

    class SteamProfile:
        __slots__ = ("username", "real_name", "url", "summary", "background",
                     "location", "state", "privacy", "time_created", "vacbanned")

        def __init__(self, data):
            self.username = data.get('username')
            self.real_name = data.get('realname')
            self.url = data.get('url')
            self.summary = data.get('summary')
            self.background = data.get('background')
            self.location = data.get('location')
            self.state = data.get('state')
            self.privacy = data.get('privacy')
            self.time_created = data.get('timecreated')
            self.vacbanned = data.get('vacbanned')

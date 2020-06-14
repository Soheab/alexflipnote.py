class SteamUser:
    __slots__ = ("id", "avatars", "profile")

    def __init__(self, data):
        self.id = data.get('id')
        self.avatars = data.get('avatars')
        self.profile = data.get('profile')

    @property
    def steamid3(self):
        return self.id['steamid3']

    @property
    def steamid32(self):
        return self.id['steamid32']

    @property
    def steamid64(self):
        return int(self.id['steamid64'])

    @property
    def custom_url(self):
        return self.id['customurl']

    @property
    def avatar(self):
        return self.id['avatar']

    @property
    def avatar_medium(self):
        return self.id['avatarmedium']

    @property
    def avatar_full(self):
        return self.id['avatarfull']

    @property
    def username(self):
        return self.profile['username']

    @property
    def real_name(self):
        return self.profile['realname']

    @property
    def url(self):
        return self.profile['url']

    @property
    def summary(self):
        return self.profile['summary']

    @property
    def background(self):
        return self.profile['background']

    @property
    def location(self):
        return self.profile['location']

    @property
    def state(self):
        return self.profile['state']

    @property
    def privacy(self):
        return self.profile['privacy']

    @property
    def created_at(self):
        return self.profile['timecreated']

    @property
    def vac_banned(self):
        return self.profile['vacbanned']

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
        self.rgb_values = data.get('rgb_values')
        self.shade = data.get('shade')
        self.tint = data.get('tint')

class PixleyPixels(object):
    def __init__(self, neopixels):
        self.neopixels = neopixels
        self.set_home_pixels(16, 0)

    def blank(self):
        for i in range(self.neopixels.n):
            self.neopixels[i] = (0, 0, 0)
        self.neopixels.show()

    def light(self, pixels, colour):
        if type(pixels) == tuple:
            x = []
            for i in range(pixels[0], pixels[1] + 1):
                x.append(i)
            pixels = x

        if not type(pixels) == list:
            pixels = [pixels]

        for p in pixels:
            self.neopixels[p % self.neopixels.n] = colour

    def show(self):
        self.neopixels.show()

    def light_all(self, colour):
        self.light(list(range(32)), colour)
        self.show()

    def set_home_pixels(self, left, right):
        self.left_home = left
        self.right_home = right

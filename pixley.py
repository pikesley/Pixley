def blank(neopixels, display = False):
    for i in range(neopixels.n):
        neopixels[i] = (0, 0, 0)
    if display: neopixels.show()

def light(neopixels, pixels, colour):
    if type(pixels) == tuple:
        x = []
        for i in range(pixels[0], pixels[1] + 1):
            x.append(i)
        pixels = x

    if not type(pixels) == list:
        pixels = [pixels]

    for p in pixels:
        neopixels[p % neopixels.n] = colour

class WavePosition:
    position = 0

    @classmethod
    def increment(cls, limit):
        cls.position = cls.position + 1
        if cls.position == limit:
            cls.position = 0

    @classmethod
    def reset(cls):
        cls.position = 0

def wave(neopixels, colour):
    light(neopixels, (0, 11), fractional_colour(colour, 0.1))
    light(neopixels, [WavePosition.position, neopixels.n - (WavePosition.position + 1)], colour)

    WavePosition.increment(neopixels.n / 2)

def fractional_colour(colour, proportion):
    return tuple(map(lambda x: int(x * proportion), colour))

def knight_rider_sequence(count):
    offset = 4

    tops = []
    for i in range(count / 4):
        tops.append(i + offset)

    bottoms = []
    for i in range(count / 4, 0, -1):
        v = i - offset - 1
        if v < 0:
            v = (count / 2) + v
        bottoms.append(v)

    for i in range(count / 4):
        tops.append(i + offset + (count / 2))

    for i in range(count / 4, 0, -1):
        v = (i - offset - 1) + count / 2
        if v < count / 2:
            v = (count / 2) + v
        bottoms.append(v)

    seq = []
    for i in range(count / 2):
        seq.append((tops[i], bottoms[i]))

    return seq

# def wheel(pos):
#     # Input a value 0 to 255 to get a color value.
#     # The colours are a transition r - g - b - back to r.
#     if (pos < 0):
#         return (0, 0, 0)
#     if (pos > 255):
#         return (0, 0, 0)
#     if (pos < 85):
#         return (int(pos * 3), int(255 - (pos*3)), 0)
#     elif (pos < 170):
#         pos -= 85
#         return (int(255 - pos*3), 0, int(pos*3))
#     else:
#         pos -= 170
#         return (0, int(pos*3), int(255 - pos*3))

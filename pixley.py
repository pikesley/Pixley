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

def wave(neopixels, colour):
    light(neopixels, (0, 11), fractional_colour(colour, 0.25))
    light(neopixels, [WavePosition.position, neopixels.n - (WavePosition.position + 1)], colour)

    WavePosition.position = WavePosition.position + 1

def fractional_colour(colour, proportion):
    return tuple(map(lambda x: int(x * proportion), colour))

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

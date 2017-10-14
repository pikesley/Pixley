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

def blank(neopixels, display = False):
    for i in range(neopixels.n):
        neopixels[i] = (0, 0, 0)
    if display: neopixels.show()

def light(neopixels, pixels, colour):
    for p in pixels:
        neopixels[p] = colour

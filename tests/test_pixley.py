import pytest
from pixley import *

def test_blank():
    neopixels = FakePixels(12)
    blank(neopixels)

    for i in range(12):
        assert(neopixels[i]) == (0, 0, 0)

def test_light():
    neopixels = FakePixels(12)
    light(neopixels, [5, 7], (255, 0, 0))

    assert neopixels == [
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (255, 0, 0), (0, 0, 0), (255, 0, 0),
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
    ]

def test_light_different_colours():
    neopixels = FakePixels(12)
    light(neopixels, 1, (0, 0, 255))
    light(neopixels, 7, (0, 255, 255))

    assert neopixels == [
        (0, 0, 0), (0, 0, 255), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 255),
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
    ]

class FakePixels(list):
    def __init__(self, n):
        self.n = n
        for i in range(n):
            self.append((0, 0, 0))

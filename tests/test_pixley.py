import pytest
from helpers import *
# from pixley import *

from Pixley.pixley_pixels import PixleyPixels

class TestPixleyPixels:
    def test_blank(self):
        neopixels = FakePixels(12)
        pp = PixleyPixels(neopixels)

        for i in range(12):
            assert(pp[i]) == (0, 0, 0)


    def test_light(self):
        pp = PixleyPixels(FakePixels(12))
        pp.light([5, 7], (255, 0, 0))

        assert pp.neopixels == [
            (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
            (0, 0, 0), (255, 0, 0), (0, 0, 0), (255, 0, 0),
            (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
        ]

    def test_light_overflow(self):
        pp = PixleyPixels(FakePixels(12))
        pp.light(14, (255, 255, 255))
        assert pp.neopixels[2] == (255, 255, 255)

    def test_light_different_colours(self):
        pp = PixleyPixels(FakePixels(12))
        pp.light(1, (0, 0, 255))
        pp.light(7, (0, 255, 255))

        assert pp.neopixels == [
            (0, 0, 0), (0, 0, 255), (0, 0, 0), (0, 0, 0),
            (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 255),
            (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
        ]

    def test_light_range(self):
        pp = PixleyPixels(FakePixels(12))
        pp.light((3, 6), (0, 127, 0))
        assert pp.neopixels == [
            (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 127, 0),
            (0, 127, 0), (0, 127, 0), (0, 127, 0), (0, 0, 0),
            (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
        ]

#
# def test_fractional_colour():
#     assert fractional_colour((255, 255, 255), 0.5) == (127, 127, 127)
#     assert fractional_colour((255, 0, 255), 0.5) == (127, 0, 127)

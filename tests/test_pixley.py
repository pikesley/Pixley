import pytest
from helpers import *

from Pixley.pixley import Pixley

class TestPixley:
    def test_blank(self):
        neopixels = FakePixels(12)
        pix = Pixley(neopixels)

        for i in range(12):
            assert(pix[i]) == (0, 0, 0)


    def test_light(self):
        pix = Pixley(FakePixels(12))
        pix.light([5, 7], (255, 0, 0))

        assert pix.neopixels == [
            (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
            (0, 0, 0), (255, 0, 0), (0, 0, 0), (255, 0, 0),
            (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
        ]

    def test_light_overflow(self):
        pix = Pixley(FakePixels(12))
        pix.light(14, (255, 255, 255))
        assert pix.neopixels[2] == (255, 255, 255)

    def test_light_different_colours(self):
        pix = Pixley(FakePixels(12))
        pix.light(1, (0, 0, 255))
        pix.light(7, (0, 255, 255))

        assert pix.neopixels == [
            (0, 0, 0), (0, 0, 255), (0, 0, 0), (0, 0, 0),
            (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 255),
            (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
        ]

    def test_light_range(self):
        pix = Pixley(FakePixels(12))
        pix.light((3, 6), (0, 127, 0))
        assert pix.neopixels == [
            (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 127, 0),
            (0, 127, 0), (0, 127, 0), (0, 127, 0), (0, 0, 0),
            (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
        ]

#
# def test_fractional_colour():
#     assert fractional_colour((255, 255, 255), 0.5) == (127, 127, 127)
#     assert fractional_colour((255, 0, 255), 0.5) == (127, 0, 127)

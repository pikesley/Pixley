import pytest
from helpers import *
from Pixley.patterns.pac_man import PacMan

def test_sequence():
    neopixels = FakePixels(32)
    pm = PacMan(neopixels)

    assert pm.sequence() == [
        {
            "on": [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
            "off": []
        },
        {
            "on": [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            "off": [16, 31]
        },
        {
            "on": [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
            "off": [16, 17, 30, 31]
        },
        {
            "on": [19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
            "off": [16, 17, 18, 29, 30, 31]
        },
        {
            "on": [20, 21, 22, 23, 24, 25, 26, 27],
            "off": [16, 17, 18, 19, 28, 29, 30, 31]
        },
    ]

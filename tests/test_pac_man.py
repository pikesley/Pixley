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
            "on": [16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
            "off": [20, 21]
        },
        {
            "on": [16, 17, 18, 23, 24, 25, 26, 27, 28, 29, 30, 31],
            "off": [19, 20, 21, 22]
        },
        {
            "on": [16, 17, 24, 25, 26, 27, 28, 29, 30, 31],
            "off": [18, 19, 20, 21, 22, 23]
        },
        {
            "on": [16, 25, 26, 27, 28, 29, 30, 31],
            "off": [17, 18, 19, 20, 21, 22, 23, 24]
        }
    ]

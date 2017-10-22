import pytest
from helpers import *
from Pixley.patterns.knight_rider import KnightRider

def test_sequence():
    neopixels = FakePixels(32)
    kr = KnightRider(neopixels)

    assert kr.sequence() == [
        [ 4,  3],
        [ 5,  2],
        [ 6,  1],
        [ 7,  0],
        [ 8, 15],
        [ 9, 14],
        [10, 13],
        [11, 12],

        [20, 19],
        [21, 18],
        [22, 17],
        [23, 16],
        [24, 31],
        [25, 30],
        [26, 29],
        [27, 28]
    ]

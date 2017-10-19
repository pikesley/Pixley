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

def test_light_overflow():
    neopixels = FakePixels(12)
    light(neopixels, 14, (255, 255, 255))
    assert neopixels[2] == (255, 255, 255)

def test_light_different_colours():
    neopixels = FakePixels(12)
    light(neopixels, 1, (0, 0, 255))
    light(neopixels, 7, (0, 255, 255))

    assert neopixels == [
        (0, 0, 0), (0, 0, 255), (0, 0, 0), (0, 0, 0),
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 255, 255),
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
    ]

def test_light_range():
    neopixels = FakePixels(12)
    light(neopixels, (3, 6), (0, 127, 0))
    assert neopixels == [
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 127, 0),
        (0, 127, 0), (0, 127, 0), (0, 127, 0), (0, 0, 0),
        (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
    ]

def test_wave():
    neopixels = FakePixels(12)

    wave(neopixels, (255, 0, 0))
    assert neopixels == [
        (255, 0, 0), (25, 0, 0), (25, 0, 0), (25, 0, 0),
        (25, 0, 0), (25, 0, 0), (25, 0, 0), (25, 0, 0),
        (25, 0, 0), (25, 0, 0), (25, 0, 0), (255, 0, 0)
    ]

    wave(neopixels, (255, 0, 0))
    assert neopixels == [
        (25, 0, 0), (255, 0, 0), (25, 0, 0), (25, 0, 0),
        (25, 0, 0), (25, 0, 0), (25, 0, 0), (25, 0, 0),
        (25, 0, 0), (25, 0, 0), (255, 0, 0), (25, 0, 0)
    ]

def test_wave_position():
    WavePosition.reset()
    assert WavePosition.position == 0

    for i in range(6):
        WavePosition.increment(6)

    assert WavePosition.position == 0

def test_fractional_colour():
    assert fractional_colour((255, 255, 255), 0.5) == (127, 127, 127)
    assert fractional_colour((255, 0, 255), 0.5) == (127, 0, 127)

def test_knight_rider_sequence():
    assert knight_rider_sequence(32) == [
        ( 4,  3),
        ( 5,  2),
        ( 6,  1),
        ( 7,  0),
        ( 8, 15),
        ( 9, 14),
        (10, 13),
        (11, 12),

        (20, 19),
        (21, 18),
        (22, 17),
        (23, 16),
        (24, 31),
        (25, 30),
        (26, 29),
        (27, 28)
    ]
################################################################################

class FakePixels(list):
    def __init__(self, n):
        self.n = n
        for i in range(n):
            self.append((0, 0, 0))

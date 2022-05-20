import pytest
import numpy as np
from day_06_2015 import ChristmasLights, ChristmasLights2


@pytest.fixture
def test_grid():
    return np.zeros([10, 10], dtype=int)


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("turn on 0,0 through 9,9", 100),
        (
            """turn on 0,0 through 9,9
         turn off 0,0 through 9,9""",
            0,
        ),
        (
            """turn on 0,0 through 9,9
         turn off 0,0 through 9,9
         toggle 4,4 through 5,5""",
            4,
        ),
    ],
)
def test_christmas_lights_01(arg, expected):
    lights = ChristmasLights(10, arg)
    lights.follow_instructions()
    assert lights.lights_on == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("turn on 0,0 through 0,0", 1),
        (
            """turn on 0,0 through 9,9
         turn off 0,0 through 0,0""",
            99,
        ),
        (
            """turn on 0,0 through 9,9
         turn off 0,0 through 0,0
         toggle 4,4 through 5,5""",
            107,
        ),
    ],
)
def test_christmas_lights_02(arg, expected):
    lights = ChristmasLights2(10, arg)
    lights.follow_instructions()
    assert lights.lights_on == expected

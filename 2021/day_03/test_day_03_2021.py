import pytest
import pandas as pd
from day_03_2021 import get_power, get_life_support

data = [
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
]

df = pd.DataFrame(data)


@pytest.mark.parametrize(
    "input, expected",
    [
        (df, 198),
    ],
)
def test_get_power(input, expected):
    assert get_power(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (df, 230),
    ],
)
def test_get_life_support(input, expected):
    assert get_life_support(input) == expected

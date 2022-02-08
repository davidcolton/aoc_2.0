import pytest
from day_01_2017 import captcha


@pytest.mark.parametrize(
    "arg, expected",
    [
        ([1, 1, 2, 2], 3),
        ([1, 1, 1, 1], 4),
        ([1, 2, 3, 4], 0),
        ([9, 1, 2, 1, 2, 1, 2, 9], 9),
    ],
)
def test_captcha(arg, expected):
    assert captcha(arg) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        ([1, 2, 1, 2], 6),
        ([1, 2, 2, 1], 0),
        ([1, 2, 3, 4, 2, 5], 4),
        ([1, 2, 3, 1, 2, 3], 12),
        ([1, 2, 1, 3, 1, 4, 1, 5], 4),
    ],
)
def test_captcha(arg, expected):
    assert captcha(arg, half=True) == expected

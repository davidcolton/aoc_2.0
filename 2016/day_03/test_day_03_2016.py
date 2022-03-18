import pytest
from day_03_2016 import is_triangle


@pytest.mark.parametrize(
    "arg, expected",
    [
        ([1, 2, 3], 0),
        ([2, 2, 6], 0),
        ([2, 2, 3], 1),
        ([2, 3, 4], 1),
        ([4, 4, 2], 1),
    ],
)
def test_is_triangle(arg, expected):
    assert is_triangle(arg) == expected

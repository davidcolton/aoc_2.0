import pytest
from day_02_2017 import checksum, evenly_divisible_values


@pytest.mark.parametrize(
    "arg, expected",
    [
        (
            [
                [5, 1, 9, 5],
                [7, 5, 3],
                [2, 4, 6, 8],
            ],
            18,
        ),
    ],
)
def test_checksum(arg, expected):
    assert checksum(arg) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (
            [
                [5, 9, 2, 8],
                [9, 4, 7, 3],
                [3, 8, 6, 5],
            ],
            9,
        ),
    ],
)
def test_evenly_divisible_values(arg, expected):
    assert evenly_divisible_values(arg) == expected

import pytest
from day_01_2018 import frequency


@pytest.mark.parametrize(
    "arg, expected",
    [([1, -2, 3, 1], 3)],
)
def test_frequency(arg, expected):
    assert frequency(arg) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (([1, -2, 3, 1], 2)),
        (([-1, 1], 0)),
        (([3, 3, 4, -2, -4], 10)),
        (([-6, 3, 8, 5, -6], 5)),
        (([7, 7, -2, -7, -4], 14)),
    ],
)
def test_frequency_duplicate(arg, expected):
    assert frequency(arg, duplicate=True) == expected

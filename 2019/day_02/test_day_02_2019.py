import pytest
from day_02_2019 import intcode


@pytest.mark.parametrize(
    "arg, expected",
    [
        ([1, 0, 0, 0, 99], 2),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], 30),
        ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 3500),
    ],
)
def test_int_code(arg, expected):
    assert expected == intcode(arg, arg[1], arg[2])

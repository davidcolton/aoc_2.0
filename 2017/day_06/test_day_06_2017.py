import pytest
from day_06_2017 import redistribution_cycles


@pytest.mark.parametrize(
    "arg, expected",
    [
        ([0, 2, 7, 0], 5),
        ([2, 4, 1, 2], 4),
    ],
)
def test_redistribution_cycless(arg, expected):
    assert redistribution_cycles(arg) == expected

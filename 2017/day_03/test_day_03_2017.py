import pytest
from day_03_2017 import manhattan_distance


@pytest.mark.parametrize(
    "arg, expected",
    [(1, 1), (12, 3), (23, 2), (1024, 31)],
)
def test_checksum(arg, expected):
    assert manhattan_distance(arg) == expected

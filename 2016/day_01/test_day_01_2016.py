import pytest
from day_01_2016 import StreetGrid


@pytest.mark.parametrize(
    "arg, expected",
    [
        (["R2", "L3"], 5),
        (["R2", "R2", "R2"], 2),
        (["R5", "L5", "R5", "R3"], 12),
    ],
)
def test_shortest_path(arg, expected):
    santa = StreetGrid(arg)
    assert santa.shortest_path() == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (["R8", "R4", "R4", "R8"], 4),
    ],
)
def test_visited_twice(arg, expected):
    santa = StreetGrid(arg)
    assert santa.shortest_path(visited_twice=True) == expected

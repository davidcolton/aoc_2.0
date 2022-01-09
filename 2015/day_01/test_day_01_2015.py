import pytest
from day_01_2015 import Floor


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("(())", 0),
        ("()()", 0),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("))(", -1),
        (")())())", -3),
    ],
)
def test_santa_floor(arg, expected):
    santa = Floor(arg)
    assert santa.final_floor == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (")", 1),
        ("()())((())))", 5),
        ("()()()(()))())())", 11),
    ],
)
def test_santa_basement(arg, expected):
    santa = Floor(arg)
    assert santa.first_basement_visit == expected

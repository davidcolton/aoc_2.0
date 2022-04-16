import pytest
from day_05_2015 import SantasList, SantasListTwo


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("ugknbfddgicrmopn", 1),
        ("aaa", 1),
        ("jchzalrnumimnmhp", 0),
        ("haegwjzuvuyypxyu", 0),
        ("dvszwmarrgswjxmb", 0),
    ],
)
def test_naughty_or_nice_first(arg, expected):
    santas_list = SantasList(arg)
    santas_list.naught_or_nice()
    assert santas_list.length_nice_list == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("qjhvhtzxzqqjkmpb", 1),
        ("xxyxx", 1),
        ("uurcxstgmygtbstg", 0),
        ("ieodomkazucvgmuy", 0),
    ],
)
def test_naughty_or_nice_second(arg, expected):
    santas_list = SantasListTwo(arg)
    santas_list.naught_or_nice()
    assert santas_list.length_nice_list == expected

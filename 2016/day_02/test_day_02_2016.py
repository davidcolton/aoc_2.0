import pytest
from day_02_2016 import keypad, enter_keycode, complex_keypad


@pytest.mark.parametrize(
    "arg, expected",
    [
        (["ULL", "RRDDD", "LURDL", "UUUUD"], "1985"),
    ],
)
def test_keypad(arg, expected):
    assert enter_keycode(arg, keypad) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (["ULL", "RRDDD", "LURDL", "UUUUD"], "5DB3"),
    ],
)
def test_complex_keypad(arg, expected):
    assert enter_keycode(arg, complex_keypad) == expected

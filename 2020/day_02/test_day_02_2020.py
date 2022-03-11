import pytest
from day_02_2020 import password_checker
from day_02_2020 import positional_password_checker


@pytest.mark.parametrize(
    "password_list, expected",
    [
        (["2-4 v: vqdn", "8-12 t: thllsbqtgdsf", "10-17 h: vpbrjcbhnwqhhphxjk"], 0),
        (["3-8 s: sssssssbs", "6-9 w: wwwwwcwwww", "5-10 r: rvwrrlxbrjhp"], 2),
    ],
)
def test_password_checker(password_list, expected):
    assert password_checker(password_list) == expected


@pytest.mark.parametrize(
    "password_list, expected",
    [
        (["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"], 1),
    ],
)
def test_positional_password_checker(password_list, expected):
    assert positional_password_checker(password_list) == expected

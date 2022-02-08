import pytest
from day_01_2021 import examine_sonar


@pytest.mark.parametrize(
    "input, window, expected",
    [
        ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 1, 7),
        ([199, 200, 208, 210, 240, 269], 1, 5),
        ([199, 100, 95, 80], 1, 0),
        ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 3, 5),
        ([199, 200, 208, 210, 240, 269], 3, 3),
        ([199, 100, 95, 80], 3, 0),
    ],
)
def test_examine_sonar(input, window, expected):
    assert examine_sonar(input, window) == expected

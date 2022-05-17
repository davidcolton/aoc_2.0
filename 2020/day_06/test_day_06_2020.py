import pytest
from day_06_2020 import total_yes_answers, everyone_answered_yes

test_01 = """abc

a
b
c

ab
ac

a
a
a
a

b"""

test_02 = """abc

a
b
c

ab
ac

a
a
a
a

b"""


@pytest.mark.parametrize(
    "input, expected",
    [
        (test_01, 11),
    ],
)
def test_total_yes_answers(input, expected):
    assert total_yes_answers(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (test_02, 6),
    ],
)
def test_everyone_answered_yes(input, expected):
    assert everyone_answered_yes(input) == expected

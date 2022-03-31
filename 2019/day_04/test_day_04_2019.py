import pytest
from day_04_2019 import rule_01, rule_02, rule_03


@pytest.mark.parametrize(
    "arg, exp",
    [
        ([1, 1, 1, 1, 1, 1], True),
        ([1, 2, 2, 3, 4, 5], True),
        ([2, 2, 3, 4, 5, 0], True),
        ([1, 2, 3, 7, 8, 9], False),
        ([5, 6, 7, 8, 9, 0], False),
    ],
)
def test_rule_01(arg, exp):
    assert rule_01(arg) == exp


@pytest.mark.parametrize(
    "arg, exp",
    [
        ([1, 1, 1, 1, 1, 1], True),
        ([1, 2, 2, 3, 4, 5], True),
        ([2, 2, 3, 4, 5, 0], False),
        ([1, 2, 3, 7, 8, 9], True),
        ([5, 6, 7, 8, 9, 0], False),
    ],
)
def test_rule_02(arg, exp):
    assert rule_02(arg) == exp


@pytest.mark.parametrize(
    "arg, exp",
    [
        ([1, 1, 2, 2, 3, 3], True),
        ([1, 2, 3, 4, 4, 4], False),
        ([1, 1, 1, 1, 2, 2], True),
    ],
)
def test_rule_03(arg, exp):
    assert rule_03(arg) == exp

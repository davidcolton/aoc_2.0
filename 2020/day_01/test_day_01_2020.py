import pytest
import numpy as np
from day_01_2020 import fix_expenses


@pytest.mark.parametrize(
    "target, count, report, expected",
    [
        (16, 2, [2, 4, 6, 8, 10], 60),
        (23, 3, [2, 4, 6, 7, 8, 10], 420),
        (99, 2, [2, 4, 6, 7, 8, 10], None),
    ],
)
def test_fix_expenses(target, count, report, expected):
    assert fix_expenses(target, count, report) == expected

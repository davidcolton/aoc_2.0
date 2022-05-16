import pytest
import numpy as np
from day_06_2021 import evolve, intelligent_evolution


input = "3,4,3,1,2"
data = [int(n) for n in input.split(",")]
arr = np.array(data)


@pytest.mark.parametrize(
    "input, days, expected",
    [
        (arr, 18, 26),
        (arr, 80, 5934),
    ],
)
def test_evolve(input, days, expected):
    assert evolve(input, days) == expected


@pytest.mark.parametrize(
    "input, days, expected",
    [
        (data, 18, 26),
        (data, 80, 5934),
    ],
)
def test_intelligent_evolution(input, days, expected):
    assert intelligent_evolution(input, days) == expected

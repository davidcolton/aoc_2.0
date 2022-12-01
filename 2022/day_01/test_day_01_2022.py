import pytest
from day_01_2022 import most_calories, top_three

test_data = [
    [1000, 2000, 3000],
    [4000],
    [5000, 6000],
    [7000, 8000, 9000],
    [10000]
]


@pytest.mark.parametrize(
    "input, expected",
    [
        (test_data, 24000),
    ],
)
def test_most_calories(input, expected):
    assert most_calories(input) == expected

@pytest.mark.parametrize(
    "input, expected",
    [
        (test_data, 45000),
    ],
)
def test_top_three(input, expected):
    assert top_three(input) == expected
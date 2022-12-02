import pytest
from day_02_2022 import blind_strategy, real_strategy

test_data = [
    'A Y', 'B X', 'C Z'
]


@pytest.mark.parametrize(
    "input, expected",
    [
        (test_data, 15),
    ],
)
def test_blind_strategy(input, expected):
    assert blind_strategy(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (test_data, 12),
    ],
)
def test_real_strategy(input, expected):
    assert real_strategy(input) == expected
import pytest
from day_02_2021 import calculate_position
from day_02_2021 import calculate_position_with_aim


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            [
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2",
            ],
            150,
        ),
    ],
)
def test_calculate_position(input, expected):
    assert calculate_position(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            [
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2",
            ],
            900,
        ),
    ],
)
def test_calculate_position_with_aim(input, expected):
    assert calculate_position_with_aim(input) == expected

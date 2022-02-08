import pytest
from day_01_2019 import calculate_fuel, calculate_fuel_complex


@pytest.mark.parametrize(
    "arg, expected",
    [
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583),
    ],
)
def test_calculate_fuel(arg, expected):
    assert calculate_fuel(arg) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (1969, 966),
        (100756, 50346),
    ],
)
def test_calculate_fuel_complex(arg, expected):
    assert calculate_fuel_complex(arg) == expected

import pytest
from day_01_2022 import calibrate_values, find_numbers


@pytest.mark.parametrize(
    "input, expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
        ("abcdefg", 0),
    ],
)
def test_calibrate_values(input, expected):
    assert calibrate_values(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen",76),
        ("9986fmfqhdmq8", 98)
    ],
)
def test_find_numbers(input, expected):
    assert find_numbers(input) == expected

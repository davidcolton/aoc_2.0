import pytest
from day_05_2016 import calculate_matching_hash, positional_passowrd

hash_root = "wtnhxymk"


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("abc", "18f47a30"),
    ],
)
def test_calculate_matching_hash(arg, expected):
    assert calculate_matching_hash(arg, 5) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("abc", "05ace8e3"),
    ],
)
def test_positional_passowrd(arg, expected):
    assert positional_passowrd(arg, 5) == expected

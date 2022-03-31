import pytest
from day_04_2015 import calculate_matching_hash


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("abcdef", 609043),
        ("pqrstuv", 1048970),
    ],
)
def test_calculate_matching_hash(arg, expected):
    assert calculate_matching_hash(arg, 5) == expected

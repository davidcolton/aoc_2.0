import pytest
from day_05_2018 import (
    replacement_strings,
    polymer_reactions,
    single_polymer_reaction,
)


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("dabAcCaCBAcCcaDA", 10),
    ],
)
def test_polymer_reactions(arg, expected):
    assert polymer_reactions(arg, replacement_strings) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("dabAcCaCBAcCcaDA", 4),
    ],
)
def test_single_polymer_reaction(arg, expected):
    assert single_polymer_reaction(arg, replacement_strings) == expected

import pytest
from day_03_2022 import sum_of_priorities, elf_priorities

test_data = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


@pytest.mark.parametrize(
    "input, expected",
    [
        (test_data, 157),
    ],
)
def test_sum_of_priorities(input, expected):
    assert sum_of_priorities(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (test_data, 70),
    ],
)
def test_elf_priorities(input, expected):
    assert elf_priorities(input) == expected

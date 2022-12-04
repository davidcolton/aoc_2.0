import pytest
from day_04_2022 import assignments_overlap

test_data = [
    [(2, 4), (6, 8)],
    [(2, 3), (4, 5)],
    [(5, 7), (7, 9)],
    [(2, 8), (3, 7)],
    [(6, 6), (4, 6)],
    [(2, 6), (4, 8)],
]


@pytest.mark.parametrize(
    "input, type, expected",
    [(test_data, "contained", 2), (test_data, "overlap", 4)],
)
def test_assignments_overlap(input, type, expected):
    assert assignments_overlap(input, type) == expected

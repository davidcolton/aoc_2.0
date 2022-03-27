import pytest
from day_03_2018 import generate_coords_counter, no_overlap


@pytest.mark.parametrize(
    "arg, expected",
    [
        (
            [
                "#1 @ 1,3: 4x4",
                "#2 @ 3,1: 4x4",
                "#3 @ 5,5: 2x2",
            ],
            4,
        ),
    ],
)
def test_multiple_claims(arg, expected):
    all_coords = generate_coords_counter(arg)
    two_claims = {k: v for k, v in all_coords.items() if v > 1}
    assert len(two_claims) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (
            [
                "#1 @ 1,3: 4x4",
                "#2 @ 3,1: 4x4",
                "#3 @ 5,5: 2x2",
            ],
            "#3",
        ),
    ],
)
def test_unique_claim(arg, expected):
    all_coords = generate_coords_counter(arg)
    unique_claim = no_overlap(arg, all_coords)
    assert unique_claim == expected

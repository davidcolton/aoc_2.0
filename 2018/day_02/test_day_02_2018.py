import pytest
from day_02_2018 import checksum, common_letters


@pytest.mark.parametrize(
    "arg, expected",
    [
        (
            [
                "abcdef",
                "bababc",
                "abbcde",
                "abcccd",
                "aabcdd",
                "abcdee",
                "ababab",
            ],
            12,
        ),
    ],
)
def test_checksum(arg, expected):
    assert checksum(arg) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (
            [
                "abcde",
                "fghij",
                "klmno",
                "pqrst",
                "fguij",
                "axcye",
                "wvxyz",
            ],
            "fgij",
        ),
    ],
)
def test_common_letters(arg, expected):
    assert common_letters(arg) == expected

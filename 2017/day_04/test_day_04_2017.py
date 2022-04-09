import pytest
from day_04_2017 import simple_pass_phrases, complex_pass_phrases

data_01 = [
    "aa bb cc dd ee",
    "aa bb cc dd aa",
    "aa bb cc dd aaa",
]
data_02 = [
    "abcde fghij",
    "abcde xyz ecdab",
    "a ab abc abd abf abj",
    "iiii oiii ooii oooi oooo",
    "oiii ioii iioi iiio",
]


@pytest.mark.parametrize(
    "arg, expected",
    [
        (data_01, 2),
    ],
)
def test_simple_pass_phrases(arg, expected):
    assert simple_pass_phrases(arg) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (data_02, 3),
    ],
)
def test_complex_pass_phrases(arg, expected):
    assert complex_pass_phrases(arg) == expected

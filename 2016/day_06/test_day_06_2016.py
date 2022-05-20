import pytest
from day_06_2016 import error_corrected_message

input = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""

input_lst = [word for word in input.split("\n")]
data = [list(word) for word in input_lst]


@pytest.mark.parametrize(
    "arg, expected_01, expected_02",
    [
        (data, "easter", "advent"),
    ],
)
def test_error_corrected_message(arg, expected_01, expected_02):
    mc, lc = error_corrected_message(arg)
    assert mc == expected_01
    assert lc == expected_02

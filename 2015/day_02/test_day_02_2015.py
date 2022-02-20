import pytest
from day_02_2015 import Presents, Present


@pytest.mark.parametrize("arg, expected", [("2x3x4", 58), ("1x1x10", 43)])
def test_calculate_wrapping_paper(arg, expected):
    present = Present(arg)
    assert present.calculate_wrapping_paper == expected


@pytest.mark.parametrize("arg, expected", [("2x3x4", 34), ("1x1x10", 14)])
def test_calculate_ribbon(arg, expected):
    present = Present(arg)
    assert present.calculate_ribbon == expected


@pytest.mark.parametrize("arg, expected", [("2x3x4\n1x1x10", 101)])
def test_wrap_all_presents(arg, expected):
    presents = Presents(arg)
    assert presents.wrap_all_presents == expected


@pytest.mark.parametrize("arg, expected", [("2x3x4\n1x1x10", 48)])
def test_ribbon_all_presents(arg, expected):
    presents = Presents(arg)
    assert presents.ribbon_all_presents == expected

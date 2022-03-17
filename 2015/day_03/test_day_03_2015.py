import pytest
from day_03_2015 import DeliveryRoute


@pytest.mark.parametrize(
    "arg, expected",
    [
        (">", 2),
        ("^>v<", 4),
        ("^v^v^v^v^v", 2),
    ],
)
def test_houses_delivered(arg, expected):
    route = DeliveryRoute(arg)
    route.follow_route()
    assert route.houses_visited == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (["^v", 2], 3),
        (["^>v<", 2], 3),
        (["^v^v^v^v^v", 2], 11),
    ],
)
def test_houses_delivered_two_santas(arg, expected):
    route = DeliveryRoute(arg[0], arg[1])
    route.follow_route()
    assert route.houses_visited == expected

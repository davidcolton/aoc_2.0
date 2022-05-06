import pytest
from day_05_2017 import process_maze_steps

data = [0, 3, 0, 1, -3]
data_02 = [0, 3, 0, 1, -3]


@pytest.mark.parametrize(
    "arg, expected",
    [
        (data, 5),
    ],
)
def test_process_maze_steps(arg, expected):
    assert process_maze_steps(arg) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (data_02, 10),
    ],
)
def test_process_maze_steps_part02(arg, expected):
    assert process_maze_steps(arg, part=2) == expected

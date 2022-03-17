import pytest
import numpy as np
from day_03_2020 import tree_counter

data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split(
    "\n"
)


@pytest.mark.parametrize(
    "data, right, down, expected",
    [
        (data, 1, 1, 2),
        (data, 3, 1, 7),
        (data, 5, 1, 3),
        (data, 7, 1, 4),
        (data, 1, 2, 2),
    ],
)
def test_count_tree_hit(data, right, down, expected):
    assert tree_counter(data, right, down) == expected

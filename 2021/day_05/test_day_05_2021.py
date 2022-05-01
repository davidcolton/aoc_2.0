import pytest
import numpy as np
from day_05_2021 import Point, Line, process_lines, process_point

input = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

data = [process_point(point) for point in input.strip().split("\n")]


@pytest.mark.parametrize(
    "input, size, diags, expected",
    [
        (data, 10, False, 5),
        (data, 10, True, 12),
    ],
)
def test_process_lines(input, size, diags, expected):
    assert process_lines(input, size, include_diagonals=diags) == expected

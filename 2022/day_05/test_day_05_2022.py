import pytest
from day_05_2022 import process_stacks, follow_moves

test_data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

starting_positions1, instructions1 = test_data.split("\n\n")
starting_positions2, instructions2 = test_data.split("\n\n")


@pytest.mark.parametrize(
    "stacks, instructions, crawler, expected",
    [
        (starting_positions1, instructions1, 9000, "CMZ"),
        (starting_positions2, instructions2, 9001, "MCD"),
    ],
)
def test_process_stacks(stacks, instructions, crawler, expected):
    assert follow_moves(process_stacks(stacks), instructions, crawler) == expected

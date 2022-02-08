from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list_of_ints as loi
from itertools import combinations
import numpy as np


def fix_expenses(target, count, report):
    solution = [
        option for option in combinations(report, count) if sum(option) == target
    ]
    if solution:
        print(f"Solution Found: {solution}")
        print(f"The product of these {count} numbers is {np.prod(solution)}")
        return np.prod(solution)
    else:
        print("No solutions exist")
        return None


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_01.txt"
    raw_data = rd(input)

    # Convert comma separated string to list
    data = loi(raw_data)

    print(
        f"PART 01: Multipling the 2 numbers that sum to 2020: {fix_expenses(2020, 2, data)}."
    )
    print(
        f"PART 02: Multipling the 3 numbers that sum to 2020: {fix_expenses(2020, 3, data)}."
    )

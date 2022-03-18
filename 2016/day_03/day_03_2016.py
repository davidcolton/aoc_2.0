from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list as stl
from aoc.data import split_string_of_ints_by_given_char as ssgc

import numpy as np


def is_triangle(lengths: list) -> int:
    lengths.sort()
    if lengths[0] + lengths[1] > lengths[2]:
        return 1
    else:
        return 0


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


if __name__ == "__main__":

    input = "day_03.txt"

    # Simple import
    # Single line of data imported as a string
    raw_data = rd(input)

    # Convert line separated string to list
    tmp_data = stl(raw_data)

    # Convert space separated string to list of ints
    data = [ssgc(x, None) for x in tmp_data]

    # Get the number of Row Triangles
    part_01 = sum(is_triangle(triangle) for triangle in data)

    # Create a clean version of the data
    data_02_raw = [ssgc(x, None) for x in tmp_data]

    # Transpose the data
    # And join the lists together
    data_02_trans = [list(i) for i in zip(*data_02_raw)]
    data_02 = [j for i in data_02_trans for j in i]

    part_02 = sum(is_triangle(triangle) for triangle in chunks(data_02, 3))

    print(f"PART 01: The number of valid triangles is: {part_01}")
    print(f"PART 01: Using a complex keypad: {part_02}")

from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list as stl
from aoc.data import split_string_of_ints_by_given_char as ssoi

from itertools import permutations


def checksum(data: list) -> int:
    return sum([max(r) - min(r) for r in data])


def evenly_divisible_values(data: list) -> int:
    return sum(
        int(x / y) for row in data for x, y in permutations(row, 2) if x % y == 0
    )


if __name__ == "__main__":

    input = "day_02.txt"

    # Simple import
    # Single line of data imported as a string
    raw_data = rd(input)

    # Split string by line into list
    tmp_data = stl(raw_data.strip())

    # Split list elements by given character
    data = [ssoi(l, "\t") for l in tmp_data]

    print(f"PART 01: The checksum in: {checksum(data)}")
    print(
        f"PART 02: The evenly divisible values checksum is : {evenly_divisible_values(data)}"
    )

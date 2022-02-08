from itertools import accumulate, cycle
from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list_of_ints as loi


def frequency(numbers: list, duplicate: bool = False) -> int:
    if duplicate:
        seen = {0}
        return next(
            freq
            for freq in accumulate(cycle(numbers))
            if freq in seen or seen.add(freq)
        )
    else:
        return sum(numbers)


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_01.txt"
    raw_data = rd(input)

    # Convert comma separated string to list
    data = loi(raw_data)

    print(f"PART 01: The frequency is {frequency(data)}.")
    print(f"PART 02: The frequency is {frequency(data, duplicate=True)}.")

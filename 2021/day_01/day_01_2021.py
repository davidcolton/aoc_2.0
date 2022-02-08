from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list_of_ints as loi


def examine_sonar(input, window):
    increases = 0
    for position in range(len(input) - window):
        if sum(input[position + 1 : position + window + 1]) > sum(
            input[position : position + window]
        ):
            increases += 1

    return increases


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_01.txt"
    raw_data = rd(input)

    # Convert comma separated string to list
    data = loi(raw_data)

    print(f"PART 01: Sonar measurements increased: {examine_sonar(data, 1)}.")
    print(
        f"PART 02: Using sliding window of size 3, Sonar measurements increased: {examine_sonar(data, 3)}."
    )

from aoc.data import read_data as rd
from aoc.data import split_string_of_ints_by_given_char as ssoi


def redistribution_cycles(input: list) -> int:

    seen_distributions = []
    redistributions = 0

    num_blocks = len(input)

    # Add the first distibution to the list
    seen_distributions.append("".join(str(c) for c in input))

    while True:

        redistributions += 1

        most_blocks = max(input)
        index_most_blocks = input.index(most_blocks)

        input[index_most_blocks] = 0

        for idx in range(index_most_blocks + 1, index_most_blocks + 1 + most_blocks):
            input[idx % num_blocks] += 1

        this_arrangement = "".join(str(c) for c in input)

        if this_arrangement in seen_distributions:
            # seen_distributions.append(this_arrangement)
            first_occurances = seen_distributions.index(this_arrangement)
            return redistributions, len(seen_distributions) - first_occurances
        else:
            seen_distributions.append(this_arrangement)


if __name__ == "__main__":

    input = "day_06.txt"

    # Simple import
    # Single line of data imported as a string
    raw_data = rd(input)
    data = ssoi(raw_data, ",")

    part_01, part_02 = redistribution_cycles(data)

    print(f"PART 01: {part_01}")
    print(f"PART 02: {part_02}")

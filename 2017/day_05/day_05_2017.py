from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list_of_ints as loi


def process_maze_steps(data: list, part: int = 1) -> int:

    # The starting index
    idx = 0
    step = 0

    # Loop while idx is less than the length of the data
    while len(data) >= idx >= 0:
        try:
            new_idx = data[idx] + idx
            if part == 1:
                data[idx] = data[idx] + 1
            else:
                if data[idx] >= 3:
                    data[idx] = data[idx] - 1
                else:
                    data[idx] = data[idx] + 1
            idx = new_idx
            step += 1
        except IndexError:
            return step

        # print(step, idx, data[idx])


if __name__ == "__main__":

    input = "day_05.txt"

    # Simple import
    # Single line of data imported as a string
    raw_data = rd(input)
    data = loi(raw_data)

    print(
        f"PART 01: Jumped out of maze after: {process_maze_steps(data.copy())} steps."
    )
    print(
        f"PART 02: Jumped out of maze after: {process_maze_steps(data.copy(), part=2)} steps."
    )

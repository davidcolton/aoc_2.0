from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list as stl


def tree_counter(forest: list, right: int, down: int) -> int:

    rows = len(forest)
    cols = len(forest[0])

    row_number = 0
    col_number = 0

    tree_count = 0

    while row_number < rows:
        if forest[row_number][col_number % cols] == "#":
            tree_count += 1
        row_number += down
        col_number += right

    return tree_count


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_03.txt"
    raw_data = rd(input)

    # Convert comma separated string to list
    data = stl(raw_data)

    setting_01 = tree_counter(data, 1, 1)
    setting_02 = tree_counter(data, 3, 1)
    setting_03 = tree_counter(data, 5, 1)
    setting_04 = tree_counter(data, 7, 1)
    setting_05 = tree_counter(data, 1, 2)

    all_trees = setting_01 * setting_02 * setting_03 * setting_04 * setting_05

    print(f"PART 01: Trees encountered at setting 2 is {setting_02}.")
    print(f"PART 02: Sums of trees encountered at all setting levels is {all_trees}.")

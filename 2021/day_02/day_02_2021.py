from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list as stl


def calculate_position(values):

    position = depth = 0

    for ins in values:
        direction, dist = ins.split()
        if direction == "forward":
            position += int(dist)
        elif direction == "down":
            depth += int(dist)
        elif direction == "up":
            depth -= int(dist)

    return position * depth


def calculate_position_with_aim(values):

    position = depth = aim = 0

    for ins in values:
        direction, dist = ins.split()
        if direction == "forward":
            depth += int(dist) * aim
            position += int(dist)
        elif direction == "down":
            aim += int(dist)
        elif direction == "up":
            aim -= int(dist)

    return position * depth


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_02.txt"
    raw_data = rd(input)

    # Convert comma separated string to list
    data = stl(raw_data)

    print(f"PART 01: Position is: {calculate_position(data)}")
    print(f"PART 02: Position with aim is: {calculate_position_with_aim(data)}")

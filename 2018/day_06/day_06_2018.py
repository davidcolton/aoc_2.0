from aoc.data import read_lines_of_data as rd

from itertools import product


def manhattan(x: tuple, y: tuple) -> int:
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


if __name__ == "__main__":

    input = "day_06.txt"

    # Simple import
    # Single line of data imported as a string
    # raw_data = rd(input)
    # data = [[int(n) for n in s.split(", ")] for s in raw_data]

    data = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]

    # Get the smallest x, y coordinates
    min_x = min(data, key=lambda x: x[0])[0]
    min_y = min(data, key=lambda x: x[1])[1]

    # # Move all coordinates to reduce the time to process
    # new_data = [[x[0] - min_x, x[1] - min_y] for x in data]

    # Get the new largest x, y coordinates
    max_x = max(data, key=lambda x: x[0])[0]
    max_y = max(data, key=lambda x: x[1])[1]

    coords = list(product(range(min_x, max_x + 1), range(min_y, max_y + 1)))

    distances_list = []

    # Get distance from every coordinate to every point
    for coord in coords:

        # Calculate distance to each data point
        distances = {p: manhattan(coord, p) for p in data}

        minval = min(distances.values())
        res = [k for k, v in distances.items() if v == minval]

        print(coord, minval, res)

        distances_list.append({coord: distances})

    # print(distances_list)

    print(f"PART 01: ")
    print(f"PART 02: ")

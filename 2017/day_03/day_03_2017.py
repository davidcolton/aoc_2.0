from math import sqrt


def manhattan_distance(target: int) -> int:

    if target == 1:
        return 1

    # Square Root whole number
    sqrt_target = int(sqrt(target))

    # Get the bottom right corner after the target
    # sqrt_corner is also the length of each side
    # Half length are the number of memory positions
    #   either side of the midpoint of a side
    sqrt_corner = (sqrt_target + 1) if sqrt_target % 2 == 0 else (sqrt_target + 2)
    first_block_in_loop = ((sqrt_corner - 2) ** 2) + 1
    half_length = sqrt_corner // 2

    # Get all corner values
    bottom_right_corner = sqrt_corner ** 2
    bottom_left_corner = bottom_right_corner - sqrt_corner + 1
    top_left_corner = bottom_left_corner - sqrt_corner + 1
    top_right_corner = top_left_corner - sqrt_corner + 1

    # Get all midpoints
    right_midpoint = top_right_corner - half_length
    top_midpoint = top_left_corner - half_length
    left_midpoint = bottom_left_corner - half_length
    bottom_midpoint = bottom_right_corner - half_length

    midpoints = [right_midpoint, top_midpoint, left_midpoint, bottom_midpoint]

    # Calculate Manhattan distance
    dist = min(abs(target - m) for m in midpoints) + half_length

    return dist


def spiral(max_size):
    # Not my work. See:
    # https://stackoverflow.com/questions/398299/looping-in-a-spiral
    x, y = 0, 0
    dx, dy = 0, -1

    for _ in range(max_size ** 2):
        if abs(x) == abs(y) and [dx, dy] != [1, 0] or x > 0 and y == 1 - x:
            dx, dy = -dy, dx  # corner, change direction

        yield x, y

        x, y = x + dx, y + dy


def sum_neighbours(values_dict: dict, new_key: tuple) -> int:

    neighbours = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

    x, y = new_key

    new_keys = [(n[0] + x, n[1] + y) for n in neighbours]

    total = 0
    for key in new_keys:
        try:
            total += values_dict[key]
        except KeyError:
            # Memory location has not been written yet
            ...
    return total


def get_larger_value(value: int) -> int:

    values_dict = {(0, 0): 1}

    for x, y in spiral(target):
        if x == 0 and y == 0:
            # (0, 0) key is already present
            ...
        else:
            values_dict[(x, y)] = sum_neighbours(values_dict, (x, y))

        if values_dict[(x, y)] > target:
            return values_dict[(x, y)]


if __name__ == "__main__":

    target = 312051

    print(f"PART 01: Manhattan Steps to target is:{manhattan_distance(target)}")
    print(
        f"PART 02: First value larger than puzzle input is: {get_larger_value(target)}"
    )

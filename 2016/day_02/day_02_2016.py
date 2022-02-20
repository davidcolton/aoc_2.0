from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list as stl

keypad = {
    1: {"U": 1, "R": 2, "D": 4, "L": 1},
    2: {"U": 2, "R": 3, "D": 5, "L": 1},
    3: {"U": 3, "R": 3, "D": 6, "L": 2},
    4: {"U": 1, "R": 5, "D": 7, "L": 5},
    5: {"U": 2, "R": 6, "D": 8, "L": 4},
    6: {"U": 3, "R": 6, "D": 9, "L": 5},
    7: {"U": 4, "R": 8, "D": 7, "L": 7},
    8: {"U": 5, "R": 9, "D": 8, "L": 7},
    9: {"U": 6, "R": 9, "D": 9, "L": 8},
}

complex_keypad = {
    1: {"U": 1, "R": 1, "D": 3, "L": 1},
    2: {"U": 2, "R": 3, "D": 6, "L": 2},
    3: {"U": 1, "R": 4, "D": 7, "L": 2},
    4: {"U": 4, "R": 4, "D": 8, "L": 3},
    5: {"U": 5, "R": 6, "D": 5, "L": 5},
    6: {"U": 2, "R": 7, "D": "A", "L": 5},
    7: {"U": 3, "R": 8, "D": "B", "L": 6},
    8: {"U": 4, "R": 9, "D": "C", "L": 7},
    9: {"U": 9, "R": 9, "D": 9, "L": 8},
    "A": {"U": 6, "R": "B", "D": "A", "L": "A"},
    "B": {"U": 7, "R": "C", "D": "D", "L": "A"},
    "C": {"U": 8, "R": "C", "D": "C", "L": "B"},
    "D": {"U": "B", "R": "D", "D": "D", "L": "D"},
}


def enter_keycode(codes: list, keyboard: dict) -> str:
    # Always start at key 5
    current_key = 5
    code = []

    for line in codes:
        for move in line:
            current_key = keyboard[current_key][move]
        code.append(current_key)

    return "".join(str(c) for c in code)


if __name__ == "__main__":

    input = "day_02.txt"

    # Simple import
    # Single line of data imported as a string
    raw_data = rd(input)

    # Convert line separated string to list
    data = stl(raw_data)

    print(f"PART 01: Using a standard keypad: {enter_keycode(data, keypad)}")
    print(f"PART 01: Using a complex keypad: {enter_keycode(data, complex_keypad)}")

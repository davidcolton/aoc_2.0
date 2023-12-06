from aoc.data import read_data as rd

import re

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def calibrate_values(input):
    digits = [char for char in input if char.isdigit()]
    if len(digits) > 0:
        return int(digits[0] + digits[-1])
    else:
        return 0


def find_numbers(input):
    digits_to_sum = []

    for num in numbers.keys():
        for match in re.finditer(num, input):
            digits_to_sum.append((match.start(), numbers[num]))

    od = sorted(digits_to_sum, key=lambda x: x[0])

    return int(od[0][1] + od[-1][1])


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_01.txt"
    raw_data = rd(input)

    # Convert raw data to list
    data = [line for line in raw_data.split()]

    print(f"PART 01: Calibrated Values: {sum([calibrate_values(line) for line in data])}.")
    print(f"PART 02: Find Numbers in Test: {sum([find_numbers(line) for line in data])}.")

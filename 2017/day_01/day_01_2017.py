from collections import Counter, namedtuple
from typing import NoReturn
from aoc.data import read_data as rd
from aoc.data import number_to_list_of_ints as loi


def captcha(numbers: list, half: bool = False) -> int:
    jump = int(len(numbers) / 2) if half else 1
    total = 0
    for idx, num in enumerate(numbers):
        if num == numbers[(idx + jump) % len(numbers)]:
            total += num

    return total


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_01.txt"
    raw_data = rd(input)

    # Convert comma separated string to list
    data = loi(raw_data)

    print(f"PART 01: The answer to the Captcha is {captcha(data)}.")
    print(f"PART 02: The answer to the Captcha is {captcha(data, half=True)}.")

from collections import Counter
from aoc.data import number_to_list_of_ints as loi


def rule_01(numbers: list) -> bool:
    digit_counter = Counter(numbers)
    return digit_counter.most_common(1)[0][1] >= 2 or len(digit_counter) == 1


def rule_02(numbers: list) -> bool:
    ht, tt, th, hu, te, si = numbers
    return si >= te >= hu >= th >= tt >= ht


def rule_03(numbers: list) -> bool:
    digit_counter = Counter(numbers)

    # Reverse the counter keys / values to a dictionary
    rev = {v: k for k, v in digit_counter.items()}

    # Is 2 in the keys (could have done values either)
    return 2 in rev.keys()


def part_01(lower: int, upper: int) -> int:

    valid_numbers = 0

    for number in range(lower, upper):
        number_list = loi(number)
        if rule_01(number_list) and rule_02(number_list):
            valid_numbers += 1

    return valid_numbers


def part_02(lower: int, upper: int) -> int:

    valid_numbers = 0

    for number in range(lower, upper):
        number_list = loi(number)
        if rule_01(number_list) and rule_02(number_list) and rule_03(number_list):
            valid_numbers += 1

    return valid_numbers


if __name__ == "__main__":
    # Simple input today
    lower_bound = 147981
    upper_bound = 691423

    print(f"PART 01: {part_01(lower_bound, upper_bound)}.")
    print(f"PART 02: {part_02(lower_bound, upper_bound)}.")

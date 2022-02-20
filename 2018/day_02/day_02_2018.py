import collections
from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list as stl

from collections import Counter
from difflib import SequenceMatcher
from itertools import combinations


def checksum(data: list) -> int:
    two_count = three_count = 0
    for box_id in data:
        tmp_counter = Counter(box_id)
        if 2 in tmp_counter.values():
            two_count += 1
        if 3 in tmp_counter.values():
            three_count += 1
    return two_count * three_count


def common_letters(data: list) -> str:
    best_match_score = 0
    best_match_first = ""
    best_match_second = ""

    for pair in combinations(data, 2):
        score = SequenceMatcher(a=pair[0], b=pair[1]).ratio()
        if score > best_match_score:
            best_match_score = score
            best_match_first = pair[0]
            best_match_second = pair[1]

    return "".join(a for a, b in zip(best_match_first, best_match_second) if a == b)


if __name__ == "__main__":

    input = "day_02.txt"

    # Simple import
    # Single line of data imported as a string
    raw_data = rd(input)

    # Split string by line into list
    data = stl(raw_data.strip())

    print(f"PART 01: The checksum in: {checksum(data)}")
    print(f"PART 02: The common letters checksum is : {common_letters(data)}")

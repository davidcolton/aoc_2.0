from curses import raw
from aoc.data import read_lines_of_data as rd
from collections import Counter
from itertools import permutations


def simple_pass_phrases(data: list) -> int:

    # Part 01
    # Create a list of the words in each line
    # Split by spaces and make a counter
    # Any Counter where the most common value is 1 has all unique words
    list_of_word_counters = [Counter(l.split(" ")) for l in data]
    return sum(1 for c in list_of_word_counters if c.most_common()[0][1] == 1)


def complex_pass_phrases(data: list) -> int:

    # Part 02
    # Same as part 1 but this time all permutation of all pass phrases
    added_security = 0
    for line in data:
        all_permutations = []
        for word in line.split(" "):
            all_permutations.extend(list(set(["".join(p) for p in permutations(word)])))

        list_of_permutations_counter = Counter(all_permutations)

        if list_of_permutations_counter.most_common()[0][1] == 1:
            added_security += 1

    return added_security


if __name__ == "__main__":

    input = "day_04.txt"

    # Simple import
    # Single line of data imported as a string
    raw_data = rd(input)

    print(f"PART 01: Simple pass phrases: {simple_pass_phrases(raw_data)}")
    print(f"PART 02: Added security pass phrases: {complex_pass_phrases(raw_data)}")

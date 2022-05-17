from aoc.data import read_data as rd
from collections import Counter


def total_yes_answers(input):
    questions_list = [l.replace("\n", "").strip().split() for l in input.split("\n\n")]
    answers_counters = [Counter(l[0]) for l in questions_list]
    return sum([len(c) for c in answers_counters])


def everyone_answered_yes(input):
    questions_list = [l.replace("\n", " ").strip().split() for l in input.split("\n\n")]
    answers_sets = [[set(person) for person in group] for group in questions_list]
    return sum(len(answers[0].intersection(*answers)) for answers in answers_sets)


if __name__ == "__main__":
    # Simple import
    # Single line o
    # f data imported as a string
    input = "day_06.txt"

    raw_data = rd(input)

    print(f"PART 01: Questions answered YES: {total_yes_answers(raw_data)}")
    print(
        f"PART 02: Questions everyone answered YES: {everyone_answered_yes(raw_data)}"
    )

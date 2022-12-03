from aoc.data import read_data as rd
from aoc.data import read_lines_of_data as rlod

from string import ascii_lowercase, ascii_uppercase


low_priorities = {g[0]: g[1] for g in zip(ascii_lowercase, range(1, 27))}
high_priorities = {g[0]: g[1] for g in zip(ascii_uppercase, range(27, 53))}
all_priorities = low_priorities | high_priorities


def sum_of_priorities(input):
    priorities = []
    for l in input:
        len_l = int(len(l) / 2)
        list_l = [c for c in l]
        left_compartment = list_l[:len_l]
        right_compartment = list_l[len_l:]
        priorities.append(
            set(
                [
                    x
                    for x in left_compartment + right_compartment
                    if x in left_compartment and x in right_compartment
                ]
            ).pop()
        )
    return sum(all_priorities[p] for p in priorities)


def elf_priorities(input):
    elf_priorities = []
    for elves in zip(*(iter(input),) * 3):
        elf_priorities.append(set(elves[0]).intersection(elves[1], elves[2]).pop())
    return sum(all_priorities[p] for p in elf_priorities)


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_03.txt"
    data = rlod(input)

    print(f"PART 01: Sum of priorities: {sum_of_priorities(data)}")
    print(f"PART 02: Sum of Elf priorities: {elf_priorities(data)}")

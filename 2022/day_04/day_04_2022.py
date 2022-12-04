from aoc.data import read_data as rd
from aoc.data import read_lines_of_data as rlod

test_data = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]


def assignments_overlap(input, type="contained"):
    overlaps = 0
    for l in input:
        r1 = set(range(l[0][0], l[0][1] + 1))
        r2 = set(range(l[1][0], l[1][1] + 1))
        if type == "contained" and (r1.issubset(r2) or r2.issubset(r1)):
            overlaps += 1
        elif type == "overlap" and (r1 & r2):
            overlaps += 1

    return overlaps


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_04.txt"
    raw_data = rlod(input)

    data = []
    for l in raw_data:
        print(l)
        e1, e2 = l.split(",")
        e1f, e1l = map(int, e1.split("-"))
        e2f, e2l = map(int, e2.split("-"))
        data.append([(e1f, e1l), (e2f, e2l)])

    print(data)

    print(f"PART 01: Number of overlapping assignments: {assignments_overlap(data)}")
    print(f"PART 02: Sum of Elf priorities: {assignments_overlap(data, 'overlap')}")

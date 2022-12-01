from aoc.data import read_data as rd
from aoc.data import read_blocks_of_data as rbod


def most_calories(input):
    return max([sum(n) for n in input])

def top_three(input):
    all_calories = [sum(n) for n in input]
    all_calories.sort(reverse=True)
    return sum(all_calories[:3])


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_01.txt"
    raw_data = rbod(input)

    # Convert raw data to list of ints
    data = [[int(n) for n in l.strip().split("\n")] for l in raw_data]

    print(f"PART 01: Most calaries: {most_calories(data)}.")
    print(f"PART 02: Sum of top three calories: {top_three(data)}.")

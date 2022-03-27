from email import generator
from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list as stl

from collections import Counter


def extract_coords(line: str) -> tuple[str, generator.Generator]:

    # For Part 01 we do not case about the ID's
    elements = line.split()
    claim_id = elements[0]
    left, top = elements[2][:-1].split(",")
    width, height = elements[3].split("x")

    x = range(int(left), int(left) + int(width))
    y = range(int(top), int(top) + int(height))

    return claim_id, ((a, b) for a in x for b in y)


def generate_coords_counter(data: list) -> Counter:

    all_coords = Counter()
    for claim in data:
        coords = Counter(extract_coords(claim)[1])
        all_coords.update(coords)

    return all_coords


def no_overlap(data: list, all_coords: Counter) -> str:

    # Get all coords that only appear once
    appear_once = set(k for k, v in all_coords.items() if v == 1)

    # Loop over all data items
    # If all coords of a claim appear in appear_once
    # That that is the ID we are looking for
    for claim in data:
        claim_id, coords = extract_coords(claim)
        coords = set(coords)
        if coords.issubset(appear_once):
            return claim_id


if __name__ == "__main__":

    input = "day_03.txt"

    # Simple import
    # Single line of data imported as a string
    raw_data = rd(input)

    # Split string by line into list
    data = stl(raw_data.strip())

    # Generate a Counter of all positions in all claims
    # Remove all single values
    all_coords = generate_coords_counter(data)
    two_claims = {k: v for k, v in all_coords.items() if v > 1}

    # Get unique claim
    unique_claim = no_overlap(data, all_coords)

    print(f"PART 01: The number of square inches in multiple claims: {len(two_claims)}")
    print(f"PART 02: The unique claim is: {unique_claim}")

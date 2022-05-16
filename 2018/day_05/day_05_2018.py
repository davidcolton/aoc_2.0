from aoc.data import read_data as rd

from string import ascii_lowercase, ascii_uppercase

# Create a single list of all the replacement strings
lower_upper = ["".join(t) for t in (zip(ascii_lowercase, ascii_uppercase))]
upper_lower = ["".join(t) for t in (zip(ascii_uppercase, ascii_lowercase))]
replacement_strings = lower_upper + upper_lower


def replace_str(text: str, strs_to_repl: list) -> str:
    for s in strs_to_repl:
        text = text.replace(s, "")
    return text


def polymer_reactions(text: str, strs_to_repl: list) -> str:

    # Loop while True
    # Breakout when the length of the string doesn't change

    while True:

        length_before = len(text)
        text = replace_str(text, strs_to_repl)
        if len(text) == length_before:
            return len(text)


def single_polymer_reaction(text: str, strs_to_repl: list) -> str:

    # Test each chain to see which give the best reduction
    shortest_length = len(text) + 1

    for c in ascii_lowercase:

        text_to_change = text
        new_length = polymer_reactions(
            replace_str(text_to_change, [c, c.upper()]), strs_to_repl
        )

        if new_length < shortest_length:
            shortest_length = new_length

    return shortest_length


if __name__ == "__main__":

    input = "day_05.txt"

    # Simple import
    # Single line of data imported as a string
    raw_data = rd(input)

    part_01 = raw_data
    part_02 = raw_data

    print(f"PART 01: The answer is: {polymer_reactions(part_01, replacement_strings)}")
    print(
        f"PART 02: The answer is: {single_polymer_reaction(part_02, replacement_strings)}"
    )

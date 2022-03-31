import hashlib


def calculate_matching_hash(starts_with, zeros, lowest_value=0):
    while True:
        text_to_hash = f"{starts_with}{lowest_value}"
        h = hashlib.md5(text_to_hash.encode("utf-8")).hexdigest()
        if h.startswith("0" * zeros):
            print(f"The hash that starts with {zeros} zeros is: {h}")
            print(f"The input value to produce this hash is {text_to_hash}")
            print(f"The suffix added to {starts_with} is {lowest_value}\n")
            return lowest_value
            break
        lowest_value += 1


if __name__ == "__main__":

    puzzle_input = "bgvyzdsv"

    five_zeros = calculate_matching_hash(puzzle_input, 5)
    six_zeros = calculate_matching_hash(puzzle_input, 6, five_zeros)

    print(f"PART 01: The lowest positive number with 5 leading zeros is : {five_zeros}")
    print(f"PART 02: The lowest positive number with 6 leading zeros is : {six_zeros}")

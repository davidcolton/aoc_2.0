from collections import Counter

from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list as stl


def process_password_definition(password_definition):
    # Process the line contain the password policy and the password
    letter_range, letter, password = password_definition.split()
    lower, upper = letter_range.split("-")
    letter = letter[0]
    return int(lower), int(upper), letter, password


def password_checker(password_list):
    valid_passowrds = 0

    for password_definition in password_list:
        lower, upper, letter, password = process_password_definition(
            password_definition
        )

        # Use a Counter to get a count of each letter in the password
        password_letters = Counter(password)

        # Is the letter the requisite times in the password
        if lower <= password_letters[letter] <= upper:
            valid_passowrds += 1

    return valid_passowrds


def positional_password_checker(password_list):
    valid_passwords = 0

    for password_definition in password_list:
        lower, upper, letter, password = process_password_definition(
            password_definition
        )

        # The positional locater and 1 indexed
        # Need to handle 0 indexed string
        if bool(password[lower - 1] == letter) ^ bool(password[upper - 1] == letter):
            valid_passwords += 1

    return valid_passwords


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_02.txt"
    raw_data = rd(input)

    # Convert comma separated string to list
    data = stl(raw_data)

    print(f"PART 01: Number of valid Sled passwords: {password_checker(data)}.")
    print(
        f"PART 02: Number of valid Toboggan passwords: {positional_password_checker(data)}."
    )

def read_data(file_path: str) -> str:
    """Read in the data file as a string.
    No post procession or any formatting applied.
    Further preparatin of the data for downstream logic is handled separately.

    Args:
        file_path (str): The path to the data file to be imported.

    Returns:
        str: The whole datafile as a string for processing later
    """

    with open(file_path, "r") as f:
        raw_data = f.read()

    return raw_data


def read_lines_of_data(file_path: str) -> str:
    """Read in the data file as a string.
    No post procession or any formatting applied.
    Further preparatin of the data for downstream logic is handled separately.

    Args:
        file_path (str): The path to the data file to be imported.

    Returns:
        str: The whole datafile with each line returned as an element of a list
    """

    with open(file_path, "r") as f:
        raw_data = f.read().split("\n")

    return raw_data


def comma_separated_strings_to_list(string: str) -> list:
    """Takes a comma separated sequence of strings and returns a list of the strings

    Args:
        string (str): A comma separated string e.g. "a, b, c"

    Returns:
        list: A list of strings e.g. ["a", "b", "c"]
    """

    return [s.strip() for s in string.split(",")]


def line_separated_strings_to_list(string: str) -> list:
    """Takes a line separated sequence of strings and returns a list of the strings

    Args:
        string (str): A line separated string e.g. "a\nb\nc"

    Returns:
        list: A list of strings e.g. ["a", "b", "c"]
    """

    return [s.strip() for s in string.split("\n")]


def line_separated_strings_to_list_of_ints(string: str) -> list:
    """Takes a line separated sequence of strings and returns a list of the strings

    Args:
        string (str): A line separated string e.g. "+1,
        -2,
        +3"

    Returns:
        list: A list of ints e.g. [1, 2, 3]
    """

    return [int(s.strip()) for s in string.strip().split("\n")]


def number_to_list_of_ints(num: int) -> list:
    """Takes a number and returns a list of integers

    Args:
        num (int): A number e.g. 12345

    Returns:
        list: A list of ints e.g. [1, 2, 3, 4, 5]
    """

    return [int(s) for s in str(num).strip()]


def split_string_of_ints_by_given_char(string: str, sep: str) -> list:
    """Takes a character separated list and the separator and
    returns a list of integers

    Args:
        string (str): A list of separated integers e.g. "1\t2\t3"
        sep" (str): The string separator e.g. "\t"

    Returns:
        list: A list of ints e.g. [1, 2, 3]
    """

    return [int(s) for s in string.split(sep)]

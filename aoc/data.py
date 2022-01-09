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


def comma_separated_strings_to_list(string: str) -> list:
    """Takes a comma separated sequence of strings and returns a list of the strings

    Args:
        string (str): A comma separated string e.g. "a, b, c"

    Returns:
        list: A list of strings e.g. ["a", "b", "c"]
    """

    return [s.strip() for s in string.split(",")]

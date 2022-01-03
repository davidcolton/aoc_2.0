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

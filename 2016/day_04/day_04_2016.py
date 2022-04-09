from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list as stl
from aoc.data import split_string_of_strings_by_given_char as ssgc
from collections import Counter
from string import ascii_lowercase

letters = [c for c in ascii_lowercase]


def process_data(raw_data: str) -> list:

    # Convert line separated string to list
    tmp_data = stl(raw_data)

    # Some string replacements to make the data easier to handle
    tmp_data = [s.replace("[", "-") for s in tmp_data]
    tmp_data = [s.replace("]", "") for s in tmp_data]

    # Lists to hold the different part
    rooms = []

    for room in tmp_data:
        data = ssgc(room, "-")
        encrypted_name = "".join(t for t in data[:-2])
        space_sep_name = " ".join(t for t in data[:-2])
        sector_id = int(data[-2])
        checksum = data[-1]

        rooms.append(
            {
                "encrypted_name": encrypted_name,
                "space_sep_name": space_sep_name,
                "character_count": dict(Counter(encrypted_name)),
                "sector_id": sector_id,
                "checksum": checksum,
            }
        )

    return rooms


def validate_checksums(rooms: list) -> list:

    sum_of_ids = 0
    valid_rooms = []

    for room in rooms:

        # Sort the encrypted name dictionary
        # First by: Value
        # Then by:  Key
        # And return first 5 values
        checksum_tuples = sorted(
            room["character_count"].items(), key=lambda k: (-k[1], k[0])
        )[:5]

        # Extract the checksum from the tuples
        checksum = "".join(i[0] for i in checksum_tuples)

        if checksum == room["checksum"]:
            sum_of_ids += room["sector_id"]
            valid_rooms.append(room)

    return sum_of_ids, valid_rooms


def decrypt_room_name(encrypted_name: str, sector_id: int) -> str:

    of_shiff = sector_id % 26
    decrypted_name = ""

    for char in encrypted_name:
        try:
            char_idx = letters.index(char)
            decrypted_char = letters[(char_idx + of_shiff) % 26]
            decrypted_name += decrypted_char
        except ValueError:
            decrypted_name += char

    return decrypted_name


def find_north_pole(rooms: list) -> int:

    for room in rooms:

        room_name = decrypt_room_name(room["space_sep_name"], room["sector_id"])
        if room_name.startswith("northpole"):
            return room["sector_id"]


if __name__ == "__main__":

    input = "day_04.txt"

    # Simple import
    # Single line of data imported as a string
    raw_data = rd(input)

    data = process_data(raw_data)

    sum_of_ids, valid_rooms = validate_checksums(data)

    print(f"PART 01: The sum of valis Room IDs: {sum_of_ids}")
    print(
        f"PART 01: The ID of the room where North Pole objects are stored: {find_north_pole(valid_rooms)}"
    )

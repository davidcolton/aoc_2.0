import pytest
from day_04_2016 import process_data, validate_checksums, decrypt_room_name

raw_data = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""

data = process_data(raw_data)


@pytest.mark.parametrize(
    "arg, expected",
    [
        (data, 1514),
    ],
)
def test_validate_checksums(arg, expected):
    assert validate_checksums(arg)[0] == expected


@pytest.mark.parametrize(
    "encrypt, sector_id, expected",
    [
        ("qzmt zixmtkozy ivhz", 343, "very encrypted name"),
    ],
)
def test_decrypt_room_name(encrypt, sector_id, expected):
    assert decrypt_room_name(encrypt, sector_id) == expected

import pytest
from day_06_2022 import start_packet


@pytest.mark.parametrize(
    "input, window_size, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4, 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 4, 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 4, 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4, 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4, 11),
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14, 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 14, 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 14, 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14, 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14, 26),
    ],
)
def test_start_packet(input, window_size, expected):
    assert start_packet(input, window_size) == expected

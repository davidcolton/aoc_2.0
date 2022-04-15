import pytest
from day_04_2018 import (
    read_records,
    identify_shifts,
    generate_guards,
    best_guard,
    sleep_guard,
)

raw_data = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""".split(
    "\n"
)

# Convert the raw data to a list of Record Tuples
data = read_records(raw_data)

# Get the shift details
shift_tuples = identify_shifts(data)

# Create the dictiony of the guards
# The key is the gaurds id
# The value is a numpy array of the guards sleep patterm
guards = generate_guards(data, shift_tuples)


@pytest.mark.parametrize(
    "arg, expected",
    [
        (guards, 240),
    ],
)
def test_best_guard(arg, expected):
    assert best_guard(arg) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (guards, 4455),
    ],
)
def test_sleep_guard(arg, expected):
    assert sleep_guard(arg) == expected

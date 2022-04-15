from aoc.data import read_lines_of_data as rd

from collections import namedtuple
from datetime import datetime, timedelta

import numpy as np

Record = namedtuple(
    "Record",
    [
        "timestamp",
        "year",
        "month",
        "day",
        "hour",
        "minute",
        "description",
    ],
)


def read_records(raw_data: list) -> list:

    # List of all shift records
    records = []

    # Convert each shift record to a named tuple
    for row in raw_data:

        # Extract the timestamp
        ts = datetime.strptime(row[1:17], "%Y-%m-%d %H:%M")
        year = ts.year
        month = ts.month
        day = ts.day
        hour = ts.hour
        minute = ts.minute
        description = row[19:]

        records.append(Record(ts, year, month, day, hour, minute, description))

    records = sorted(records, key=lambda tup: tup.timestamp)

    return records


def identify_shifts(data: list) -> list:

    # Process the list of Record Tuples
    # Get the index of all Record where shift begins
    starts_shift = []
    for idx, rec in enumerate(data):
        if "begins shift" in rec.description:
            starts_shift.append(idx)

    # Append last shift record index to the list
    starts_shift.append(len(data))

    # Create a list of tuples with start / end index of each day
    shift_tuples = [
        (starts_shift[i], starts_shift[i + 1]) for i in range(len(starts_shift) - 1)
    ]

    return shift_tuples


def generate_guards(data: list, shift_tuples: list) -> dict:

    # A dictionary to hold every guard
    guards = dict()

    # Process every days records
    for shift in shift_tuples:

        # Create a blank day for this shift
        # This assumes that the gaurd will work every minute in the shift
        day_array = [0] * 60

        rec_entries = data[shift[0] : shift[1]]

        for idx, rec in enumerate(rec_entries):
            # The shift starts
            if "begins shift" in rec.description:
                # The guards id is the second element of the description
                month = (
                    rec.month
                    if rec.hour == 0
                    else (rec.timestamp + timedelta(days=1)).month
                )
                day = (
                    rec.day
                    if rec.hour == 0
                    else (rec.timestamp + timedelta(days=1)).day
                )
                guard_id = rec.description.split()[1]
                guard = int(guard_id[1:])

            # Capture sleep periods
            # Set to zero in day_array
            if "falls asleep" in rec.description:
                start_idx = rec.minute
                end_idx = rec_entries[idx + 1].minute
                day_array[start_idx:end_idx] = [1] * (end_idx - start_idx)

        if guard not in guards.keys():
            guards[guard] = np.empty((0, 60), int)

        guards[guard] = np.append(guards[guard], np.array([day_array]), axis=0)

    return guards


def best_guard(guards: dict) -> int:

    # The guard that sleeps the most by the
    #   max number of days asleep
    best_guard = max(
        [
            (
                days_array.sum(),
                key,
                list(days_array.sum(axis=0)).index(max(days_array.sum(axis=0))),
            )
            for key, days_array in guards.items()
        ]
    )

    return best_guard[1] * best_guard[2]


def sleep_guard(guards: dict) -> int:

    # The guard that sleeps the most on a particular day
    #     by the id of the guard
    sleepy_guard = max(
        [
            (
                max(days_array.sum(axis=0)),
                list(days_array.sum(axis=0)).index(max(days_array.sum(axis=0))),
                key,
            )
            for key, days_array in guards.items()
        ]
    )

    return sleepy_guard[1] * sleepy_guard[2]


if __name__ == "__main__":

    input = "day_04.txt"

    # Simple import
    # Single line of data imported as a string
    raw_data = rd(input)

    # Convert the raw data to a list of Record Tuples
    data = read_records(raw_data)

    # Get the shift details
    shift_tuples = identify_shifts(data)

    # Create the dictiony of the guards
    # The key is the gaurds id
    # The value is a numpy array of the guards sleep patterm
    guards = generate_guards(data, shift_tuples)

    print(f"PART 01: The answer for strategy 1 is: {best_guard(guards)}")
    print(f"PART 02: The answer for strategy 1 is: {sleep_guard(guards)}")

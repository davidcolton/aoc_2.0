from socket import SO_SNDTIMEO
from aoc.data import read_data as rd
from aoc.data import split_string_of_ints_by_given_char as ssoi

import numpy as np


def evolve_lanternfish(arr):
    # Count number of Zero day Lanternfish
    ready_to_evolve = np.count_nonzero(arr == 0)

    # Reset Lanternfish that will reproduce
    arr = np.where(arr == 0, 7, arr)

    # Age all :anternfish by 1 day
    arr = arr - 1

    # Add new Lanternfish
    arr = np.append(arr, [8] * ready_to_evolve)

    return arr


def evolve(arr, days):

    # Do each Lanternfish separately
    fishes = np.split(arr, arr.size)

    total_population = 0

    # Evolve everyday
    for fish in fishes:
        for day in range(days):
            fish = evolve_lanternfish(fish)
        total_population += fish.size

    return total_population


def intelligent_evolution(data, days):
    # Get a count of number of fish per days 0 - 8
    state_count = [data.count(i) for i in range(9)]

    # Every day the
    for _ in range(0, days):
        # Fish at idx[0] are about to reproduce
        # Shift left wrap idx[0] to idx[8]
        state_count = state_count[1:] + state_count[:1]

        # The number of fish that reproduces are also 6 days
        #     from reproducing again
        state_count[6] += state_count[8]

    return sum(state_count)


if __name__ == "__main__":

    raw_data = rd("day_06.txt")
    data = ssoi(raw_data, ",")

    arr = np.array(data)

    print(f"Part 01: {evolve(arr, 80)}")
    print(f"Part 02: {intelligent_evolution(data, 256)}")

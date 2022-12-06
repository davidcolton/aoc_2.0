from aoc.data import read_data as rd
from more_itertools import windowed
from collections import Counter


def start_packet(data, window_size):
    packets = list(windowed(iter(data), n=window_size))
    for idx, packet in enumerate(packets):
        cnt = Counter(packet)
        if cnt.most_common(1)[0][1] == 1:
            return idx + window_size


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_06.txt"
    data = rd(input)

    print(f"PART 01: Package start location: {start_packet(data, 4)}")
    print(f"PART 02: Message start location: {start_packet(data, 14)}")

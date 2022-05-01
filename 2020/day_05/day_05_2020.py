from aoc.data import read_lines_of_data as rd


def binary_decimal(n):
    return int(n, 2)


def get_seat_numbers(input):
    seat_numbers = []
    for seat_code in input:
        row = binary_decimal(seat_code[:7].replace("F", "0").replace("B", "1"))
        seat = binary_decimal(seat_code[7:].replace("R", "1").replace("L", "0"))
        seat_numbers.append(row * 8 + seat)
    return seat_numbers


def find_my_seat(input):
    first_seat = min(input)
    sorted_seats = sorted(input)
    for idx, seat in enumerate(sorted_seats, first_seat):
        if idx != seat:
            return idx


if __name__ == "__main__":
    # Simple import
    # Single line o
    # f data imported as a string
    input = "day_05.txt"
    data = rd(input)

    print(f"PART 01: The maximum seat number is: {max(get_seat_numbers(data))}.")

    sorted_seats = sorted(get_seat_numbers(data))
    print(f"PART 02: Santa's seat number is: {find_my_seat(get_seat_numbers(data))}.")

from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list_of_ints as loi


def calculate_fuel(mass):
    return (mass // 3) - 2


def calculate_fuel_complex(mass):
    fuel = calculate_fuel(mass)

    # Base case: Fuel == 0
    if fuel <= 0:
        return 0

    # Recursive case:
    else:
        return fuel + calculate_fuel_complex(fuel)


def simple_fuel(list_of_masses):
    return sum(calculate_fuel(m) for m in list_of_masses)


def complex_fuel(list_of_masses):
    return sum(calculate_fuel_complex(m) for m in list_of_masses)


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_01.txt"
    raw_data = rd(input)

    # Convert comma separated string to list
    data = loi(raw_data)

    print(f"PART 01: Fuel calculated using simple method: {simple_fuel(data)}.")
    print(f"PART 02: Fuel calculated using complex method: {complex_fuel(data)}.")

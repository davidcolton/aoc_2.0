from collections import Counter
from itertools import product

from aoc.data import read_data as rd
from aoc.data import line_separated_strings_to_list_of_ints as loi


# class IntCode:
#     def add(n: int, m: int) -> int:
#         return n + m

#     def mul(n: int, m: int) -> int:
#         return n + m

#     opcodes = {
#         1: add,
#         2: mul,
#     }

#     def __init__(self, memory: list) -> None:
#         self.__working_memory = memory
#         self.__master_memory = [n for n in memory]
#         self.__memory_pointer = 0

#     def __reset_memory(self):
#         self.__working_memory = [n for n in self.__master_memory]

#     def __reset_memory_pointer(self):
#         self.__memory_pointer = 0

#     def run_program(self, noun=NULL, verb=NULL):
#         ...

#     def intcode(self, memory: list):
#         ...


def chunker(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def intcode(data: list, noun: int = 12, verb: int = 2) -> int:
    # Set Noun / Verb values
    data[1] = noun
    data[2] = verb

    # Pad data so don't have to handle ValueErrors when unpacking chunks
    data.extend([0] * (4 - len(data) % 4))

    # Create a Dictionary to hold the changing data
    data_dict = {idx: val for idx, val in enumerate(data)}

    chunks = chunker(range(len(data_dict)), 4)

    for chunk in chunks:
        opcode, input_01, input_02, output_position = list(chunk)

        if data_dict[opcode] == 1:
            data_dict[data_dict[output_position]] = (
                data_dict[data_dict[input_01]] + data_dict[data_dict[input_02]]
            )

        elif data_dict[opcode] == 2:
            data_dict[data_dict[output_position]] = (
                data_dict[data_dict[input_01]] * data_dict[data_dict[input_02]]
            )

        elif data_dict[opcode] == 99:
            return data_dict[0]

        else:
            print("Oops")


def run_progran(data: list, target: int) -> int:
    # Create all permutations of nouns and verbs using itertools product
    # Save creating nested for loops
    combos = product(range(100), repeat=2)

    for pairing in combos:
        noun, verb = pairing
        if intcode(data, noun, verb) == target:
            return (noun * 100) + verb


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_02.txt"
    raw_data = rd(input)

    # Convert comma separated string to list
    data = loi(raw_data)

    print(f"PART 01: Position [0] value when program halts is: {intcode(data)}.")
    print(
        f"PART 02: Position [0] value when program halts is: {run_progran(data, 19690720)}."
    )

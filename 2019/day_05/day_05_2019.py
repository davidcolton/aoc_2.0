from aoc.data import read_data as rd
from aoc.data import split_string_of_ints_by_given_char as ssgc


def interpret_instruction(opcode: int) -> list:

    opcode_list = [int(o) for o in str(opcode).zfill(5)]

    return [
        opcode_list[0],
        opcode_list[1],
        opcode_list[2],
        int("".join(str(n) for n in opcode_list[3:])),
    ]


def int_code(data: list, the_input):

    # The starting index
    idx = 0
    input = the_input

    outputs = []

    # Loop while idx is less than the length of the data
    while idx <= len(data):

        mode_03, mode_02, mode_01, op_code = interpret_instruction(data[idx])

        if op_code in [1, 2, 5, 6, 7, 8]:
            param_01 = data[idx + 1] if mode_01 else data[data[idx + 1]]
            param_02 = data[idx + 2] if mode_02 else data[data[idx + 2]]

        if op_code == 1:
            data[data[idx + 3]] = param_01 + param_02
            idx += 4

        if op_code == 2:
            data[data[idx + 3]] = param_01 * param_02
            idx += 4

        if op_code == 3:
            if mode_01:
                data[idx + 1] = input
            else:
                data[data[idx + 1]] = input
            idx += 2

        if op_code == 4:
            if mode_01:
                output = data[idx + 1]
            else:
                output = data[data[idx + 1]]
            outputs.append(output)
            idx += 2

        if op_code == 5:
            if param_01 != 0:
                idx = param_02
            else:
                idx += 3

        if op_code == 6:
            if param_01 == 0:
                idx = param_02
            else:
                idx += 3

        if op_code == 7:
            if param_01 < param_02:
                data[data[idx + 3]] = 1
            else:
                data[data[idx + 3]] = 0
            idx += 4

        if op_code == 8:
            if param_01 == param_02:
                data[data[idx + 3]] = 1
            else:
                data[data[idx + 3]] = 0
            idx += 4

        if op_code == 99:
            return outputs[-1]


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_05.txt"
    raw_data = rd(input)

    # Convert comma separated string to list of ints
    data = ssgc(raw_data, ",")
    data_02 = ssgc(raw_data, ",")

    print(f"PART 01: Diagnostic Code is: {int_code(data, 1)}.")
    print(f"PART 02: Diagnostic Code is: {int_code(data_02, 5)}.")

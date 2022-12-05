from aoc.data import read_data as rd
from aoc.data import read_blocks_of_data as rbod

import queue

test_data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

queue_indecies_test = [1, 5, 9]
queue_indecies = [1, 5, 9, 13, 17, 21, 25, 29, 33]


def process_stacks(input):
    data = ["".join(chars) for chars in zip(*input.splitlines())]
    stacks = {}
    for line in data:
        if "[" in line or "]" in line or line.isspace():
            next
        else:
            s = list(line.strip()[::-1])
            stacks[s[0]] = s[1:]

    return stacks


def follow_moves(stacks, instructions, crate_mover=9000):
    for move in instructions.split("\n"):
        _, num, _, from_stack, _, to_stack = move.split(" ")
        num = int(num)

        # Get the stack
        remove_from_stack = stacks[from_stack]

        # Crates to move
        crates_to_move = remove_from_stack[-num:]

        # Remove crates from the from Stack
        del remove_from_stack[-num:]
        stacks[from_stack] = remove_from_stack

        # Add crates to to the to Stack
        add_to_stack = stacks[to_stack]
        if crate_mover == 9000:
            add_to_stack = add_to_stack + crates_to_move[::-1]
        elif crate_mover == 9001:
            add_to_stack = add_to_stack + crates_to_move
        stacks[to_stack] = add_to_stack

        # print(stacks)

    message = ""
    for final_stacks in stacks.values():
        try:
            message = message + final_stacks[-1]
        except IndexError:
            message = message + " "

    return message


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_05.txt"
    starting_positions_01, instructions_01 = rbod(input)
    starting_positions_02, instructions_02 = rbod(input)
    stacks_01 = process_stacks(starting_positions_01)
    stacks_02 = process_stacks(starting_positions_02)
    message_part01 = follow_moves(stacks_01, instructions_01)
    message_part02 = follow_moves(stacks_02, instructions_02, crate_mover=9001)

    print(f"PART 01: Message: {message_part01}")
    print(f"PART 02: Message: {message_part02}")

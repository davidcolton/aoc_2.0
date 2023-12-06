from aoc.data import read_data as rd

import numpy as np

simple_game_rules = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def play_simple_game(input):
    name, game = input.split(":")
    game_num = int(name.split(" ")[1])

    good_game = True

    draws = game.split(";")
    for draw in draws:
        turns = draw.split(",")
        for turn in turns:
            num, colour = turn.strip().split(" ")
            if int(num.strip()) > simple_game_rules[colour.strip()]:
                good_game = False 

    return game_num if good_game else 0

def least_game(input):
    name, game = input.split(":")
    game_num = int(name.split(" ")[1])

    biggest = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    draws = game.split(";")
    for draw in draws:
        turns = draw.split(",")
        for turn in turns:
            num, colour = turn.strip().split(" ")
            if int(num.strip()) > biggest[colour.strip()]:
                biggest[colour.strip()] = int(num.strip())

    return np.prod(list(biggest.values()))


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_02.txt"
    raw_data = rd(input)

    # Convert raw data to list
    data = [line for line in raw_data.split("\n")]

    print(f"PART 01: Simple Game: {sum([play_simple_game(line) for line in data])}.")
    print(f"PART 02: Least Games: {sum([least_game(line) for line in data])}.")

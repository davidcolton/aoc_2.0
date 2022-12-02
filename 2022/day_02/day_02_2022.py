from aoc.data import read_data as rd
from aoc.data import read_lines_of_data as rlod

"""
    A & X: Rock
    B & Y: Paper
    C & Z: Scissors

    X: lose
    Y: draw
    Z: win
"""

strategy_1 = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3 
}

strategy_2 = {
    "A X": strategy_1["A Z"],
    "A Y": strategy_1["A X"],
    "A Z": strategy_1["A Y"],
    "B X": strategy_1["B X"],
    "B Y": strategy_1["B Y"],
    "B Z": strategy_1["B Z"],
    "C X": strategy_1["C Y"],
    "C Y": strategy_1["C Z"],
    "C Z": strategy_1["C X"] 
}

def blind_strategy(input):
    return sum([strategy_1[l] for l in input])

def real_strategy(input):
    return sum([strategy_2[l] for l in input])

if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_02.txt"
    data = rlod(input)


    print(f"PART 01: Follow assumed Stategy: {blind_strategy(data)}.")
    print(f"PART 02: Follow actual Stategy: {real_strategy(data)}.")

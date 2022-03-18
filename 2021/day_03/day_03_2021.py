from aoc.data import read_data as rd
from aoc.data import lines_of_numbers_to_lists_of_ints as loi

import pandas as pd


def get_power(df):
    val_counts = df.apply(pd.Series.value_counts)
    gamma = int("".join(map(str, list(val_counts.idxmax()))), 2)
    epsilon = int("".join(map(str, list(val_counts.idxmin()))), 2)
    return gamma * epsilon


def get_oxygen(df):
    for col in range(df.shape[1] + 1):
        max_val = df[col].value_counts().idxmax()
        min_val = df[col].value_counts().idxmin()
        if df[col].value_counts()[0] == df[col].value_counts()[1]:
            max_val = 1
        df = df[df[col] == max_val]
        if df.shape[0] == 1:
            break
    return int("".join(map(str, df.values.flatten().tolist())), 2)


def get_carbon(df):
    for col in range(df.shape[1] + 1):
        max_val = df[col].value_counts().idxmax()
        min_val = df[col].value_counts().idxmin()
        if df[col].value_counts()[0] == df[col].value_counts()[1]:
            min_val = 0
        df = df[df[col] == min_val]
        if df.shape[0] == 1:
            break
    return int("".join(map(str, df.values.flatten().tolist())), 2)


def get_life_support(df):

    oxygen = get_oxygen(df.copy())
    carbon = get_carbon(df.copy())
    return oxygen * carbon


# if __name__ == "__main__":

#     # Read in the input ... always called `input`
#     # Customize depending on the type of data structure required

#     # Day 03: Binary but treat as pandas columns of ints
#     df = pd.read_csv('input', dtype=object, header=None)
#     df = df[0].str.split('',expand=True)
#     df = df.drop(columns=[0, 13])
#     df = df.astype(int)

#     print(f'Power Consumption is: {get_power(df)}')
#     print(f'Life Support Rating is: {get_life_support(df)}')


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_03.txt"
    raw_data = rd(input)

    data = loi(raw_data)
    df = pd.DataFrame(data)

    print(f"PART 01: Power Consumption is: {get_power(df)}")
    print(f"PART 02: Life Support Rating is: {get_life_support(df)}")

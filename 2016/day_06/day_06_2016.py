from aoc.data import read_lines_of_data as rd

from collections import Counter


def error_corrected_message(input: list) -> str:

    transposed_input = list(map(list, zip(*input)))

    mc_message = ""
    lc_message = ""

    for letter in transposed_input:
        c = Counter(letter)
        mc_message = mc_message + c.most_common(1)[0][0]
        lc_message = lc_message + c.most_common()[-1][0][0]

    return mc_message, lc_message


if __name__ == "__main__":

    input = "day_06.txt"
    raw_data = rd(input)
    data = [list(word) for word in raw_data]

    mc, lc = error_corrected_message(data)

    print(f"PART 01: {mc}")
    print(f"PART 02: {lc}")

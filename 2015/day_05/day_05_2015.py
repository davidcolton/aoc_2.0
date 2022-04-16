from collections import Counter
from itertools import permutations
import re


class SantasList:
    def __init__(self, santa_list):
        self.__list = santa_list.split("\n")
        self.__vowels = ["a", "e", "i", "o", "u"]
        self.__naughty_strings = ["ab", "cd", "pq", "xy"]
        self.__nice_list = []
        self.__naughty_list = []

    def naught_or_nice(self):
        for word in self.__list:
            c = Counter(word)
            if any([ns in word for ns in self.__naughty_strings]):
                self.__naughty_list.append(word)
            elif (
                any([word[i] == word[i + 1] for i in range(len(word) - 1)])
                and sum(c[v] for v in ["a", "e", "i", "o", "u"]) >= 3
            ):
                self.__nice_list.append(word)
            else:
                self.__naughty_list.append(word)
        return self

    @property
    def length_nice_list(self):
        return len(self.__nice_list)


class SantasListTwo:
    def __init__(self, santa_list):
        self.__list = santa_list.split("\n")
        self.__nice_list = []
        self.__naughty_list = []

    def __check_word_first_test(self, word):
        for idx, letter in enumerate(word):
            if idx + 2 < len(word) and word[idx + 2] == letter:
                return True
        return False

    def __check_word_second_test(self, word):
        # Create a counter of all adjacent characters
        c = Counter([f"{f}{s}" for f, s in zip(word[:-1], word[1:])])
        if (
            # If the the most common pair appears more than once
            c.most_common(1)[0][1] > 1
            # There is more then one occurrence of the pair
            #     for example aaa will return a list with a single tuple
            #     whilst aabaa will return a list with 2 tuples
            and len(
                [
                    (i.start(), i.end())
                    for i in re.finditer(c.most_common(1)[0][0], word)
                ]
            )
            > 1
        ):
            return True
        else:
            False

    def naught_or_nice(self):
        for word in self.__list:

            if self.__check_word_first_test(word) and self.__check_word_second_test(
                word
            ):
                self.__nice_list.append(word)
            else:
                self.__naughty_list.append(word)
        return self

    @property
    def length_nice_list(self):
        return len(self.__nice_list)


if __name__ == "__main__":
    with open("./day_05.txt", "r") as f:
        list_to_check = f.read()

    santas_list = SantasList(list_to_check)
    santas_list.naught_or_nice()

    print(f"Part 01:\nSanta's nice list is {santas_list.length_nice_list} words long\n")

    santas_list_two = SantasListTwo(list_to_check)
    santas_list_two.naught_or_nice()

    print(
        f"Part 02:\nSanta's nice list second time is {santas_list_two.length_nice_list} words long\n"
    )

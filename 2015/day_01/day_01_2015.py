from collections import Counter
import aoc.data as d

input = "day_01.txt"


class Floor:
    def __init__(self, input: str):
        """Initialise the Floor.
        Takes a string containing the list of brackets to be processed as instructions.
        A ( bracket means move up a floor.
        A ) bracket means move down a floor.

        Args:
            input (str): The input instructions.
        """
        self.__instructions = [i for i in input]
        self.__floors_counter = Counter(input)
        self.__floor = 0
        self.__moves = 0

    @property
    def final_floor(self) -> int:
        """Simple function to calculate the final floor Santa will be on
        after following all the instructions

        Returns:
            int: The final floor number
        """
        return self.__floors_counter["("] - self.__floors_counter[")"]

    def move_up_floor(self):
        """Move up a single floor."""
        self.__floor += 1

    def move_down_floor(self):
        """Move down a single floor."""
        self.__floor -= 1

    @property
    def first_basement_visit(self) -> int:
        """Find the first time Santa visits the basement.

        The function iterates through all the input instructions keeping note
        of the current floor that Santa is in. Each time Santa moves the moves
        counter is increased.

        When the current floor is -1, the basement, the number of moves to
        reach it is returned.

        Returns:
            int: The number of moves to visit the basement.
        """
        while self.__instructions and self.__floor >= 0:
            self.__moves += 1
            inst = self.__instructions.pop(0)
            self.move_up_floor() if inst == "(" else self.move_down_floor()
        return self.__moves


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    raw_data = d.read_data(input)

    santa = Floor(raw_data)

    print(f"Part 01: Santa is on floor: {santa.final_floor}")
    print(
        f"Part 02: Santa first went to the basement on move {santa.first_basement_visit}"
    )

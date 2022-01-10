from collections import Counter, namedtuple
from typing import NoReturn
from aoc.data import read_data as rd
from aoc.data import comma_separated_strings_to_list as cs

input = "day_01.txt"


class StreetGrid:
    # The Instruction named tuple is used to allow easy access to the
    # instructions to follow.
    # It contins two items:
    #   direction: The direction to follow
    #   distance: The distance to travel in the
    Instruction = namedtuple("Instruction", ["direction", "distance"])

    # The CompassPoint named tuple is used to allow easy access to the
    # values required to move according to each instruction.
    # It contains three items:
    #   x_mul: The number of blocks to move in the x direction +1 east, -1 west
    #   y_mul: The number of blocks to move in the y direction +1 north, -1 south
    #   new_direction: After folling the Instruction the direction you'll be facing
    CompassPoint = namedtuple("CompasPoint", ["x_mul", "y_mul", "new_direction"])

    # The compass dictionary ditates how each Instruction is processed.
    # The compass has 4 keys N, E, S and W. This is the direction you are facing.
    # The value of each compass key is itself a dictionary with L & R keys.
    # The value of each L & R key is a Compass point that allow you travel through the grid.
    compass = {
        "N": {
            "L": CompassPoint(-1, 0, "W"),
            "R": CompassPoint(1, 0, "E"),
        },
        "E": {
            "L": CompassPoint(0, 1, "N"),
            "R": CompassPoint(0, -1, "S"),
        },
        "S": {
            "L": CompassPoint(1, 0, "E"),
            "R": CompassPoint(-1, 0, "W"),
        },
        "W": {
            "L": CompassPoint(0, -1, "S"),
            "R": CompassPoint(0, 1, "N"),
        },
    }

    def __init__(self, input: list) -> None:
        """Initialise the StreetGrid Class.

        The class takes a list of strings that represent the directions to the
        Bunny's Headquarters.

        The input list is converted to a list of Instruction named tuples.

        In all cases it is assumed that the starting pointion is 0,0 and facing
        North.

        Args:
            input (list): A list of string containing the instrictions to follow
        """
        self.__instructions = [self.Instruction(ins[0], int(ins[1:])) for ins in input]
        self.__facing = "N"
        self.__grid_position = [0, 0]

    def shortest_path(self, visited_twice: bool = False) -> int:
        """Follow the grid based instructions and calculate the distance from the
        starting point to the location of the Bunny's Headquarters.

        The naive way follows all instructions and the calculates the Manhatten Distance.

        The alternative way, when `visited_twice=True` calculate the distance from the
        starting point to the first block, grid, position visited twice

        Args:
            visited_twice (bool, optional): Set to True if the distance to the first
            block, grid, visited twice is the distance required. Defaults to False.

        Returns:
            int: The Manhatten Distance from the starting poistion 0,0 to the final block,
            grid, position.
        """
        facing = self.__facing
        position = self.__grid_position

        # An empty set to hold the grid positions visited
        visited = set()

        # For each instruction
        for ins in self.__instructions:

            # The grid locations visited in the execution of this instruction
            this_path = set()

            # Get the details of how this instructions move are to be executed
            move = self.compass[facing][ins.direction]

            # For each single step in the instruction
            steps = range(ins.distance)
            for _ in steps:
                # Get the next position
                position = [
                    position[0] + move.x_mul * 1,
                    position[1] + move.y_mul * 1,
                ]

                # And add it to the path
                this_path.add(tuple(position))

            # After all steps you are now facing
            facing = move.new_direction

            # Check if this path contains a grid position already visited
            if visited_twice and visited.intersection(this_path):

                # If so return the distance to this position
                position = visited.intersection(this_path).pop()
                return abs(position[0]) + abs(position[1])
            else:

                # Other add the grid position in the path to the visited set
                visited = visited | this_path

        return abs(position[0]) + abs(position[1])


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    raw_data = rd(input)

    # Convert comma separated string to list
    data = cs(raw_data)

    # Create an instance of the StreetGris Class
    s = StreetGrid(data)

    print(f"PART 01: Easter Bunny HQ is {s.shortest_path()} blocks away.")
    print(
        f"PART 02: The first location you visit twice is {s.shortest_path(visited_twice=True)} blocks away."
    )

from aoc.data import read_lines_of_data as rd
from collections import namedtuple

PathCoords = namedtuple("PathCoords", "x y dist")


class WirePath:
    def __init__(self, path: list):
        self.root = PathCoords(0, 0, 0)
        self.current = PathCoords(0, 0, 0)
        self.path = path
        self.steps = 0

        self.wire_path_coords = set()
        self.steps_taken = dict()

    def move_up(self, length: str):
        x = self.current.x
        y = self.current.y
        moves = int(length[1:])
        for n in range(1, moves + 1):
            self.steps += 1
            dist = abs(x) + abs(y + n)
            new_coords = PathCoords(x, y + n, dist)
            self.wire_path_coords.add(new_coords)
            if not new_coords in self.steps_taken.keys():
                self.steps_taken[new_coords] = self.steps
        self.current = new_coords

    def move_down(self, length: str):
        x = self.current.x
        y = self.current.y
        moves = int(length[1:])
        for n in range(1, moves + 1):
            self.steps += 1
            dist = abs(x) + abs(y - n)
            new_coords = PathCoords(x, y - n, dist)
            self.wire_path_coords.add(new_coords)
            if not new_coords in self.steps_taken.keys():
                self.steps_taken[new_coords] = self.steps
        self.current = new_coords

    def move_right(self, length: str):
        x = self.current.x
        y = self.current.y
        moves = int(length[1:])
        for n in range(1, moves + 1):
            self.steps += 1
            dist = abs(x + n) + abs(y)
            new_coords = PathCoords(x + n, y, dist)
            self.wire_path_coords.add(new_coords)
            if not new_coords in self.steps_taken.keys():
                self.steps_taken[new_coords] = self.steps
        self.current = new_coords

    def move_left(self, length: str):
        x = self.current.x
        y = self.current.y
        moves = int(length[1:])
        for n in range(1, moves + 1):
            self.steps += 1
            dist = abs(x - n) + abs(y)
            new_coords = PathCoords(x - n, y, dist)
            self.wire_path_coords.add(new_coords)
            if not new_coords in self.steps_taken.keys():
                self.steps_taken[new_coords] = self.steps
        self.current = new_coords

    def follow_path(self) -> set:
        for instruction in self.path:
            if instruction.startswith("U"):
                self.move_up(instruction)
            elif instruction.startswith("D"):
                self.move_down(instruction)
            elif instruction.startswith("L"):
                self.move_left(instruction)
            else:
                self.move_right(instruction)
        return self.wire_path_coords


def crossed_wires(wire_01: list, wire_02: list, measure="manhattan") -> int:

    coords_wire_01 = WirePath(wire_01)
    coords_wire_02 = WirePath(wire_02)

    wire_01_coords = coords_wire_01.follow_path()
    wire_02_coords = coords_wire_02.follow_path()

    intersetion_points = wire_01_coords.intersection(wire_02_coords)

    closest = min(intersetion_points, key=lambda x: x.dist)

    min_steps = 99999
    for point in intersetion_points:
        d1 = coords_wire_01.steps_taken[point]
        d2 = coords_wire_02.steps_taken[point]
        dist = d1 + d2
        min_steps = dist if dist < min_steps else min_steps

    return closest.dist, min_steps


if __name__ == "__main__":
    # Simple import
    # Single line of data imported as a string
    input = "day_03.txt"
    data = rd(input)

    # Convert comma separated string to list
    wire_01 = data[0].split(",")
    wire_02 = data[1].split(",")

    min_steps, closest = crossed_wires(wire_01, wire_02)

    print(f"PART 01: Minimum steps using Manhattan distance is: {min_steps}.")
    print(f"PART 02: Fewest combined steps are: {closest}.")

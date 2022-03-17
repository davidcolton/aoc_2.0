from aoc.data import read_data as rd


from dataclasses import dataclass
from collections import defaultdict
from itertools import cycle


class DeliveryRoute:
    def __init__(self, route, santas=1):
        self.__route_raw = route
        self.__route_list = [r for r in self.__route_raw]
        self.__points = [Point(0, 0) for n in range(santas)]
        self.__route_dict = defaultdict(int)
        for point in self.__points:
            self.__route_dict[(point.x, point.y)] += 1

    def follow_route(self):
        p = cycle(self.__points)
        for move in self.__route_list:
            point_to_move = next(p)
            point_to_move.move_point(move)
            self.__route_dict[(point_to_move.x, point_to_move.y)] += 1
        return self

    @property
    def houses_visited(self):
        return len(self.__route_dict)


@dataclass
class Point:
    x: int = 0
    y: int = 0

    def __init__(self, x=0, y=0):
        self.__movements = {
            "^": self.move_north,
            ">": self.move_east,
            "v": self.move_south,
            "<": self.move_west,
        }

    def __add__(self, point):
        self.x += point.x
        self.y += point.y
        return self

    def move_point(self, direction):
        self.__movements[direction]()

    def move_north(self):
        self.y += 1

    def move_east(self):
        self.x += 1

    def move_south(self):
        self.y -= 1

    def move_west(self):
        self.x -= 1


if __name__ == "__main__":

    input = "day_03.txt"

    # Simple import
    # Single line of data imported as a string
    data = rd(input)

    santa_route = DeliveryRoute(data)
    santa_route.follow_route()

    print(f"Part 01:\nSanta visited: {santa_route.houses_visited}\n")

    santas_route = DeliveryRoute(data, 2)
    santas_route.follow_route()

    print(f"Part 02:\n2 Santas visited: {santas_route.houses_visited}\n")

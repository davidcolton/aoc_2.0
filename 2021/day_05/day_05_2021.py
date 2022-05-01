from aoc.data import read_data as rd

import numpy as np
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    p1: Point
    p2: Point
    dir: str


def process_point(data: str):
    # Expected format x,y -> x,y
    points = data.split(" -> ")
    p1_x, p1_y = points[0].split(",")
    p2_x, p2_y = points[1].split(",")
    p1 = Point(int(p1_x), int(p1_y))
    p2 = Point(int(p2_x), int(p2_y))

    # Determine direction
    direction = ""
    if p1.x == p2.x:
        direction = "Vertical"
    elif p1.y == p2.y:
        direction = "Horizontal"
    else:
        direction = "Diagonal"

    # Create line and order points correctly
    if direction == "Horizontal" or direction == "Diagonal":
        if p1.x <= p2.x:
            return Line(p1, p2, direction)
        else:
            return Line(p2, p1, direction)
    elif direction == "Vertical":
        if p1.y <= p2.y:
            return Line(p1, p2, direction)
        else:
            return Line(p2, p1, direction)


def process_lines(data, size, include_diagonals=False):

    arr = np.zeros((size, size))

    for point in data:
        if point.dir == "Horizontal":
            x_range = range(point.p1.x, point.p2.x + 1)
            for x in x_range:
                arr[point.p1.y, x] += 1

        if point.dir == "Vertical":
            y_range = range(point.p1.y, point.p2.y + 1)
            for y in y_range:
                arr[y, point.p1.x] += 1

        if include_diagonals and point.dir == "Diagonal":
            x_range = range(point.p1.x, point.p2.x + 1)
            if point.p1.y < point.p2.y:
                y_range = range(point.p1.y, point.p2.y + 1)
            else:
                y_range = range(point.p1.y, point.p2.y - 1, -1)

            for idx, _ in enumerate(x_range):
                arr[y_range[idx], x_range[idx]] += 1

    # Replace 1's with 0s
    arr[arr == 1] = 0

    return (arr > 0).sum()


if __name__ == "__main__":

    raw_data = rd("day_05.txt")

    data = [process_point(point) for point in raw_data.strip().split("\n")]
    print(f"Part 01: {process_lines(data, 1000)}")
    print(f"Part 02: {process_lines(data, 1000, include_diagonals=True)}")

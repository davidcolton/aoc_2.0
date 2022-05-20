from aoc.data import read_data as rd
import numpy as np


class ChristmasLights:
    def __init__(self, grid_size, instructions):
        self.grid = np.zeros([grid_size, grid_size], dtype=int)
        self.instructions = [
            line.strip() for line in instructions.split("\n") if line != ""
        ]

    def process_grid_coordinates(self, s1, s2):
        x1 = int(s1.split(",")[0])
        y1 = int(s1.split(",")[1])

        # x2 & y2 are + 1 because we are using matrix slices
        #    e.g. x1, x2 = 2, 4 only returns rows 2 up to but
        #         not including row 4 i.e. rows 2 & 3 only
        x2 = int(s2.split(",")[0]) + 1
        y2 = int(s2.split(",")[1]) + 1

        return x1, x2, y1, y2

    def turn_on(self, s1, s2):
        x1, x2, y1, y2 = self.process_grid_coordinates(s1, s2)
        self.grid[x1:x2, y1:y2] = 1
        return self

    def turn_off(self, s1, s2):
        x1, x2, y1, y2 = self.process_grid_coordinates(s1, s2)
        self.grid[x1:x2, y1:y2] = 0
        return self

    def toggle(self, s1, s2):
        x1, x2, y1, y2 = self.process_grid_coordinates(s1, s2)
        self.grid[x1:x2, y1:y2] += 1
        self.grid[x1:x2, y1:y2] = self.grid[x1:x2, y1:y2] % 2
        return self

    def follow_instructions(self):
        for ins in self.instructions:
            if ins.startswith("toggle"):
                s1, _, s2 = ins[7:].split()
                self.toggle(s1, s2)
            elif ins.startswith("turn on"):
                s1, _, s2 = ins[8:].split()
                self.turn_on(s1, s2)
            else:
                s1, _, s2 = ins[9:].split()
                self.turn_off(s1, s2)
        return self

    @property
    def lights_on(self):
        return self.grid.sum()


class ChristmasLights2(ChristmasLights):
    def turn_on(self, s1, s2):
        x1, x2, y1, y2 = self.process_grid_coordinates(s1, s2)
        self.grid[x1:x2, y1:y2] += 1
        return self

    def turn_off(self, s1, s2):
        x1, x2, y1, y2 = self.process_grid_coordinates(s1, s2)
        self.grid[x1:x2, y1:y2] -= 1
        self.grid[self.grid < 0] = 0
        return self

    def toggle(self, s1, s2):
        x1, x2, y1, y2 = self.process_grid_coordinates(s1, s2)
        self.grid[x1:x2, y1:y2] += 2
        return self


if __name__ == "__main__":
    input = "day_06.txt"
    raw_data = rd(input)

    lights = ChristmasLights(1000, raw_data)
    lights.follow_instructions()
    print(f"Part 01: Number of Lights on: {lights.lights_on}")

    lights2 = ChristmasLights2(1000, raw_data)
    lights2.follow_instructions()
    print(f"Part 02: Brightness of Lights: {lights2.lights_on}")

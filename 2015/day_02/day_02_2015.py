from aoc.data import read_data as rd


class Presents:
    def __init__(self, presents):
        self.__presents_raw = presents
        self.__presents_list = [
            Present(dimensions)
            for dimensions in self.__presents_raw.split("\n")
            if dimensions != ""
        ]

    @property
    def wrap_all_presents(self):
        return sum(
            [present.calculate_wrapping_paper for present in self.__presents_list]
        )

    @property
    def ribbon_all_presents(self):
        return sum([present.calculate_ribbon for present in self.__presents_list])


class Present:
    def __init__(self, dimensions):
        self.__dimensions = dimensions.split("x")
        self.__length = int(self.__dimensions[0])
        self.__width = int(self.__dimensions[1])
        self.__height = int(self.__dimensions[2])
        self.__volume = self.__length * self.__width * self.__height
        self.__required_wrapping_paper = 0
        self.__required_ribbon = 0

    @property
    def calculate_wrapping_paper(self):
        len_by_wid = self.__length * self.__width
        len_by_hei = self.__length * self.__height
        wid_by_hei = self.__width * self.__height
        smallest = min(len_by_wid, len_by_hei, wid_by_hei)
        self.__required_wrapping_paper = (
            (len_by_wid + len_by_hei + wid_by_hei) * 2
        ) + smallest
        return self.__required_wrapping_paper

    @property
    def calculate_ribbon(self):
        return (
            sum(sorted([self.__length, self.__width, self.__height])[:2]) * 2
        ) + self.__volume


if __name__ == "__main__":

    input = "day_02.txt"

    # Simple import
    # Single line of data imported as a string
    raw_data = rd(input)

    santas_bag = Presents(raw_data)

    print(f"PART 01: Total wrapping paper: {santas_bag.wrap_all_presents}")
    print(f"PART 02: Total ribbon: {santas_bag.ribbon_all_presents}")

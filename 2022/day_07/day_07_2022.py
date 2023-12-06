from aoc.data import read_data as rd

f = open("day_07.txt")
lst = f.read().split("\n")

directories = {}
list_of_directories = []
cd = ""
for x in lst:
    if "$ cd" in x and ".." not in x:
        dir = x.removeprefix("$ cd ")
        cd += dir
        if cd not in directories:
            directories[cd] = []
        list_of_directories.append(dir)

    elif "$ cd" in x and ".." in x:
        cd = cd.removesuffix(list_of_directories[len(list_of_directories) - 1])
        list_of_directories.pop(len(list_of_directories) - 1)

    elif "$ cd" not in x and "$ ls" not in x:
        if "dir" in x:
            dir = x.removeprefix("dir ")
            directories[cd + dir] = []
        else:
            size, name = x.split()
            directories[cd].append((int(size), name))

total_size = {directory: 0 for directory in directories}

for directory in directories:
    for item in directories[directory]:
        if type(item) == tuple:
            total_size[directory] += item[0]

for key in total_size.keys():
    for directory in directories:
        if key in directory and key != directory:
            total_size[key] += total_size[directory]

# Part 1
total = 0

# Part 2
empty_space = 70_000_000 - max(total_size.values())
space_needed = 30_000_000 - empty_space
temp = []

for directory in total_size:
    # Part 1
    if total_size[directory] <= 100_000:
        total += total_size[directory]
    # Part 2
    if total_size[directory] >= space_needed:
        temp.append(total_size[directory])

print(total)
print(min(temp))


# if __name__ == "__main__":
#     # Simple import
#     # Single line of data imported as a string
#     input = "day_06.txt"
#     data = rd(input)

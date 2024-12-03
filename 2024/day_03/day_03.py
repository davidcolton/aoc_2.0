# Assisted by watsonx Code Assistant
import re

with open("input.txt", "r") as file:
    data = file.read()


# Part 1
def calculate_sum(data):
    pattern_part_01 = r"mul\((\d+),(\d+)\)"
    mul_matches = re.findall(pattern_part_01, data)

    sum = 0
    for match in mul_matches:
        sum = sum + int(match[0]) * int(match[1])

    return sum


# Part 01 Answer
print(f"Part 1: {calculate_sum(data)}")

# Part 2
# Remove newline characters from data
# For simplicity add do() at the start and "\n" at the end
# Break the data into do's and don'ts
# Drop the don'ts
# Rejoin text and calculate again

tmp_data = data.replace("\n", "")
tmp_data = "do()" + tmp_data + "\n"
tmp_data = tmp_data.replace("don't()", "\ndon't()")
tmp_data = tmp_data.replace("do()", "\ndo()")
tmp_data = re.sub(r"^don\'t\(\).*\n", "", tmp_data, flags=re.M)

# Rejoin
new_data = re.sub(r"\s+", "", tmp_data)

# Part 02 Answer
print(f"Part 2: {calculate_sum(new_data)}")

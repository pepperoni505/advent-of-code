import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    data = f.readlines()

# Part 1
horizontal_value = 0
depth = 0

for i in data:
    instruction, change = i.split(" ")
    if instruction == "forward":
        horizontal_value += int(change)
    elif instruction == "down":
        depth += int(change)
    elif instruction == "up":
        depth -= int(change)

print("Part 1: " + str(horizontal_value * depth))

# Part 2
horizontal_value = 0
depth = 0
aim = 0

for i in data:
    instruction, change = i.split(" ")
    if instruction == "forward":
        horizontal_value += int(change)
        depth += aim * int(change)
    elif instruction == "down":
        aim += int(change)
    elif instruction == "up":
        aim -= int(change)

print("Part 2: " + str(horizontal_value * depth))

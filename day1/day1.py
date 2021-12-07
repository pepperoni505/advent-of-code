import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    data = f.readlines()

# Part 1
total_increased = 0
for i, line in enumerate(data):
    if i == 0:
        continue
    if int(line) > int(data[i - 1]):
        total_increased += 1

print("Part 1: " + str(total_increased))

# Part 2

values = []
for i, line in enumerate(data):
    if len(data) > i+2:
        values.append(int(line) + int(data[i+1]) + int(data[i+2]))

total_increased = 0
for i, line in enumerate(values):
    if i == 0:
        continue
    if int(line) > int(values[i - 1]):
        total_increased += 1

print("Part 2: " + str(total_increased))
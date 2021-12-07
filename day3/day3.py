import os

def getInput():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().splitlines()
    return data

# Part 1

data = getInput()
bits = list([] for _ in range(len(data[0].strip()))) # Check the first line in data and generate a list of lists with length of first line
for i, line in enumerate(data):
    for j, character in enumerate(line.strip()):
        bits[j].append(int(character))

gamma_rate = ""
epsilon_rate = ""
for i in bits:
    if i.count(0) > i.count(1):
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"

# Convert gamma rate and epsilon rate from binary to decimal
gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print("Part 1: " + str(gamma_rate * epsilon_rate))

# Part 2

def getRating(type): # Type can either be "oxygen" or "co2".
    data = getInput()
    for i in range(len(data[0])):
        if len(data) == 1:
            break
        zero_bit_occurrences = 0
        one_bit_occurrences = 0
        for line in data:
            if line[i] == '0':
                zero_bit_occurrences += 1
            else:
                one_bit_occurrences += 1
        
        pop = []
        for j, line in enumerate(data):
            if type == "oxygen":
                if one_bit_occurrences >= zero_bit_occurrences:
                    if line[i] == '0':
                        pop.append(j)
                else:
                    if line[i] == '1':
                        pop.append(j)
            else:
                if zero_bit_occurrences <= one_bit_occurrences:
                    if line[i] == '1':
                        pop.append(j)
                else:
                    if line[i] == '0':
                        pop.append(j)
        data = [line for i, line in enumerate(data) if i not in pop]

    return data[0]

oxygen_generator_rating = int(getRating("oxygen"), 2) # Convert from binary to decimal
co2_scrubber_rating = int(getRating("co2"), 2) # Convert from binary to decimal

print("Part 2: " + str(oxygen_generator_rating * co2_scrubber_rating))
import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
    file_data = f.read().splitlines()

# Part 2

def getRating(type): # Type can either be "oxygen" or "co2".
    data = file_data
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
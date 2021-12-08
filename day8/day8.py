import os
import numpy as np

def getInput():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().splitlines()
    return data


def getuniqueAppearances():
    data = getInput()
    uniqueAppearances = 0
    for line in data:
        output_values = list(map(str, line.split(" | ")[1].split(" ")))
        for value in output_values:
            if len(value) == 2: # Digit 1
                uniqueAppearances += 1
            elif len(value) == 4: # Digit 4
                uniqueAppearances += 1
            elif len(value) == 3: # Digit 7
                uniqueAppearances += 1
            elif len(value) == 7: # Digit 8
                uniqueAppearances += 1

    return uniqueAppearances

def getDigitIntersects(digit1, digit2): # See how many places digit1 intersects with digit2
    digit1_chars = [i for i in digit1]
    digit2_chars = [i for i in digit2]
    overlaps = 0
    for digit1_char in digit1_chars:
        if digit1_char in digit2_chars:
            overlaps += 1
    return overlaps

def digitContains(digit1, digit2): # See if digit1 contains digit2
    intersects = getDigitIntersects(digit1, digit2)
    return intersects == len(digit2)

def getDigits():
    data = getInput()
    sums = 0
    for line in data:
        output_values = list(map(str, line.split(" | ")[0].split(" ")))
        known_values = {}
        unknown_values = {}
        for value in output_values:
            # Get our known digits
            if len(value) == 2: # Digit 1
                known_values[1] = "".join(sorted(value))
            elif len(value) == 4: # Digit 4
                known_values[4] = "".join(sorted(value))
            elif len(value) == 3: # Digit 7
                known_values[7] = "".join(sorted(value))
            elif len(value) == 7: # Digit 8
                known_values[8] = "".join(sorted(value))
            else:
                if len(value) not in unknown_values:
                    unknown_values[len(value)] = [value]
                else:
                    unknown_values[len(value)].append(value)
        for _, (length, values) in enumerate(unknown_values.items()):
            for value in values:
                if length == 5: # Can either be a 2, 3, or 5
                    if digitContains(value, known_values[7]): # Digit 3
                        known_values[3] = "".join(sorted(value))
                    elif getDigitIntersects(value, known_values[4]) == 3: # Digit 5
                        known_values[5] = "".join(sorted(value))
                    else: # Digit 2
                        known_values[2] = "".join(sorted(value))
                elif length == 6: # Can either be 0, 6, or 9
                    if digitContains(value, known_values[4]): # Digit 9
                        known_values[9] = "".join(sorted(value))
                    elif digitContains(value, known_values[7]): # Digit 0
                        known_values[0] = "".join(sorted(value))
                    else: # Digit 6
                        known_values[6] = "".join(sorted(value))

        inverted_values = {v: k for k, v in known_values.items()} # Turn dictionary into digit lookup
        output_values = list(map(str, line.split(" | ")[1].split(" ")))
        sum = ""
        for value in output_values:
            sum += str(inverted_values["".join(sorted(value))])
        sums += int(sum)
    
    return sums
        
        

# Part 1
print("Part 1: " + str(getuniqueAppearances()))

# Part 2
print("Part 2: " + str(getDigits()))
import os

def getInput():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().splitlines()
    return data

def getCheapestPosition(deltaFuel): # deltaFuel is change in fuel after each movement
    data = list(map(int, getInput()[0].split(",")))
    fuel_dict = {}
    for i in range(min(data), max(data)):
        total_fuel = 0
        for position in data:
            position_change = abs(position - i)
            if deltaFuel > 0:
                fuel_spent = 0
                for j in range(1, position_change + 1):
                    fuel_spent += j ** deltaFuel # Not entirely sure if this will work work deltaFuel over 1
                total_fuel += fuel_spent
            else:
                total_fuel += position_change
        fuel_dict[i] = total_fuel
    
    cheapest_position = min(fuel_dict, key=fuel_dict.get)
    return fuel_dict[cheapest_position]

# Part 1
print("Part 1: " + str(getCheapestPosition(0)))

# Part 2
print("Part 2: " + str(getCheapestPosition(1))) # Improve speed
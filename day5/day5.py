import os

def getInput():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().splitlines()
    return data

def getVents():
    data = getInput()
    coordinateDict = {}
    for i, line in enumerate(data):
        ventStart, ventEnd = line.split(" -> ")
        ventStart = list(map(int, ventStart.split(",")))
        ventEnd = list(map(int, ventEnd.split(",")))
        print(ventStart, ventEnd)
        

vents = getVents()
intersects = []
for vent in vents:
    intersects.extend(vent.getIntersects(vents))

print(len(set(intersects)))

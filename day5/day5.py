import os

def getInput():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().splitlines()
    return data

def getIntersects(lineTypes): # lineTypes can have "vertical", "horizontal", and "diagonal". Only returns lines that are in this list
    data = getInput()
    coordinateDict = {}
    for line in data:
        ventStart, ventEnd = line.split(" -> ")
        x1, y1 = list(map(int, ventStart.split(",")))
        x2, y2 = list(map(int, ventEnd.split(",")))
        
        if x1 == x2: # Vertical
            if "vertical" in lineTypes:
                sorted_y = sorted((y1, y2))
                for i in range(sorted_y[0], sorted_y[1] + 1):
                    coords = (i, x1)
                    if coords in coordinateDict:
                        coordinateDict[coords] += 1
                    else:
                        coordinateDict[coords] = 1
        elif y1 == y2: # Horizontal
            if "horizontal" in lineTypes:
                sorted_x = sorted((x1, x2))
                for i in range(sorted_x[0], sorted_x[1] + 1):
                    coords = (y1, i)
                    if coords in coordinateDict:
                        coordinateDict[coords] += 1
                    else:
                        coordinateDict[coords] = 1
        elif "diagonal" in lineTypes: # Diagonal
            sorted_x = sorted((x1, x2))
            slope = int((y2 - y1) / (x2 - x1))
            y = min(y1, y2) if slope == 1 else max(y1, y2)
            for i in range(sorted_x[0], sorted_x[1] + 1):
                coords = (y, i)
                if coords in coordinateDict:
                    coordinateDict[coords] += 1
                else:
                    coordinateDict[coords] = 1

                y += slope

    intersects = 0
    for value in coordinateDict.values():
        if value >= 2:
            intersects += 1

    return intersects

# Part 1
print("Part 1: " + str(getIntersects(["vertical", "horizontal"])))

# Part 2
print("Part 2: " + str(getIntersects(["vertical", "horizontal", "diagonal"])))

import os

def getInput():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().splitlines()
    return data

def simulateGlowfish(days):
    data = list(map(int, getInput()[0].split(",")))
    glowfish = {} # Use a dictionary to keep track of how many glowfish we have for each age. Better for memory than using a list
    for i in data:
        if i not in glowfish:
            glowfish[i] = 1
        else:
            glowfish[i] += 1

    for i in range(days):
        newGlowfish = {}
        for _, (timer, fishes) in enumerate(glowfish.items()):
            # print(age, fishes)
            if timer == 0:
                # Reset timer
                if 6 in newGlowfish:
                    newGlowfish[6] += fishes
                else:
                    newGlowfish[6] = fishes

                # Spawn new fishes
                if 8 in newGlowfish:
                    newGlowfish[8] += fishes
                else:
                    newGlowfish[8] = fishes
            else:
                # Remove 1 from timer
                if timer - 1 in newGlowfish:
                    newGlowfish[timer - 1] += fishes
                else:
                    newGlowfish[timer - 1] = fishes
        
        glowfish = newGlowfish

    return sum(glowfish.values())

# Part 1
print("Part 1: " + str(simulateGlowfish(80)))

# Part 2
print("Part 2: " + str(simulateGlowfish(256)))
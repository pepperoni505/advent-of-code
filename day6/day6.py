import os

def getInput():
    with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as f:
        data = f.read().splitlines()
    return data


class Lanternfish:

    def __init__(self, internal_timer):
        self.internal_timer = internal_timer
        self.children = []

    def createNewLanternfish(self):
        newFish = Lanternfish(8)
        self.children.append(newFish)

    def tick(self):
        if self.internal_timer == 0:
            self.internal_timer = 6
            self.createNewLanternfish()
        else:
            self.internal_timer -= 1

    def getChildren(self):
        children = self.children
        for child in self.children:
            children.extend(child.getChildren())

        return children



ages = list(map(int, getInput()[0].split(",")))

lantenfishes = []
for age in ages:
    fish = Lanternfish(age)
    lantenfishes.append(fish)

for i in range(17):
    for fish in lantenfishes:
        fish.tick()

total_fish = 0
for fish in lantenfishes:
    total_fish += len(fish.getChildren())

print(total_fish)
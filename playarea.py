#for testing
import random


area = []


count = 0

while count < 10:
    count = count + 1
    randomArea = random.randint(0, 2)

    if randomArea == 2:
        area.append([0,0])
    elif randomArea == 1:
        area.append([0])
    else:
        area.append(randomArea)

print(area)
from collections import defaultdict

def movement(x, y, char):
    if char == "^":
        y += 1
    elif char == ">":
        x += 1
    elif char == "v":
        y -= 1
    elif char == "<":
        x -= 1
    return x,y

x = 0
y = 0
x_robo = 0
y_robo = 0
houses = defaultdict(int)

with open("input3.txt") as f:
    i = 0
    for char in f.read():
        # santa
        if i % 2 == 0:
            houses[(x,y)] += 1
            x, y = movement(x, y, char)
        # robo-santa
        if i % 2 == 1:
            houses[(x_robo, y_robo)] += 1
            x_robo ,y_robo = movement(x_robo, y_robo, char)
        i += 1

    houses[(x,y)] += 1
    houses[(x_robo,y_robo)] += 1
    print(len(houses))


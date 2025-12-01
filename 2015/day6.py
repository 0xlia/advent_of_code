
# 1mio lights
lights = [[0 for _ in range(1000)] for _ in range(1000)]

with open ("input6.txt") as f:
    for line in f:

        status = "off"
        if line.startswith("turn off"):
            status = "off"
            line = line.split()[2:]
        elif line.startswith("turn on"):
            status = "on"
            line = line.split()[2:]
        elif line.startswith("toggle"):
            status = "toggle"
            line = line.split()[1:]
        c1 = line[0].split(",")
        x1 = int(c1[0])
        y1 = int(c1[1])
        c2 = line[2].split(",")
        x2 = int(c2[0])
        y2 = int(c2[1])

        if status == "off":
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] -= 1 
                    if lights[x][y] < 0:
                        lights[x][y] = 0
        elif status == "on":
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] += 1
        else: 
            for x in range(x1, x2+1):
                for y in range(y1, y2+1): 
                    lights[x][y] += 2

lit = 0
for i in lights:
    lit += sum(i)

print(lit)
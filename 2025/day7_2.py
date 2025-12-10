from collections import defaultdict

# empty space
space = []

# fill space
with open("input7.txt") as f:
    for line in f.readlines():
        space.append([char for char in line.strip() ])


# find first beam
beams = {}
beams[space[0].index("S")] = 1
print(beams)


# move through space
for y in range(len(space)):
    new_beams = defaultdict(int)
    for key, value in beams.items():
        # move downward
        if space[y][key] != "^":
            new_beams[key] += value
        # split
        else:
            new_beams[key -1] += value
            new_beams[key +1] += value
    beams = new_beams

print(beams)

print(sum(beams.values()))

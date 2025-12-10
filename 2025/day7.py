# empty space
space = []

# fill space
with open("input7.txt") as f:
    for line in f.readlines():
        space.append([char for char in line.strip() ])
print(space)

# find first beam
beams = {space[0].index("S")}
print(beams)

total_splits = 0 

# move through space
for y in range(len(space)):
    new_beams = set()
    for beam in beams:
        # move downward
        if space[y][beam] != "^":
            new_beams.add(beam)
        # split beam
        else:
            total_splits += 1
            new_beams.add(beam-1)
            new_beams.add(beam+1)
    beams = new_beams

print(total_splits)
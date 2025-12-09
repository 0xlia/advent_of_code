# empty space
space = []

# fill space
with open("input7.txt") as f:
    for line in f.readlines():
        space.append([char for char in line.strip() ])
print(space)

# find first beam
beams = {(0, space[0].index("S"))}
print(beams)

total_splits = 0 

# move through space
for _ in space:
    new_beams = set()
    for beam in beams:
        # move downward
        if space[beam[0]][beam[1]] != "^":
            new_beams.add((beam[0]+1, beam[1]))
        # split beam
        else:
            total_splits += 1
            new_beams.add((beam[0]+1, beam[1]-1))
            new_beams.add((beam[0]+1, beam[1]+1))
    beams = new_beams

print(total_splits)
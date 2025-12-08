def adjacent_rolls(y,x,layout):
    adjacent_rolls = 0

    # [y+1][x-1], [y+1][x], [y+1][x+1]
    if layout[y+1][x-1] == '@': adjacent_rolls += 1
    if layout[y+1][x  ] == '@': adjacent_rolls += 1
    if layout[y+1][x+1] == '@': adjacent_rolls += 1

    # [y  ][x-1], [y  ][x], [y  ][x+1]
    if layout[y  ][x-1] == '@': adjacent_rolls += 1
    if layout[y  ][x+1] == '@': adjacent_rolls += 1

    # [y-1][x-1], [y-1][x], [y-1][x+1]
    if layout[y-1][x-1] == '@': adjacent_rolls += 1
    if layout[y-1][x  ] == '@': adjacent_rolls += 1
    if layout[y-1][x+1] == '@': adjacent_rolls += 1

    return adjacent_rolls < 4


# parse printing department layout
layout = []
accessible_rolls = 0

with open("input4.txt") as f:

    for line in f.readlines():
        row = ["."] + [char for char in line.strip()] + ["."]
        layout.append(row)
    
    empty_row = ["." for i in range(len(layout[0]))]
    layout = [empty_row] + layout + [empty_row]

print(layout)

roll_removed = True

while(roll_removed):
    roll_removed = False
    for y in range(1, len(layout)-1):
        for x in range(1, len(layout[y])-1):
            if layout[y][x] == '@':
                if adjacent_rolls(y,x,layout):
                    layout[y][x] = "x"
                    accessible_rolls += 1
                    roll_removed = True

print(layout)
print(accessible_rolls)
        




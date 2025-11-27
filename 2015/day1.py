floor = 0
position = 1
update_position = True

with open("input1.txt") as f:
    for char in f.read():
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        if floor == -1:
            update_position = False
        if update_position:
            position += 1

print("floor:", floor)
print("position:", position)
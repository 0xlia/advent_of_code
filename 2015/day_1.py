# Santa needs to find the floor he needs to be on. 
# He starts on floor 0.

# get input from file
floor = 0
position = 1
f = open("input_1.txt", "r")
for char in f.read():
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    if floor == -1:
        break
    position += 1

# first time he enters basement
print(position)


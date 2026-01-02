from collections import defaultdict
import numpy as np


def array_in_list(a, l):
    for b in l:
        if np.array_equal(a, b) == True:
            return True
    return False


presents = defaultdict(list)
present_sizes = {}
regions = []


with open("input12.txt") as f:
    
    current_present = 0 
    for line in f.readlines():
        line = line.strip()
        # store presents in dict
        if line.endswith(":"):
            current_present = int(line[0])
        elif line.startswith("#") or line.startswith("."):
            present_line = []
            for char in line:
                if char == "#":
                    present_line.append(1)
                else:
                    present_line.append(0)
            presents[current_present].append(present_line)
        elif line == "":
            continue
        else:
            regions.append(line.split(":"))


# store present variations
for i in presents.keys():
    present_sizes[i] = np.sum(presents[i])
    present_variations = []
    present = np.array(presents[i])
    present_flip = np.fliplr(present)

    # flip
    present_variations.append(present)
    present_variations.append(present_flip)

    # rotate
    for j in range (1, 4):
        present_variations.append(np.rot90(present, j))
        present_variations.append(np.rot90(present_flip, j))
    
    unique_variations = []
    for var in present_variations:
        if not array_in_list(var, unique_variations):
            unique_variations.append(var)  
    
    presents[i] = unique_variations
    

print(presents)

valid_regions = 0

for region in regions:
    # region[0] -> dimensions
    x, y = region[0].split("x")
    size = int(x) * int(y)
    
    # region[1] -> quantities
    gifts = region[1].strip().split(" ")
    
    # total size 
    total = 0
    for i in range(len(gifts)):
        quantity = int(gifts[i])
        total += quantity * present_sizes[i]

    if size >= total:
        valid_regions += 1
    
    print(size, total)
print(len(regions), valid_regions)

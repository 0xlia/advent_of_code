from heapq import heappush, heappop

# fresh and spoiled ingredients
# ranges of fresh ingredients
# 
# available ingredients
# -> number of fresh ingredients


fresh_ingredients = []
available_ingredients = []
ranges = True

with open("input5.txt") as f:
    for line in f.readlines():
        if line.strip() == "":
            ranges = False
        
        # get fresh ingredient ranges as list of tuples
        elif ranges:
            start, end = line.strip().split("-")
            fresh_ingredients.append((int(start), int(end)))
        # get available ingredients bu
        elif not ranges:
            available_ingredients.append(int(line.strip()))
    
# sort fresh ingredients 
fresh_ingredients.sort()
print(fresh_ingredients)

# part 1: number of fresh ingredients
fresh = 0
for ingredient in available_ingredients:
    for start, stop in fresh_ingredients:
        if ingredient >= start and ingredient <= stop:
            fresh += 1
            break

print(fresh)

# part 2: number if fresh ids 
ids = 0 
current_id = 0 

for start, stop in fresh_ingredients:
    if start > current_id:
        ids += stop - start + 1
    elif current_id > stop:
        continue
    else: 
        ids += stop - current_id
    current_id = stop


print("Number of fresh Ids:", ids)




# (3,5), (10,14), (12,18), (16,20), 
#  i start <= i+1 start <= istop
#       istop <= i+1 stop
#       stop = max(istop, i+1stop)
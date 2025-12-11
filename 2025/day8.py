from math import sqrt

# straight line distance between two boxes
def distance(p, q):
    
    distance = 0 
    if len(p) != len(q):
        raise ValueError("unable to compute distance: len(p) = ", len(p), ", len(q) = ", len(q))

    for i in range(len(p)):
        distance += (q[i]-p[i])**2

    return sqrt(distance)

# search box in circuits
# return circuit indexes
def circuit_search(box0, box1, circuits):
    box0_circuit_index = None
    box1_circuit_index = None
    for i in range(len(circuits)):
        if box0 in circuits[i]:
            box0_circuit_index = i
        if box1 in circuits[i]:
            box1_circuit_index = i
    return box0_circuit_index, box1_circuit_index


# box = (x,y,z)
boxes = []

with open("input8.txt") as f:
    for line in f.readlines():
        coordinates = line.strip().split(",")
        print(coordinates)
        x,y,z = map(int,coordinates)
        boxes.append((x,y,z))


# create list of distances (box1_index, box2_index, distance)
distances = []
for p in range(len(boxes)):
    # q < p
    for q in range(p):
        distances.append((p, q, distance(boxes[p], boxes[q])))

# sort distances (box0_index, box1_index, distance)
distances = sorted(distances, key=lambda distance: distance[2])
# print(distances)

# circuits
circuits = []
answer2 = 0 

for box0, box1, _ in distances:
    # get circuit index or None 
    box0_circuit_index, box1_circuit_index = circuit_search(box0, box1, circuits)

    # new circuit
    if box0_circuit_index is None and box1_circuit_index is None:
        circuits.append({box0, box1})
    # add to existing circuit
    elif box0_circuit_index is None and box1_circuit_index is not None:
        circuits[box1_circuit_index].add(box0)
    elif box0_circuit_index is not None and box1_circuit_index is None:
        circuits[box0_circuit_index].add(box1)
    # merge circuits
    elif box0_circuit_index is not None and box1_circuit_index is not None:
        if box0_circuit_index == box1_circuit_index:
            continue
        circuit0 = circuits[box0_circuit_index]
        circuit1 = circuits[box1_circuit_index]
        new_circuit = circuit0.union(circuit1)
        # print("union:", circuit0, circuit1, new_circuit)
        circuits.remove(circuit0)
        circuits.remove(circuit1)
        circuits.append(new_circuit)

    if len(circuits[0]) == len(boxes):
        x0 = boxes[box0][0]
        x1 = boxes[box1][0]
        answer2 = x0 * x1
        print("Part2:", x0, x1, answer2)
        print(circuits)
        break 


# sort circuits by len 
circuits.sort(key=lambda circuits: len(circuits), reverse=True)

answer = 1

for c in circuits[:3]:
    answer *= len(c)
print("Part1:", answer)
import re 

sum_invalid_ids = 0

# elfen sind stupid und haben database zerschossen 
# wir müssen invalid IDs finden
# invalid id: 446446 <- erster part der id entspricht dem 2. part


with open("input2.txt") as f:
    # parse puzzle input 
    ranges = f.read().split(",")

    # iterate over list of ranges
    for ra in ranges:
        # get first and last id
        ids = ra.split("-")
        first_id = int(ids[0])
        last_id = int(ids[1])

        # iterate over ids
        i = first_id
        for i in range(first_id, last_id+1):
            current_id = str(i)
            match = re.match(r'^(.+)\1+$', current_id)
            if match != None:
                sum_invalid_ids += i
            


print(sum_invalid_ids)
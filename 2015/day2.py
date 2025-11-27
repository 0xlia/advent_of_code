wrapping_paper = 0
ribbon = 0

with open("input2.txt") as f:
    for line in f.readlines():
        # get l, w, h 
        dimensions = line.split("x")
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2].strip())

        # wrapping paper: 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
        smallest_side = min(l*w, l*h, w*h)
        wrapping_paper += 2*l*w + 2*w*h + 2*h*l + smallest_side
        
        # ribbon: 2*smallest_dim + 2*second_smallest_dim + l*w*h
        dimensions = [l,w,h]
        dimensions.sort()
        ribbon += 2*dimensions[0] + 2*dimensions[1] + l*w*h
        

print("wrapping paper:", wrapping_paper)
print("ribbon:", ribbon)
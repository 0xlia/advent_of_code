puzzle = str(1113222113)

for _ in range(50):
    new_puzzle = ""
    i = 0
    while i < len(puzzle):
        j = i+1
        if j < len(puzzle):
            while(puzzle[j] == puzzle[i]):
                j += 1
                if j >= len(puzzle):
                    break
        new_puzzle += str(j-i) + puzzle[i]
        i = j 
    print(new_puzzle)
    puzzle = new_puzzle
        
print(len(puzzle))


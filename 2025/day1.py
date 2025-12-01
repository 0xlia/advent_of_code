dial = 50
password = 0

with open("input1.txt") as f:
    for line in f.readlines():
        direction = line[0]
        password += int(line[1:]) // 100
        clicks = int(line[1:]) % 100
        original_dial = dial

        if direction == "L":
            dial -= clicks

            if dial <= 0 and original_dial != 0:
                password += 1
            if dial < 0:
                dial += 100

        elif direction == "R":
            dial += clicks 
            if dial >= 100 or (dial == 0 and original_dial != 0):
                password += 1
            dial %= 100
        
        print(line, "og_dial:", original_dial, "dial:", dial, "password:", password)
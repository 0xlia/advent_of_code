total_joltage = 0

with open("input3.txt") as f:
    for line in f.readlines():
        # list of batteries
        batteries = [int(char) for char in line.strip()]
        print(batteries)

        power = 0
        last_index = 0

        for digit in range(11,-1, -1):
            print("looking for digit nr:", digit)
            # search next biggest battery in last battery | .... | number of remaining digits
            value = max(batteries[last_index:(len(batteries) - digit)])
            # get index (add last index! important!!!)
            index = last_index + batteries[last_index:].index(value)
            last_index = index +1
            print("index:", index, "value:", value, "last index:", last_index)
            # left shift of digit 
            power += pow(10, digit) * value
        
        total_joltage += power

print(total_joltage)          
        




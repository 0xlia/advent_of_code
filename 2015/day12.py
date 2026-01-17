

with open("input12.txt") as f:
    result = 0
    current_int = 0
    neg = False


    file_content = f.read()
    for c in file_content:
        if ord('0') <= ord(c) <= ord('9'):
            current_int *= 10
            current_int += int(c)
        elif c == '-':
            neg = True
            
        else:
            if neg:
                result -= current_int
            else:
                result += current_int
            neg = False
            current_int = 0


print(result)
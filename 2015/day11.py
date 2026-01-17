# ASCII a-z 97-122

def increment_pw(pw):
    # string to ascii array
    pw_ascii = [ord(c) for c in pw]

    # increment
    for i in range(len(pw)-1, 0, -1):
        if pw_ascii[i] == ord('z'):
            pw_ascii[i] = ord('a')
        else:
            pw_ascii[i] += 1
            break

    # ascii array to string
    inc_pw = ""
    for c in pw_ascii:
        inc_pw = inc_pw + chr(c)
    return inc_pw

def pw_check_oil(pw):
    """
    >>> pw_check_oil("abc")
    True
    >>> pw_check_oil("ight")
    False
    >>> pw_check_oil("loi")
    False
    >>> pw_check_oil("otter")
    False
    """
    return not ('o' in pw or 'i' in pw or 'l' in pw)

def pw_check_straight(pw):
    """
    >>> pw_check_straight("abcdefgh")
    True
    >>> pw_check_straight("uiobghzr")
    False
    >>> pw_check_straight("zkpbhpoz")
    False
    >>> pw_check_straight("qwestula")
    True
    """
    # string to ascii array
    pw_ascii = [ord(c) for c in pw]
    # i:0-5
    for i in range(len(pw_ascii)-2):
        if pw_ascii[i+2]-2 == pw_ascii[i+1]-1 == pw_ascii[i]:
            return True 

    return False 

def pw_check_twopairs(pw):
    """
    >>> pw_check_twopairs("aaaaiuop")
    True
    >>> pw_check_twopairs("aakjhbbu")
    True
    >>> pw_check_twopairs("bbblhjkl")
    False
    >>> pw_check_twopairs("kjhhmnbb")
    True
    """
    # ..aa..bb..
    #kkll..
    #.aaaa...
    pairs = []
    # i = [0-6]
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1]:
            pairs.append(i)
    
    # print(pairs)
    
    if len(pairs) == 2:
        return not abs(pairs[0]-pairs[1]) == 1 
    elif len(pairs) >= 3:
        return True
    return False
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # current_pw = "hepxcrrq"
    current_pw = increment_pw("hepxxyzz")


    while not (pw_check_oil(current_pw) and pw_check_straight(current_pw) and pw_check_twopairs(current_pw)):
        current_pw = increment_pw(current_pw)
    
    print(current_pw)



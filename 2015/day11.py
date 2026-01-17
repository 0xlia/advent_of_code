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






current_pw = "hepxcrrz"
print(increment_pw(current_pw))



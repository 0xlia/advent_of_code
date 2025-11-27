import hashlib

puzzle_input = "yzbqklnj"
secret_key = 0


while True:
    pisk = puzzle_input + str(secret_key)
    if hashlib.md5(pisk.encode()).hexdigest().startswith("0"*6):
        break
    secret_key += 1

print(secret_key)


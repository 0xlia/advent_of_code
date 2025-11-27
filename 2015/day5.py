import re 

# at least three vowels
vowels_regex  = "(.*[aeiou].*){3,}"
# at least one letter that appears twice in a row
double_regex  = r'((.)\2)'
# not contain: "ab", "cd", "pq", "xy"
naughty_regex = "(.*(ab)|(cd)|(xy)|(pq).*)"

# contains pair of 2 letters that appear twice without overlapping
pair_regex = r'(([a-z][a-z]).*\2)'
# contains letter which repeats with exacly 1 letter between them
letter_regex = r'(([a-z]).\2)'

nice = 0

with open("input5.txt") as f:
    for line in f.readlines():
        #if re.search(vowels_regex, line) and re.search(double_regex, line) and not re.search(naughty_regex, line):
        if re.search(pair_regex, line) and re.search(letter_regex, line):    
            nice += 1
            print(line)

print(nice)
        


        
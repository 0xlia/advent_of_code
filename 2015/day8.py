import re


code = 0
memory = 0 

with open("input8.txt") as f:
    for line in f.readlines():
        line = line.strip()
        code += len(line)
        print(len(line))

        #line = line[1:-1]
        line = line.replace("\\", "\\\\")
        line = line.replace("\"", "\\\"")
        #for match in re.findall(r'\\x..', line):
        #    line = line.replace(match, ".")
        line = "\"" + line + "\""
        memory += len(line)
        print(line, len(line))

print(memory-code)

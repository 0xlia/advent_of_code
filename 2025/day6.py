

with open("input6.txt") as f:
    lines = f.readlines()

term0 = lines[0].strip().split()
term0 = [int(x) for x in term0 if x != ""]
term1 = lines[1].strip().split(" ")
term1 = [int(x) for x in term1 if x != ""]
term2 = lines[2].strip().split(" ")
term2 = [int(x) for x in term2 if x != ""]
term3 = lines[3].strip().split(" ")
term3 = [int(x) for x in term3 if x != ""]
operators = lines[-1].strip().split(" ")
operators = [x for x in operators if x != ""]

number_of_results = len(operators)

# Part 1
results = []

for i in range(0, number_of_results):
    if operators[i] == "*":
        result = term0[i] * term1[i] * term2[i] * term3[i]
    else:
        result = term0[i] + term1[i] + term2[i] + term3[i]
    results.append(result)

total = 0
for result in results:
    total += result

print(total)


# Part 2
array0 = [char for char in lines[0].replace('\n', "")]
array1 = [char for char in lines[1].replace('\n', "")]
array2 = [char for char in lines[2].replace('\n', "")]
array3 = [char for char in lines[3].replace('\n', "")]
operators = [char for char in lines[-1].replace('\n', "")]

current_operator = ""
current_terms = []
results = 0 

for i in range(len(operators)):
    # neue operation 
    if operators[i] != " ":
        result = 0
        print(current_terms)
        # vorherige rechenaufgabe lösen 
        # addition 
        if current_operator == "+":
            for term in current_terms[0:-1]:
                result += int(term.strip())
        # mult
        elif current_operator == "*":
            result = 1 
            for term in current_terms[0:-1]:
                result *= int(term.strip())
        results += result
        # new operator & reset terms
        current_operator = operators[i]
        current_terms = []
    # add neue zahl 
    current_terms.append(array0[i] + array1[i] + array2[i] + array3[i])
    
# addition 
if current_operator == "+":
    result = 0 
    for term in current_terms:
        result += int(term.strip())
    print(result)
# mult
elif current_operator == "*":
    result = 1 
    for term in current_terms:
        result *= int(term.strip())
    print(result)
results += result

print(results)
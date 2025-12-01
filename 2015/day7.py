from typing import NamedTuple
from enum import Enum


def AND(source0, source1, target):
    if target in variables:
        return
    if source0 in variables: 
        source0 = int(variables[source0])
    if source1 in variables:
        source1 = int(variables[source1])
    variables[target] = int(source0) & int(source1) & 0xFFFF

def OR(source0, source1, target):
    if target in variables:
        return
    if source0 in variables: 
        source0 = int(variables[source0])
    if source1 in variables:
        source1 = int(variables[source1])
    variables[target] = int(source0) | int(source1) & 0xFFFF

def LSHIFT(source0, source1, target):
    if target in variables:
        return
    if source0 in variables: 
        source0 = int(variables[source0])
    if source1 in variables:
        source1 = int(variables[source1])
    variables[target] = int(source0) << int(source1) & 0xFFFF

def RSHIFT(source0, source1, target):
    if target in variables:
        return
    if source0 in variables: 
        source0 = int(variables[source0])
    if source1 in variables:
        source1 = int(variables[source1])
    variables[target] = int(source0) >> int(source1) & 0xFFFF

def NOT(source, target):
    if target in variables:
        return
    if source in variables:
        source = variables[source]
    variables[target] = ~int(source) & 0xFFFF

# 123 -> x
# a -> x
def assign(source, target):
    if target in variables:
        return
    # source is variable
    if source in variables:
        variables[target] = variables[source]
    # source is int
    else:
        variables[target] = int(source)

binary_functions = {
    "AND": AND,
    "OR": OR,
    "LSHIFT": LSHIFT,
    "RSHIFT": RSHIFT,
}

unary_functions = {
    "NOT": NOT, 
    "assign": assign,
}

class BinaryInstruction(NamedTuple):
    instruction: str
    source0: str
    source1: str
    target: str

class UnaryInstruction(NamedTuple):
    instruction: str
    source: str
    target: str

####
variables = {}
instructions = []

# create instructions list with BinaryInstructions and UnaryInstructions
with open("input7.txt") as f:
    for line in f.readlines():
        splitted = line.split()
        if splitted[1] in binary_functions:
            instructions.append(BinaryInstruction(splitted[1], splitted[0], splitted[2], splitted[4]))
        elif "NOT" in splitted:
            instructions.append(UnaryInstruction(splitted[0], splitted[1], splitted[3]))
        else:
            instructions.append(UnaryInstruction("assign", splitted[0], splitted[2]))

instructions_backup = instructions.copy()

while len(instructions) != 0:
    for instruction in instructions:
        # AND, OR, LSHIFT, RSHIFT
        if type(instruction) is BinaryInstruction:
            
            if (instruction.source0.isdigit() or instruction.source0 in variables) and (instruction.source1.isdigit() or instruction.source1 in variables):
                binary_functions[instruction.instruction](instruction.source0, instruction.source1, instruction.target)
                instructions.remove(instruction)
        # NOT, assign 
        if type(instruction) is UnaryInstruction:

            if (instruction.source.isdigit() or instruction.source in variables):
                unary_functions[instruction.instruction](instruction.source, instruction.target)
                instructions.remove(instruction)

a = variables["a"]
variables = { "b": a}
print(variables)
instructions = instructions_backup.copy()

while len(instructions) != 0:
    for instruction in instructions:
        # AND, OR, LSHIFT, RSHIFT
        if type(instruction) is BinaryInstruction:
            
            if (instruction.source0.isdigit() or instruction.source0 in variables) and (instruction.source1.isdigit() or instruction.source1 in variables):
                binary_functions[instruction.instruction](instruction.source0, instruction.source1, instruction.target)
                instructions.remove(instruction)
        # NOT, assign 
        if type(instruction) is UnaryInstruction:

            if (instruction.source.isdigit() or instruction.source in variables):
                unary_functions[instruction.instruction](instruction.source, instruction.target)
                instructions.remove(instruction)

print(variables["a"])
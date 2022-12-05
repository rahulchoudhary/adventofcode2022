from dis import Instruction
import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "input.txt")
#lines = os.path.join(dir_path, "test.txt")
f = open(lines)

count = 0;

# Test input
#stack_1 = ['Z', 'N']
#stack_2 = ['M', 'C', 'D']
#stack_3 = ['P']

#stacks = {'1': stack_1, '2': stack_2, '3': stack_3}

# Main input
stack_1 = ['L', 'N', 'W', 'T', 'D']
stack_2 = ['C', 'P', 'H']
stack_3 = ['W', 'P', 'H', 'N', 'D', 'G', 'M', 'J']
stack_4 = ['C', 'W', 'S', 'N', 'T', 'Q', 'L']
stack_5 = ['P', 'H', 'C', 'N']
stack_6 = ['T', 'H', 'N', 'D', 'M', 'W', 'Q', 'B']
stack_7 = ['M', 'B', 'R', 'J', 'G', 'S', 'L']
stack_8 = ['Z', 'N', 'W', 'G', 'V', 'B', 'R', 'T']
stack_9 = ['W', 'G', 'D', 'N', 'P', 'L']

stacks = {'1': stack_1, '2': stack_2, '3': stack_3, '4': stack_4, '5': stack_5, '6': stack_6, '7': stack_7, '8': stack_8, '9': stack_9}


instructions = False

pattern = r"[0-9]+"

def move (items, src, target):
    i = 0
    TMP_STACK = []
    while i < int(items):
        src_stack = stacks.get(src)
        TMP_STACK.append(src_stack.pop())
        i+=1
    i = 0
    print(TMP_STACK)
    while i < int(items):
        tgt_stack = stacks.get(target)
        tgt_stack.append(TMP_STACK.pop())
        i+=1

for i in f.readlines():
    if (not instructions and i.startswith("move")):
        instructions = True

    if instructions:
        #Implement movements
        instruction = re.findall(pattern, i)
        print(instruction)
        move(instruction[0], instruction[1], instruction[2])

print(stacks)
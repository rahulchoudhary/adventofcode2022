import os
from tkinter import CURRENT

dir_path = os.path.dirname(os.path.realpath(__file__))
#filepath = os.path.join(dir_path, "test.txt")
filepath = os.path.join(dir_path, "input.txt")
f = open(filepath)

# Part 1
# Identify the max calorie carried by any elf

#max = 0
#currentElf = 0
#for i in f.readlines():
#    if (i == '\n'):
#        #new elf
#        if currentElf > max:
#            max = currentElf
#        currentElf = 0
#    else:
#        currentElf += int(i)
#print("Max calorie carried by any elf are {}".format(max))

# Part 2
# Identify the max calorie carried by top three elfs
max = [0,0,0]
currentElf = 0

for i in f.readlines():
    if (i == '\n'):
        print("new elf")
        if (min(max) < currentElf):
            max[max.index(min(max))] = currentElf
            print("new max {}", max)
        currentElf = 0
    else:
        currentElf = currentElf + int(i)

print(sum(max))
import os

print(os.getcwd())

#file = open(os.path.join(os.getcwd(), 'lines.txt'), 'r')

dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "input.txt")
f = open(lines)

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
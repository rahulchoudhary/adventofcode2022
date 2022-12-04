import os

dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "input.txt")
#lines = os.path.join(dir_path, "test.txt")
f = open(lines)

count = 0;

for i in f.readlines():
    #print(i)
    elfs_ranges = i.split(",")
    elf1_s = int(elfs_ranges[0].split("-")[0])
    elf1_e = int(elfs_ranges[0].split("-")[1])
    elf2_s = int(elfs_ranges[1].split("-")[0])
    elf2_e = int(elfs_ranges[1].split("-")[1])

    if (elf1_s >= elf2_s and elf1_s <= elf2_e) or (elf1_e >= elf2_s and elf1_e <= elf2_e) or (elf2_s >= elf1_s and elf2_s <= elf1_e) or (elf2_e >= elf1_s and elf2_e <= elf1_e):
        count += 1
        print ("found submerged {0}-{1},{2}-{3}".format(elf1_s, elf1_e, elf2_s, elf2_e))

print(count)
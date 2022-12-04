
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "input.txt")
f = open(lines)

print(ord("a"), ord("A"))

sum = 0
counter = 0
three = ["", "", ""]

for i in f.readlines():
    if (counter%3 == 0):
        #reset
        three[0] = three[1] = three[2] = ""
        print("Group {}".format(counter//3))
    three[counter%3] = i
    if (counter%3 == 2):
        #do compa
        result = ""
        for char in three[0]:
            if char in three[1] and not char in result:
                result += char

        for char in result:
            if char in three[2]:
                #add in the sum
                print("Found badge {}".format(char))
                if ord(char) < 97:
                    print(ord(char) - 38)
                    sum += (ord(char) - 38)
                else:
                    print(ord(char) - 96)
                    sum += (ord(char) - 96)
                break;
    counter+=1
    
print (sum)
#for i in f.readlines():
#    #print(i)
#    s1 = i[:len(i)//2]
#    s2 = i[len(i)//2:]
#    print(s1,s2)
#    result = ""
#    for char in s1:
#        if char in s2 and not char in result:
#            result += char
#            if ord(char) < 97:
#                sum += (ord(char) - 38)
#            else:
#                sum += (ord(char) - 96)
#            break

#    print("Repeat char is {}".format(result))

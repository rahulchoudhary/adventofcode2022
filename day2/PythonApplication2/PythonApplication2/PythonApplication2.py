import math
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
lines = os.path.join(dir_path, "input.txt")
f = open(lines)

score = 0;
items = {'X': 0, 'Y': 3, 'Z': 6}
index = {'A': 1, 'B': 2, 'C': 3}

for i in f.readlines():
    round = i.split()
    score += items.get(round[1]) #Increase based on whether you won or lost or drew

    if items.get(round[1]) == 0:
        #logic
        my_score = index.get(round[0]) - 1
        if (my_score == 0):
            my_score = 3
        score += my_score
    elif items.get(round[1]) == 3:
        score += index.get(round[0]) #same as opponent
    else:
        my_score = index.get(round[0]) + 1
        if (my_score > 3):
            my_score = 1
        score += my_score
    ### diff = items.get(round[1]) - index.get(round[0])
    #print("Opponent - {0} vs Mine - {1} hence diff {2}".format(index.get(round[0]), items.get(round[1]), diff))
    #if (diff == 0):
    #    score += 3
    #elif (diff == 1 or diff == -2):
    #    score += 6
    #elif (diff == -1 or diff == 2):
    #    score += 0


print(score)
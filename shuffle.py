import random
f = open("imaged.lines", "r")
lines = f.read().split("\n")

#simple swap shuffle
for i in range(len(lines)):
    rand = random.randint(0, len(lines)-1)
    linestemp = lines[rand]
    lines[rand] = lines[i]
    lines[i] = linestemp

#output to shuffled.lines
f = open("shuffled.lines", "w")
for i in lines:
    f.write(i+"\n")

import math
data = open("Day1Data.txt", "r")
sum = 0

if data.mode == "r":
    test = data.read()
    templist = test.split()
    intlist = list(map(int, templist))

for i in intlist:
    temp = (i/3)
    x = math.trunc(temp)
    x = x -2
    sum = sum + x

print(sum)
import fileinput
 
filename = 'inputs/1.txt'

list1 = []
list2 = []

for line in fileinput.input(files=filename):
    lineValues = line.split("   ")
    list1.append(int(lineValues[0]))
    list2.append(int(lineValues[1]))

list1.sort()
list2.sort()
totalSum = 0
for idx in range(len(list1)):
    totalSum += abs(int(list1[idx]) - int(list2[idx]))

print(totalSum)






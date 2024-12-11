import fileinput
from collections import defaultdict
 
filename = 'inputs/1.txt'

lValues = []
rDict = defaultdict(int)

for line in fileinput.input(files=filename):
    lineValues = line.split("   ")
    lValues.append(int(lineValues[0]))
    rDict[int(lineValues[1])] += 1

similarityScores = map(lambda x: x * rDict[x], lValues)
print(sum(list(similarityScores)))






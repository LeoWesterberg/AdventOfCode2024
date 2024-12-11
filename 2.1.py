import fileinput
filename = 'inputs/2.txt'

def checkValidReport(row):
    isIncreasing = row[1] > row[0]
    validReport = True
    for idx in range(1, len(row)):
        if row[idx] == row[idx - 1] or abs(row[idx] - row[idx - 1]) > 3:
            validReport = False
        if isIncreasing and row[idx] < row[idx - 1]:
            validReport = False
        if not isIncreasing and row[idx] > row[idx - 1]:
            validReport = False
    print(str(validReport) + " " + str(row))
    return validReport

count = 0
for line in fileinput.input(files=filename):
    vals = [int(num) for num in line.split(" ")]
    count += int(checkValidReport(vals))

print(count)


        
        


        


import fileinput

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
for line in fileinput.input(files='inputs/2.txt'):
    vals = [int(num) for num in line.split(" ")]
    isValidReport = checkValidReport(vals)
    if isValidReport:
        count += int(isValidReport)
        continue
    else:
        for i in range(len(vals)):
            subRow = vals[:i] + vals[i+1:]
            isValidReport = checkValidReport(subRow)
            if isValidReport:
                count += int(isValidReport)
                break
print(count)


        
        


        


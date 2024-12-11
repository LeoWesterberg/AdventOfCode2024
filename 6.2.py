def findStart(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == '^':
                return (y, x)

def getNextDir(currDir):
    if currDir == (-1, 0):
        return (0, 1)
    elif currDir == (1, 0):
        return (0, -1)
    elif currDir == (0, -1):
        return (-1, 0)
    elif currDir == (0, 1):
        return (1, 0)

def isOutOfBounds(matrix, pos):
    if pos[0] >= len(matrix) or pos[0] < 0:
        return True
    if pos[1] >= len(matrix[0]) or pos[1] < 0:
        return True
    return False

def isLoop(matrix, curr, dir, visited):
    while(True):
        if isOutOfBounds(matrix, curr):
            return False
        if (curr[0], curr[1], dir) in visited:
            return True
        visited.add((curr[0], curr[1], dir))
        nextPos = tuple(a + b for a, b in zip(curr, dir))
        if isOutOfBounds(matrix, nextPos):
            return False
        while(matrix[nextPos[0]][nextPos[1]] == "#"): 
            dir = getNextDir(dir)
            nextPos = tuple(a + b for a, b in zip(curr, dir))
            if isOutOfBounds(matrix, nextPos):
                return False
        else:
            curr = nextPos
            
totalLoops = 0
with open("inputs/6.txt", 'r') as file:
    lines = file.readlines()
    matrix = [list(line.strip()) for line in lines]

    dir = (-1, 0)
    curr = findStart(matrix)
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            visited = set()
            if matrix[y][x] == '.':
                matrix[y][x] = '#'
                totalLoops += int(isLoop(matrix, curr, dir, visited))
                matrix[y][x] = '.'

print(totalLoops)

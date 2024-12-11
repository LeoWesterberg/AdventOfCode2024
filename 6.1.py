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
    elif pos[1] >= len(matrix[0]) or pos[1] < 0:
        True
    return False

with open("inputs/6.txt", 'r') as file:
    lines = file.readlines()
    matrix = [list(line.strip()) for line in lines]

    dir = (-1, 0)
    curr = findStart(matrix)
    visited = set()
    steps = 0
    while(True):
        if isOutOfBounds(matrix, curr):
            break
        if curr not in visited:
            steps += 1
            visited.add(curr)
        nextPos = tuple(a + b for a, b in zip(curr, dir))
        if isOutOfBounds(matrix, nextPos):
            break
        while(matrix[nextPos[0]][nextPos[1]] == "#"): 
            dir = getNextDir(dir)
            nextPos = tuple(a + b for a, b in zip(curr, dir))
        else:
            curr = nextPos
    print(steps)
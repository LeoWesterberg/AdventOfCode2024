import fileinput

filename = "inputs/4.txt"
char_matrix = [list(filter(lambda x: x != '\n', list(line))) for line in fileinput.input(files=filename)]

def check_diagonal(char_matrix, row, col):
    res = [[], [], [], []]
    count = 0
    for diff in range(0,4):
        if row + diff < len(char_matrix) and col + diff < len(char_matrix[row + diff]):
            res[0].append(char_matrix[row + diff][col + diff])
        if row + diff < len(char_matrix) and col - diff >= 0:
            res[1].append(char_matrix[row + diff][col - diff])
        if row - diff >= 0 and col + diff < len(char_matrix[row]):
            res[2].append(char_matrix[row - diff][col + diff])
        if row - diff >= 0 and col - diff >= 0:
            res[3].append(char_matrix[row - diff][col - diff])    
    count += sum([int(''.join(dirChars) == 'XMAS') for dirChars in res])
    return count

def check_horizontal(char_matrix, row, col):
    res = [[], []]
    count = 0
    for diff in range(0,4):
        if row + diff < len(char_matrix):
            res[0].append(char_matrix[row + diff][col])
        if row - diff >= 0:
            res[1].append(char_matrix[row - diff][col])
    count += sum([int(''.join(dirChars) == 'XMAS') for dirChars in res])
    return count
     
def check_vertical(char_matrix, row, col):
    res = [[], []]
    count = 0
    for diff in range(0,4):
        if col + diff < len(char_matrix[row]):
            res[0].append(char_matrix[row][col + diff])
        if col - diff >= 0:
            res[1].append(char_matrix[row][col - diff])
    count += sum([int(''.join(dirChars) == 'XMAS') for dirChars in res])
    return count

count = 0
for row in range(len(char_matrix)):
    for col in range(len(char_matrix[row])):
        count += check_diagonal(char_matrix, row, col)
        count += check_horizontal(char_matrix, row, col)
        count += check_vertical(char_matrix, row, col)
print(count)

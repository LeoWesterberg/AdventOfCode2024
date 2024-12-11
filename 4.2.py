import fileinput

filename = "inputs/4.txt"
char_matrix = [list(filter(lambda x: x != '\n', list(line))) for line in fileinput.input(files=filename)]

def check_diagonal(char_matrix, row, col):
    if char_matrix[row][col] == 'A':
        if row > 0 and col > 0 and row < len(char_matrix) - 1 and col < len(char_matrix[row]) - 1:
            leftUp = char_matrix[row - 1][col - 1] 
            rightDown =  char_matrix[row + 1][col + 1] 
            leftDown = char_matrix[row + 1][col - 1] 
            rightUp = char_matrix[row - 1][col + 1] 

            if (leftUp == 'M' and rightDown == "S") or (leftUp == 'S' and rightDown == "M"):
                if (leftDown == 'M' and rightUp == "S") or (leftDown == 'S' and rightUp == "M"):
                    return True
    return False

count = 0
for row in range(len(char_matrix)):
    for col in range(len(char_matrix[row])):
        count += int(check_diagonal(char_matrix, row, col))
print(count)

    

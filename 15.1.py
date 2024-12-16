UP, DOWN, LEFT, RIGHT = '^', 'v', '<', '>'
WALL, ROCK, EMPTY, POS = "#", "O", ".", "@"
filename = "inputs/15.txt"

grid = []
moves = []
with open(filename) as file:
    for line in file:
        if line.startswith("#"):
            grid.append([char for char in line if char != '\n'])
        else:
            moves.extend(line)
moves = list(filter(lambda char: char != '\n', moves))

def get_moved_coord(x, y, move):   
    if move == UP:
        return (x, y - 1)
    if move == DOWN:
        return (x, y + 1)
    if move == LEFT:
        return (x - 1, y)
    if move == RIGHT:
        return (x + 1, y)

def move_rocks(grid, x, y, dir):
    x_curr, y_curr = x, y
    while(grid[y_curr][x_curr] == ROCK):
        x_curr, y_curr = get_moved_coord(x_curr, y_curr, dir)
    if grid[y_curr][x_curr] == EMPTY:
        grid[y_curr][x_curr] = ROCK
        grid[y][x] = EMPTY

def get_pos(grid):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == POS:
                return (x, y)
    return None 

def move_pos(grid, x, y, move):
    x_new, y_new = get_moved_coord(x, y, move)
    next_pos_val = grid[y_new][x_new]
    if next_pos_val == WALL:
        return
    elif next_pos_val == EMPTY:
        grid[y][x] = EMPTY
        grid[y_new][x_new] = POS
        return x_new, y_new
    elif next_pos_val == ROCK:
        move_rocks(grid, x_new, y_new, move)
        if grid[y_new][x_new] == EMPTY:
            grid[y][x] = EMPTY
            grid[y_new][x_new] = POS
            return x_new, y_new
    return x, y


def visualize_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end=" ")
        print()
        

x, y = get_pos(grid)
for idx, move in enumerate(moves):
    res = move_pos(grid, x, y, move)
    if res:
        x, y = res

total = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == ROCK:
            total += y * 100 + x
visualize_grid(grid)
print(total)
    


            





UP, DOWN, LEFT, RIGHT = '^', 'v', '<', '>'
WALL, BOX_LEFT, BOX_RIGHT, EMPTY, POS = "#", "[", "]", ".", "@"
filename = "inputs/15.txt"

grid = []
moves = []
with open(filename) as file:
    for line in file:
        if line.startswith("#"):
            line_chars = []
            for char in line:
                if char == "\n":
                    continue
                if char == "O": 
                    line_chars.extend(["[", "]"])
                elif char == POS:
                    line_chars.extend([POS, "."])
                else:
                    line_chars.extend([char, char])
            grid.append(line_chars)
        else:
            moves.extend(line)

moves = list(filter(lambda char: char != '\n', moves))

def get_moved_coord(x, y, dir, steps=1):   
    if dir == UP:
        return (x, y - steps)
    if dir == DOWN:
        return (x, y + steps)
    if dir == LEFT:
        return (x - steps, y)
    if dir == RIGHT:
        return (x + steps, y)


def can_move_box(grid, x_left, y_left, x_right, y_right, dir):
    if dir == LEFT:
        new_x, new_y = get_moved_coord(x_left, y_left, dir)
        return grid[new_y][new_x] == EMPTY
    elif dir == RIGHT:
        new_x, new_y = get_moved_coord(x_right, y_right, dir)
        return grid[new_y][new_x] == EMPTY
    else:
        new_left_x, new_left_y = get_moved_coord(x_left, y_left, dir)
        new_right_x, new_right_y = get_moved_coord(x_right, y_right, dir)
        return grid[new_right_y][new_right_x] == EMPTY and grid[new_left_y][new_left_x] == EMPTY

def get_box_neighs(grid, x_left, y_left, x_right, y_right, dir):
    res_boxes = []
    if dir == UP or dir == DOWN:
        dy = 1 if dir == DOWN else -1
        box_combinations = [(x_left - 1, y_left + dy, x_left, y_left + dy), 
                            (x_left, y_left + dy, x_right, y_right + dy),
                            (x_right, y_left + dy, x_right + 1, y_left + dy)]
        
        for xl, yl, xr, yr in box_combinations:
            if grid[yl][xl] == BOX_LEFT and grid[yr][xr] == BOX_RIGHT:
                res_boxes.append((xl, yl, xr, yr))
    else:
        x_left_new, y_left_new = get_moved_coord(x_left, y_left, dir, steps=2)
        x_right_new, y_right_new = get_moved_coord(x_right, y_right, dir, steps=2)
        if grid[y_left_new][x_left_new] == BOX_LEFT and grid[y_right_new][x_right_new] == BOX_RIGHT:
            res_boxes.append((x_left_new, y_left_new, x_right_new, y_right_new))
            
    return res_boxes


def can_move_boxes(grid, x_left, y_left, x_right, y_right, dir):
    if can_move_box(grid, x_left, y_left, x_right, y_right, dir):
        return True, [(x_left, y_left, x_right, y_right)]

    x_left_new, y_left_new = get_moved_coord(x_left, y_left, dir)
    x_right_new, y_right_new = get_moved_coord(x_right, y_right, dir)
    new_left_val = grid[y_left_new][x_left_new]
    new_right_val = grid[y_right_new][x_right_new]

    if new_right_val == WALL or new_left_val == WALL:
        return False, []
    else:
        res = True
        visited_boxes = [(x_left, y_left, x_right, y_right)]
        neigh_boxes = get_box_neighs(grid, x_left, y_left, x_right, y_right, dir)
        for box in neigh_boxes:
            box_x_left, box_y_left, box_x_right, box_y_right = box
            can_move, boxes = can_move_boxes(grid, box_x_left, box_y_left, box_x_right, box_y_right, dir)
            visited_boxes.extend(boxes)
            res = res and can_move
        return res, visited_boxes    


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
    elif next_pos_val == BOX_LEFT or next_pos_val == BOX_RIGHT:
        is_right = next_pos_val == BOX_RIGHT
        x_left, y_left = x_new - (1 if is_right else 0), y_new
        x_right, y_right = x_new + (1 if not is_right else 0), y_new
        can_move, moved_boxes = can_move_boxes(grid, x_left, y_left, x_right, y_right, move)

        if can_move:
            for box in moved_boxes:
                xl, yl, xr, yr = box
                grid[yl][xl] = EMPTY
                grid[yr][xr] = EMPTY

            for box in moved_boxes:
                xl, yl, xr, yr = box
                xl_new, yl_new = get_moved_coord(xl, yl, move)
                xr_new, yr_new = get_moved_coord(xr, yr, move)
                grid[yl_new][xl_new] = BOX_LEFT
                grid[yr_new][xr_new] = BOX_RIGHT

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
        if grid[y][x] == BOX_LEFT:
            total += y * 100 + x
visualize_grid(grid)
print(total)

            





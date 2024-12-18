import heapq

def readinput(filename):
    grid = []
    with open(filename) as file:
        for line in file:
            if line.startswith("#"):
                line_chars = []
                for char in line:
                    if char == "\n":
                        continue
                    else:
                        line_chars.extend([char])
                grid.append(line_chars)
    return grid

def get_reverse_dir(dir):
    return (-dir[0], -dir[1])

def get_turn_dirs(dir):
    return [(0, 1), (0, -1)] if dir[0] != 0 else [(1, 0), (-1, 0)]
    
def djikstras(grid, x, y, dir):
    visited = set()
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = [] 
    cost = None
    heapq.heappush(queue, (0, (x, y), dir))
    while(grid[y][x] != "E"):
        cost, coord, dir = heapq.heappop(queue)
        if (coord, dir) not in visited:
            x, y = coord
            visited.add((coord, dir))
            for new_dir in dirs:
                dir_cost = 1001 if new_dir in get_turn_dirs(dir) else 1
                dir_pos_x, dir_pos_y = x + new_dir[0], y + new_dir[1]
                if grid[dir_pos_y][dir_pos_x] != "#" and new_dir != get_reverse_dir(dir):
                    heapq.heappush(queue, (cost + dir_cost, (dir_pos_x, dir_pos_y), new_dir))
    return cost
            
grid = readinput("inputs/16.txt")
x, y = 1, len(grid) - 2
cost = djikstras(grid, x, y, (1, 0))
print(cost)
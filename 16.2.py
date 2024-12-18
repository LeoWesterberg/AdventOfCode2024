import heapq
import sys

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
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = [] 
    min_cost = sys.maxsize
    best_path_visited = set()
    global_visited = {}
    heapq.heappush(queue, (0, (x, y), dir, set()))
    while(len(queue) > 0):
        cost, coord, dir, path_visited = heapq.heappop(queue)
        if grid[coord[1]][coord[0]] == "E":
            if cost <= min_cost:
                best_path_visited.update(set(map(lambda x: x[0], path_visited)))
                min_cost = cost
            else:
                break
        if (coord, dir) not in path_visited:
            if (coord, dir) not in global_visited:
                global_visited[(coord, dir)] = cost
            elif  cost > global_visited[(coord, dir)]:
                continue
            x, y = coord
            path_visited.add((coord, dir))
            for new_dir in dirs:
                dir_cost = 1001 if new_dir in get_turn_dirs(dir) else 1
                dir_pos_x, dir_pos_y = x + new_dir[0], y + new_dir[1]
                dir_value = grid[dir_pos_y][dir_pos_x]
                if dir_value != "#" and new_dir != get_reverse_dir(dir):
                    heapq.heappush(queue, (cost + dir_cost, (dir_pos_x, dir_pos_y), new_dir, set().union(path_visited)))
    return min_cost, best_path_visited
            
grid = readinput("inputs/16.txt")
x, y = 1, len(grid) - 2
cost, best_path_visited = djikstras(grid, x, y, (1, 0))
print(len(best_path_visited) + 1)
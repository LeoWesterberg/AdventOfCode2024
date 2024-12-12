import fileinput
from collections import defaultdict

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def inside_grid(grid, x, y):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])

def calculate_corders(grid, x, y):
    value = grid[y][x]
    outfacing_sides = set()
    corners = 0

    for diff in directions:
        dx, dy = (x + diff[0], y + diff[1])
        if inside_grid(grid, dx, dy) and grid[dy][dx] == value:
            continue
        outfacing_sides.add(diff)

    corner_dir_pairs = [
        [(-1, 0), (0, -1)], [(-1, 0), (0, 1)],
        [(1, 0), (0, -1)], [(1, 0), (0, 1)]
    ]        

    for dir_pair in corner_dir_pairs:
        if dir_pair[0] in outfacing_sides and dir_pair[1] in outfacing_sides:
            corners += 1
            
        dir1_x, dir1_y = dir_pair[0][0] + x, dir_pair[0][1] + y
        dir2_x, dir2_y = dir_pair[1][0] + x, dir_pair[1][1] + y

        if inside_grid(grid, dir1_x ,dir1_y) and inside_grid(grid,dir2_x, dir2_y):
            if grid[dir1_y][dir1_x] == value and grid[dir2_y][dir2_x] == value:
                top = (dir1_x + dir_pair[1][0], dir1_y + dir_pair[1][1])
                if inside_grid(grid, top[0], top[1]) and grid[top[1]][top[0]] != value:
                    corners += 1

    return corners

def traverse_region(grid, x, y, visited):
    value = grid[y][x]
    if not inside_grid(grid, x, y) or (x, y) in visited:
        return (0, 0)

    visited.add((x, y))
    sides, area = 0, 0
    for diff in directions:
        dx, dy = (x + diff[0], y + diff[1])
        if inside_grid(grid, dy, dx):
            if grid[dy][dx] == value:
                res = traverse_region(grid, dx, dy, visited)
                area += res[0]
                sides += res[1]
    return (area + 1, sides + calculate_corders(grid, x, y))


filename = "inputs/12.txt"
char_matrix = [list(filter(lambda x: x != '\n', list(line))) for line in fileinput.input(files=filename)]

plot_res = defaultdict(list)   
visited = set()
res = []
for y in range(len(char_matrix)):
    for x in range(len(char_matrix[y])):
        region_vals = traverse_region(char_matrix, x, y, visited)
        if region_vals != (0, 0):
            res.append((region_vals))

print(sum([a * p for a, p in res]))

        



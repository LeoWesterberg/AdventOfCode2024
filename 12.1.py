import fileinput
from collections import defaultdict

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def inside_grid(grid, x, y):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])

def perimiter_contrib(grid, x, y):
    value = grid[y][x]
    perimiter = 0
    for diff in directions:
        dx, dy = (x + diff[0], y + diff[1])
        if inside_grid(grid, dx, dy):
            if grid[dy][dx] == value:
                continue
        perimiter += 1
    return perimiter

def traverse_region(grid, x, y, visited):
    value = grid[y][x]
    if not inside_grid(grid, x, y) or (x, y) in visited:
        return (0, 0)

    visited.add((x, y))
    perimiter, area = 0, 0
    for diff in directions:
        dx, dy = (x + diff[0], y + diff[1])
        if inside_grid(grid, dy, dx):
            if grid[dy][dx] == value:
                res = traverse_region(grid, dx, dy, visited)
                area += res[0]
                perimiter += res[1]
    return (area + 1, perimiter + perimiter_contrib(grid, x, y))       

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

        



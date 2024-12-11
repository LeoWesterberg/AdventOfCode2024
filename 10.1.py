import fileinput
grid = [[int(height) for height in line if height != '\n'] for line in fileinput.input(files='inputs/10.txt')]

def find_trail_heads(grid):
    heads = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                heads.append((y,x))
    return heads

def inside_grid(grid, pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(grid) and pos[1] < len(grid)

def search_path(pos, grid, visited:set):
    visited.add(pos)
    if grid[pos[0]][pos[1]] == 9:
        return 1
    total = 0
    current_height = grid[pos[0]][pos[1]]
    for dir in [(1,0), (0,1), (-1,0), (0,-1)]:
        dir_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if inside_grid(grid, dir_pos) and grid[dir_pos[0]][dir_pos[1]] - current_height == 1 and dir_pos not in visited:
            total += search_path(dir_pos, grid, visited)
    return total

total = 0
trail_heads = find_trail_heads(grid)
for head in trail_heads:
    res = search_path(head, grid, set())
    total += res

print(total)



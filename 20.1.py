import heapq

def readinput(filename):
    grid = []
    with open(filename) as file:
        for line in file:
            grid.extend([list(row) for row in line.split()])
    return grid

def djikstras(grid, x, y):
    visited = set()
    queue = [] 
    cost = None
    heapq.heappush(queue, (0, (x, y)))
    while(len(queue) > 0):
        cost, coord = heapq.heappop(queue)
        if grid[coord[1]][coord[0]] == "E":
            return cost
        if coord not in visited:
            x, y = coord
            visited.add(coord)
            for new_dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dir_pos_x, dir_pos_y = x + new_dir[0], y + new_dir[1]
                if 0 <= dir_pos_y < len(grid) and 0 <= dir_pos_x < len(grid[0]) and grid[dir_pos_y][dir_pos_x] != "#":
                    heapq.heappush(queue, (cost + 1, (dir_pos_x, dir_pos_y)))
    return cost

def find_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                return (x, y)
    
grid = readinput("inputs/20.txt")
walls = set([(x, y) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell == "#"])
start_x, start_y = find_start(grid)
best_score = djikstras(grid, start_x, start_y)
count = 0
for idx, (w1_x, w1_y) in enumerate(walls):
    grid[w1_y][w1_x] = "."
    if djikstras(grid, start_x, start_y) <= best_score - 100:
        count += 1
    grid[w1_y][w1_x] = "#"
print(count)



            
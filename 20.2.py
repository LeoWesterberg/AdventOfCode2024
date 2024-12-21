import heapq

def readinput(filename):
    grid = []
    with open(filename) as file:
        for line in file:
            grid.extend([list(row) for row in line.split()])
    return grid

def djikstras(grid, x, y, cost_matrix):
    visited = set()
    queue = [] 
    heapq.heappush(queue, (0, (x, y)))
    while(len(queue) > 0):
        cost, coord = heapq.heappop(queue)
        if coord not in visited:
            x, y = coord
            cost_matrix[y][x] = cost
            visited.add(coord)
            for new_dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dir_pos_x, dir_pos_y = x + new_dir[0], y + new_dir[1]
                if 0 <= dir_pos_y < len(grid) and 0 <= dir_pos_x < len(grid[0]) and grid[dir_pos_y][dir_pos_x] != "#":
                    heapq.heappush(queue, (cost + 1, (dir_pos_x, dir_pos_y)))
    return cost_matrix

def find_start(grid, letter):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == letter:
                return (x, y)

def calculate_manhattan(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def get_cost_matrix(grid, start):
    start_x, start_y = find_start(grid, start)
    start_cost_matrix = [[0] * len(grid[0]) for _ in range(len(grid))]
    return djikstras(grid, start_x, start_y, start_cost_matrix)

grid = readinput("inputs/20.txt")
start_cost_matrix = get_cost_matrix(grid, "S")
end_cost_matrix = get_cost_matrix(grid, "E")

end_x, end_y = find_start(grid, "E")
best_cost = start_cost_matrix[end_y][end_x]

count = 0
path_coords  = [(x, y) for y, row in enumerate(grid) for x, cell in enumerate(row) if cell != "#"]
for idx, coord1 in enumerate(path_coords):
    for coord2 in path_coords:
        cheat_jump = calculate_manhattan(coord1, coord2)
        x1, y1 = coord1
        x2, y2 = coord2
        if cheat_jump <= 20:
            if start_cost_matrix[y1][x1] + end_cost_matrix[y2][x2] + cheat_jump <= best_cost - 100:
                count += 1
print(count)



            
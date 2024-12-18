import heapq

def readinput(filename):
    count = 0
    mem = [["."] * 71 for i in range(71)]
    with open(filename) as file:
        for line in file:
            if count < 1024:
                x, y = tuple(line.split(","))
                mem[int(y)][int(x)] = "#"
                count += 1
    return mem

def djikstras(grid, x, y, target):
    visited = set()
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = [] 
    cost = None
    heapq.heappush(queue, (0, (x, y)))
    while(len(queue) > 0):
        cost, coord = heapq.heappop(queue)
        if coord == target:
            return cost
        if coord not in visited:
            x, y = coord
            visited.add(coord)
            for new_dir in dirs:
                dir_pos_x, dir_pos_y = x + new_dir[0], y + new_dir[1]
                if 0 <= dir_pos_y < len(grid) and 0 <= dir_pos_x < len(grid[0]):
                    if grid[dir_pos_y][dir_pos_x] != "#":
                        heapq.heappush(queue, (cost + 1, (dir_pos_x, dir_pos_y)))
    return cost

grid = readinput("inputs/18.txt")
cost = djikstras(grid, 0, 0, (70, 70))
print(cost)
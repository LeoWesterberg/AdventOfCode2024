import re
from math import prod
import time

def get_quadrant(max_x, max_y, px, py):
    if 0 <= px < max_x // 2 and 0 <= py < max_y // 2:
        return 0
    if 0 <= px < max_x // 2 and max_y // 2 < py < max_y:
        return 1
    if max_x // 2 < px < max_x and 0 <= py < max_y // 2:
        return 2
    if max_x // 2 < px < max_x and max_y // 2 < py < max_y:
        return 3
    else:
        return None

def visualize(grid, filename):
    with open(filename, 'a') as file:

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 0:
                    file.write(" ")
                else:
                    file.write("*")
            file.write("\n")

robots = []
with open("inputs/14.txt") as file:
    for line in file:
        robots.append(tuple(int(num) for num in re.findall(r'-?\d+', line)))

MAX_Y, MAX_X = 103, 101

grid = [[0] * MAX_X for _ in range(MAX_Y)]
for sec in range(1, 10000):
    filename = "output" + str((sec // 1000) % 10) + ".txt"
    with open(filename, 'a') as file:

       file.write(str(sec))
    for idx, robot in enumerate(robots):
        px, py, vx, vy = robot
        px_new = (px + vx) % MAX_X
        py_new = (py + vy) % MAX_Y
        if time != 0 and grid[py][px] != 0:
            grid[py][px] -= 1

        grid[py_new][px_new] += 1
        robots[idx] = (px_new, py_new, vx, vy)
    visualize(grid, filename)
    
    
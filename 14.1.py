import re
from math import prod

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


robots = []
with open("inputs/14.txt") as file:
    for line in file:
        robots.append(tuple(int(num) for num in re.findall(r'-?\d+', line)))

MAX_Y,MAX_X = 103, 101

quadrant_count = [0, 0, 0, 0]

for robot in robots:
    px, py, vx, vy = robot
    px_100 = (px + vx * 100) % MAX_X
    py_100 = (py + vy * 100) % MAX_Y
    
    quadrant = get_quadrant(MAX_X, MAX_Y, px_100, py_100)
    if quadrant != None:
        quadrant_count[quadrant] += 1

print(prod(quadrant_count))
    
    
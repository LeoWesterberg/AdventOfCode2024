import fileinput
from functools import lru_cache
from itertools import permutations
import sys

LEFT, RIGHT, UP, DOWN, ENTER = "<", ">", "^", "v", "A"
dir_map = {
           RIGHT:   (1, 0), 
           DOWN:    (0, -1),
           LEFT:    (-1, 0), 
           UP:      (0, 1), 
           }

def get_key_pos(symbol, num_layout):
    if num_layout:
        if symbol == ENTER:
            return (2, 0)
        symbol = int(symbol)
        if symbol == 0:
            return (1, 0)
        return ((symbol - 1) % 3, (symbol - 1) // 3 + 1)
    else:
        if symbol == LEFT:
            return (0, 0)
        elif symbol == RIGHT:
            return (2, 0)
        elif symbol == UP:
            return (1, 1)
        elif symbol == DOWN:
            return (1, 0)
        elif symbol == ENTER:
            return (2, 1)

def get_moves(from_pos, to_pos, is_num_layout):
    dx, dy = (to_pos[0] - from_pos[0], to_pos[1] - from_pos[1])
    res = []
    if dy > 0: res.append(UP * abs(dy))
    if dx > 0: res.append(RIGHT * dx)
    if dx < 0: res.append(LEFT * abs(dx))
    if dy < 0: res.append(DOWN * abs(dy)) 
    moves = set(permutations("".join(res)))
    return filter(lambda moves: valid_moves(from_pos, moves, is_num_layout), moves)

def valid_moves(from_pos, moves, is_num_layout):
    for move in moves:
        move_diff = dir_map[move]
        from_pos = (from_pos[0] + move_diff[0], from_pos[1] + move_diff[1])
        if (is_num_layout and from_pos == (0, 0)) or (not is_num_layout and from_pos == (0, 1)):
            return False
    return True
    
@lru_cache(maxsize=None)
def solve(target_key, from_key, depth):
    if depth == 3:
        return 1
    
    is_num_layout = depth == 0
    from_pos = get_key_pos(from_key, is_num_layout)
    to_pos = get_key_pos(target_key, is_num_layout)
    move_combinations = get_moves(from_pos, to_pos, is_num_layout)

    nbr_moves = sys.maxsize
    for moves in move_combinations:
        move_score = 0
        for idx, move in enumerate( [*moves, "A"]):
            move_score += solve(move, "A" if idx == 0 else moves[idx - 1], depth + 1)
        nbr_moves = min(nbr_moves, move_score)
    return nbr_moves


codes = [line.strip() for line in fileinput.input(files="inputs/21.txt") if line != "\n"]
sum = 0
for code in codes:
    res = 0
    from_key = "A"
    for char in code:
        res += solve(char, from_key, 0)
        from_key = char
    sum += int(code[:-1]) * res
print(sum)
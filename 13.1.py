import sys
from functools import cache
import re
cases = []
with open("inputs/13.txt") as file:
    for line in file:
        formatted_nums = [int(num) for num in re.findall(r'\d+', line)]
        if formatted_nums:
            nums_tuple = (formatted_nums[0], formatted_nums[1])
            if "Button A" in line:
                cases.append([nums_tuple])
            else:
                cases[-1].append(nums_tuple)
 
@cache
def traverse(total, current, tokens, moves):
    if current == total:
        return tokens

    if current[0] > total[0] or current[1] > total[1]:
        return sys.maxsize
    
    min_cost = sys.maxsize
    for idx, move in enumerate(moves):
        cost = 3 if idx == 0 else 1
        new_current = (current[0] + move[0], current[1] + move[1])
        min_cost = min(traverse(total, new_current, tokens + cost, moves), min_cost)
    return min_cost
 
 
total_sum = 0
for idx, case in enumerate(cases):
    total = case[2]
    min_traverse = traverse(case[2], (0, 0), 0, tuple(case[:2]))
    if min_traverse != sys.maxsize:
        total_sum += min_traverse
print(total_sum)   
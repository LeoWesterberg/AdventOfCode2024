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
 
total_sum = 0
for idx, case in enumerate(cases):
    total = case[2]
    ax, ay = case[0]
    bx, by = case[1]
    tot_x, tot_y = case[2][0] + 10000000000000, case[2][1] + 10000000000000
    
    #Linear system: ax * steps_a + bx + steps_b = tot_x
    #               ay * steps_a + by * steps_b = tot_y
    if (ax * by - ay * bx) != 0:
        a_steps = (tot_x * by - tot_y * bx) / (ax * by - ay * bx)
        b_steps = (tot_x - ax * a_steps) / bx

        if a_steps.is_integer() and b_steps.is_integer():
            total_sum += int(a_steps) * 3 + int(b_steps)
    
print(total_sum)   

from collections import defaultdict

def occurrences(s, lst):
    return (i for i,e in enumerate(lst) if e == s)

def group_consecutive(lst):
    if not lst:
        return []
    result = []
    temp = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1] + 1:
            temp.append(lst[i])
        else:
            result.append(temp)
            temp = [lst[i]]
    result.append(temp)
    return result

def moveSeq(lst, nums_map):
    for num in reversed(nums_map):
        if num != ".":
            dot_indexes_group = group_consecutive(list(occurrences('.', lst)))
            for group in dot_indexes_group:
                if len(group) >= len(nums_map[num]) and group[0] < nums_map[num][0]:
                    group = list(reversed(group[:len(nums_map[num])]))
                    for i in range(len(nums_map[num])):
                        lst[nums_map[num][i]] = '.'
                        lst[group[i]] = num
                    break    
    return lst

with open("inputs/9.txt", 'r') as file:
    line = file.readline()
    filled_list = []
    space = False
    current_number = 0
    for idx, num in enumerate(line):
        fill_number = '.' if space else current_number
        
        for i in range(int(num)):
            filled_list.append(str(fill_number))
        current_number = current_number if space else current_number + 1
        space = not space

    nums_map = defaultdict(list)
    for idx, num in enumerate(filled_list):
        if num != ".":
            nums_map[num].append(idx)

    filled_list = moveSeq(filled_list, nums_map)

sum = 0
for idx, num in enumerate(filled_list):
    if  num != '.':
        sum += int(num) * idx

print(sum)

        
        





        


    
  

with open("inputs/9.txt", 'r') as file:
    line = file.readline()
    filled_list = []
    space = False
    current_number = 0
    dot_indexes = []
    for idx, num in enumerate(line):
        fill_number = '.' if space else current_number
        
        for i in range(int(num)):
            filled_list.append(str(fill_number))
        current_number = current_number if space else current_number + 1
        space = not space

    for i in range(len(filled_list)):
        if filled_list[i] == ".":
            dot_indexes.append(i)
    for idx in range(len(filled_list) - 1, -1, -1):
        if (filled_list[idx] != "." and len(dot_indexes) > 0):
            dot_index = dot_indexes[0]
            dot_indexes = dot_indexes[1:]
            if dot_index > idx:
                continue
            filled_list[dot_index] = filled_list[idx]
            filled_list[idx] = '.'

sum = 0
for idx, num in enumerate(filled_list):
    if num != ".":
        sum += int(num) * idx

print(sum)







        
        





        


    
  
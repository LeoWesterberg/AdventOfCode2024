import re

with open('inputs/3.txt', 'r') as file:
    content = file.read()
    do_pattern = r"do\(\)|don\'t\(\)"
    all_pattern = r"mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)"

    do_matches = [val == "do()" for val in re.findall(do_pattern, content)]
    all_matches =  re.findall(all_pattern, content)

    do_idx = 0
    status = True
    sum = 0
    print(all_matches)
    for match in all_matches:
        if match == ('',''):
            status = do_matches[do_idx]
            do_idx += 1
        elif status:
            sum += int(match[0]) * int(match[1])
    print(sum)





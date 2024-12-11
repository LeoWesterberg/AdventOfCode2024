import re

with open('inputs/3.txt', 'r') as file:
    content = file.read()
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, content)
    answer = sum([int(num1) * int(num2) for (num1, num2) in matches])
    print(answer)



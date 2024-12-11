import fileinput
input = fileinput.input(files='inputs/11.txt').readline()
nums = [int(num) for num in input.split(" ")]

def modify_entry(num):
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 1:
        return [num * 2024]
    else:
        num_str = str(num)
        num1 = num_str[:len(num_str) // 2]
        num2 = num_str[len(num_str) // 2:]
        return [int(num1), int(num2.lstrip('0') or "0")]

for i in range(25):
    new = []
    for j in range(len(nums)):
        for next_num in modify_entry(nums[j]):
            new.append(next_num)
    nums = new

print(len(nums))
    
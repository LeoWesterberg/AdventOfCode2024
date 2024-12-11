import fileinput

input_data = fileinput.input(files='inputs/11.txt').readline()
nums = [int(num) for num in input_data.split()]

memo = {}

def modify_entry(num, n):
    if (num, n) in memo:
        return memo[(num, n)]

    if n == 0:
        return 1
    if num == 0:
        return modify_entry(1, n - 1)

    num_str = str(num)
    len_num = len(num_str)
    
    if len_num % 2 == 1:
        result = modify_entry(num * 2024, n - 1)
    else:
        div_len = len_num // 2
        num1 = int(num_str[:div_len])
        num2 = int(num_str[div_len:].lstrip('0') or "0")
        result = modify_entry(num1, n - 1) + modify_entry(num2, n - 1)
    
    memo[(num, n)] = result
    return result

total = 0
for num in nums:
    total += modify_entry(num, n=75)

print(total)

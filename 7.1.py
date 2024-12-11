def calculate(nums, idx):
    if idx == 0:
        return [nums[0]]
    else:
        calculations = calculate(eq_nums, idx - 1)
        calcIncludingThis = []
        for calc in calculations:
            mulRes = nums[idx] * calc
            addRes = nums[idx] + calc
            calcIncludingThis.append(mulRes)
            calcIncludingThis.append(addRes)
        return list(calcIncludingThis)

with open("inputs/7.txt", 'r') as file:
    lines = file.readlines()
    total = 0
    for eq in lines:
        numbers = [int(num.replace(":", "")) for num in eq.split(" ")]
        ans = numbers[0]
        eq_nums = numbers[1:]
        res = calculate(eq_nums, len(eq_nums) - 1)
        if sum([int(num == ans) for num in res]) > 0:
            total += ans
print(total)
        

        

        

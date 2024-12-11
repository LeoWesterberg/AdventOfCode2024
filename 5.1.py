from collections import defaultdict
with open('inputs/5.txt', 'r') as file:
    content = file.read()
    rows = content.split("\n")

lessThan = defaultdict(set)
largerThan = defaultdict(set)
sum = 0
for row in rows:
    if row == "":
        continue
    if "|" in row:
        nums = [int(num) for num in row.split("|")]
        lessThan[nums[1]].add(nums[0])
        largerThan[nums[0]].add(nums[1])
    else:
        nums = [int(num) for num in row.split(",")]
        hasSeen = set()
        badEntry = False
        for num in nums:
            for numHasSeen in list(hasSeen):
                if num in lessThan[numHasSeen]:
                    badEntry = True
            hasSeen.add(num)

        if badEntry:
            continue
        else:
            sum += nums[len(nums) // 2]
print(sum)


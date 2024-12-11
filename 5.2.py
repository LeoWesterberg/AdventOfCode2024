from collections import defaultdict

with open('inputs/5.txt', 'r') as file:
    content = file.read()
    rows = content.split("\n")

lessThan = defaultdict(set)
sum = 0
for row in rows:
    if row == "":
        continue
    if "|" in row:
        nums = [int(num) for num in row.split("|")]
        lessThan[nums[1]].add(nums[0])
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
            for idx in range(len(nums)):
                for idx2 in range(idx - 1, -1, -1):
                    numFront = nums[idx]
                    numBack = nums[idx2]
                    if numFront in lessThan[numBack]:
                        nums[idx2] = numFront
                        nums[idx] = numBack
                        idx -= 1
            sum += nums[len(nums) // 2]     
print(sum)


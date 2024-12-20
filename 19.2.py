import fileinput
input_rows = [line.strip() for line in fileinput.input(files="inputs/19.txt") if line != "\n"]
combos = input_rows[0].split(", ")
cases = input_rows[1:]

def parse_line(line:str, combos:list[str], total, memo):
    if len(line) - 1 in memo:
        return memo[len(line) - 1]
    if line == "":
        return 1
    start_tot = total
    for combo in combos:
        if line.startswith(combo):
            total += parse_line(line[len(combo):], combos, start_tot, memo)
    memo[len(line) - 1] = total
    return total

count = 0
for idx, case in enumerate(cases):
    count += int(parse_line(case, combos, 0, {}))
print(count)


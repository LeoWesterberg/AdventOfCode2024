import fileinput
input_rows = [line.strip() for line in fileinput.input(files="inputs/19.txt") if line != "\n"]
combos = input_rows[0].split(", ")
cases = input_rows[1:]

def parse_line(line:str, combos:list[str]):
    if line == "":
        return True
    res = False
    for combo in combos:
        if line.startswith(combo):
            print(combo, line, line[len(combo):])
            if parse_line(line[len(combo):], combos):
                return True
    return res

count = 0
tot = 0
for case in cases:
    tot += 1
    count += int(parse_line(case, combos))

print(count, tot)


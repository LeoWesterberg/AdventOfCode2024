import re
REG_A, REG_B, REG_C = 4, 5, 6
INS_ADV, INS_BXL, INS_BST, INS_JNZ, INS_BXC, INS_OUT, INS_BDV, INS_CDV = 0, 1, 2, 3, 4, 5, 6, 7

buffert = []
ip = 0
reg_a, reg_b, reg_c = 0, 0, 0

def get_operand(op):
    if op == REG_A:
        return reg_a
    elif op == REG_B:
        return reg_b
    elif op == REG_C:
        return reg_c
    else:
        return op

def adv(op):
    global reg_a
    reg_a = int(reg_a / pow(2, get_operand(op)))


def bxl(op):
    global reg_b
    reg_b = reg_b ^ op

def bst(op):
    global reg_b
    reg_b = get_operand(op) % 8

def jnz(op):
    global ip
    if reg_a != 0:
        ip = op

def bxc(op):
    global reg_b
    reg_b = reg_b ^ reg_c

def out(op):
   buffert.append(get_operand(op) % 8)
    
def bdv(op):
    global reg_b
    reg_b = int(reg_a / pow(2, get_operand(op)))

def cdv(op):
    global reg_c
    reg_c = int(reg_a / pow(2, get_operand(op)))

def get_ins(num):
    if num == INS_ADV:
        return adv
    if num == INS_BXL:
        return bxl
    if num == INS_BST:
        return bst
    if num == INS_JNZ:
        return jnz
    if num == INS_BXC:
        return bxc
    if num == INS_OUT:
        return out
    if num == INS_BDV:
        return bdv
    if num == INS_CDV:
        return cdv
    
def run_program(i_list, reg_a_val):
    global reg_b, reg_c, buffert, reg_a, ip
    reg_a, reg_b, reg_c, buffert, ip = reg_a_val, 0, 0, [], 0
    while(ip < len(i_list) - 1):
        ins = get_ins(i_list[ip])
        op = i_list[(ip + 1)]
        ip = ip + 2 if ins != INS_JNZ else ip
        ins(int(op))
    return buffert
    
with open("inputs/17.txt") as file:
    nums = []
    nums.extend(int(num) for num in re.findall(r'-?\d+', file.read()))
    i_list = nums[3:]
    target = list(i_list)

cost = 0
while(True):
    buffert = run_program(i_list, cost)
    if buffert == target:
        print(cost)
        break
    if buffert == target[-len(buffert):]:
        print(buffert)
        cost *= 8
    else:
        cost += 1

        
            

    


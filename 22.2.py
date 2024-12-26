
import math
import fileinput
from collections import defaultdict

def evolve_secret(secret):
    new_secret = mix_n_prune(secret, secret * 64)    
    new_secret = mix_n_prune(new_secret, math.floor(new_secret / 32))
    new_secret = mix_n_prune(new_secret, new_secret * 2048)
    return new_secret

def mix_n_prune(secret, value):
    return (secret ^ value) % 16777216

def get_nth_secret(secret, n):
    for n in range(n):
        secret = evolve_secret(secret)
    return secret

buyer_secrets = [int(line.strip()) for line in fileinput.input(files="inputs/22.txt") if line != "\n"]

seq_map = defaultdict(int)
for secret in buyer_secrets:
    curr_secret = secret
    prev_price = curr_secret % 10
    diff_list = []
    for n in range(2000):
        curr_secret = evolve_secret(curr_secret)
        price = curr_secret % 10
        diff_list.append((price, price - prev_price))
        prev_price = price

    visited = set()
    for idx in range(3, 2000):
        diff_seq = tuple(map(lambda d: d[1], diff_list[idx - 3: idx + 1]))
        if diff_seq not in visited:
            seq_map[diff_seq] += diff_list[idx][0]
            visited.add(diff_seq)

sorted_map = sorted(seq_map.values(), key=lambda value: value)
print(sorted_map[-1])

  




import math
import fileinput
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

sum_secrets = sum(list(map(lambda s: get_nth_secret(s, 2000), buyer_secrets)))
print(sum_secrets)
from itertools import pairwise
from collections import deque

def evolve(secret):
    secret ^= (secret * 64)
    secret %= 16777216

    secret ^= (secret // 32)
    secret %= 16777216

    secret ^= (secret * 2048)
    secret %= 16777216
    return secret


fname = 'input.txt'
with open(fname, 'r') as f:
    inits = [int(x) for x in f.read().splitlines()]

total = 0
seqs = {}

for i, secret in enumerate(inits):
    last_4_diff = deque([], maxlen=4)
    for j in range(2000):
        next = evolve(secret)
        last_4_diff.append((next%10)-(secret%10))
        if len(last_4_diff) == 4:
            seq = tuple(last_4_diff)
            if seqs.setdefault(seq, [None]*len(inits))[i] is None:
                seqs[seq][i] = next%10
        secret = next
    total+=secret

print("Part 1: ", total)
print("Part 2: ", max(map(lambda x: sum(filter(None, x)), seqs.values())))

from itertools import product


fname = 'input.txt'
with open(fname, 'r') as f:
    schematics = f.read().split('\n\n')

keys, locks = [], []
for s in schematics:
    if s[0] == '#':
        locks.append([sum([i=='#' for i in col]) for col in zip(*s.splitlines()[1:]) ])
    else:
        keys.append([sum([i=='#' for i in col]) for col in zip(*s.splitlines()[:-1]) ])

total = 0
for key, lock in product(keys, locks):
    total += all(sum(i)<6 for i in zip(key, lock))

print("Part 1: ", total)

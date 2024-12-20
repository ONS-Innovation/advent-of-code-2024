import numpy as np
from collections import Counter
from operator import eq, le

def manhatten_filter(n, exact=True):
    op = eq if exact else le
    return op(np.abs((np.mgrid[-n:n+1, -n:n+1])).sum(axis=0), n)

# Setup race rules
fname = 'input.txt'
cheats_p1 = 2
cheats_p2 = 20
pad_amount = (cheats_p2, cheats_p2) # Padding is a shamefully lazy and expensive way of dealing with index errors but oh well

# Parse input
with open(fname, 'r') as f:
    race = f.read().split()
charmap = {'#':0, '.':-1, 'S':1, 'E':2}
race = np.pad(np.array([[charmap[c] for c in line] for line in race], dtype=np.int16), pad_amount)
S = np.argwhere(race==1)[0]
E = np.argwhere(race==2)[0]
race[*E] = -1
# Map the race track
track = [tuple(S)]
pos = S
nb = [[-1,0], [1,0], [0,-1], [0,1]] # = np.argwhere(manhatten_filter(1, exact=True))-1
t = 1
while not (pos==E).all():
    pos += nb[np.flatnonzero(race[tuple((pos + nb).T)]==-1)[0]]
    track.append(tuple(pos))
    t+=1
    race[*pos] = t

# Find cheap jumps
savings = (Counter(), Counter())
jumps = (np.argwhere(manhatten_filter(cheats_p1, exact=True))-cheats_p1,
         np.argwhere(manhatten_filter(cheats_p2, exact=False))-cheats_p2)
for t, time in enumerate(track):
    for _savings, _jumps in zip(savings, jumps): # Parts 1 and 2
        jump_opts = race[*(time+_jumps).T]
        t_saved = jump_opts[jump_opts>t] - t - 1 - np.abs(_jumps).sum(axis=1)[jump_opts>t]
        for ts in t_saved:
            _savings[ts] += 1

print("Part 1: ", sum(savings[0][k] for k in savings[0] if k>=100))
print("Part 2: ", sum(savings[1][k] for k in savings[1] if k>=100))

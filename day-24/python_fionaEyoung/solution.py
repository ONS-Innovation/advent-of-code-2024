from operator import and_, xor, or_
from functools import partial
from collections import defaultdict

OPS = {'AND':and_, 'XOR':xor, 'OR':or_}

fname = 'input.txt'

with open(fname, 'r') as f:
    inits, conns = f.read().split('\n\n')

wires = {wire:int(val) for line in inits.splitlines() for wire, val in [line.split(': ')]}

gates = []

for line in conns.splitlines():
    l = line.split()
    l.remove('->')
    # name = l[4]
    op = l[1]
    for wire in [l[0], l[2], l[3]]:
        if wire not in wires:
            wires[wire] = None
    gates.append(tuple(l))

while any(w is None for w in wires.values()):
    for g in gates:
        if wires[g[-1]] is None:
            if all(x is not None for x in (wires[g[0]], wires[g[2]])):
                wires[g[-1]] = OPS[g[1]](wires[g[0]], wires[g[2]])

outwires = [w for w in wires.keys() if w.startswith('z')]
outwires.sort(reverse=True)
print("Part 1: ", int(''.join(str(int(wires[out])) for out in outwires),2))

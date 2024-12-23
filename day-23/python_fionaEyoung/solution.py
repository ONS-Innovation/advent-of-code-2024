from collections import defaultdict

class LAN_Network():

    def __init__(self, fname):
        with open(fname, 'r') as f:
            connections = f.read().splitlines()

        self.network = defaultdict(set)
        for c in connections:
            a, b = c.split('-')
            self.network[a].add(b)
            self.network[b].add(a)

    def find_clubs_of_3(self, filter_keys=None):
        clubs = set()
        for key in filter_keys or network.keys():
            stack = self.network[key].copy()
            while stack:
                neighbour = stack.pop()
                for ndbo in self.network[neighbour]:
                    if key in self.network[ndbo]:
                        clubs.add(frozenset({key, neighbour, ndbo}))
        return clubs

    def BronKerbosch(self, R, P, X):
        maximal_cliques = set()
        if not P and not X and len(R) > 2:
            maximal_cliques |= {frozenset(R)}
        vertices = P.copy()
        for v in vertices:
            reported = self.BronKerbosch(R | {v}, P & self.network[v], X & self.network[v])
            if reported: maximal_cliques |= reported
            P.remove(v)
            X.add(v)
        return maximal_cliques

    def find_maximal_clique(self):
        cliques = list(self.BronKerbosch(set(), set(self.network.keys()), set()))
        s = 0
        biggest_max_clique = None
        for c in cliques:
            if len(c) > s:
                s = len(c)
                biggest_max_clique = c
        return biggest_max_clique

    def __len__(self):
        return(len(self.network))

    def __iter__(self):
        yield from self.network.keys()

    def __repr__(self):
        return self.network.__repr__()

fname = 'input.txt'

net = LAN_Network(fname)

print("Part 1: ", len(net.find_clubs_of_3(filter_keys=[k for k in net.network if k.startswith('t')])))

password = list(net.find_maximal_clique())
password.sort()

print("Part 2: ", ','.join(password))

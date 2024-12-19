import regex
from functools import cache

class StringGraph:
    def __init__(self, n, edges):
        self.graph = {i:[] for i in range(n)}
        for n in edges:
            self.graph[n[0]].append(n[1])

    # Cache this function, same start+end combos aren't recomputed
    @cache
    def find_path(self, start, end):

        # initialise visit stack with neighbours of start
        stack = self.graph[start]
        found_paths = 0

        while stack:
            next_node = stack.pop()
            if next_node is end:
                found_paths += 1
                continue
            found_paths += self.find_path(next_node, end)

        return found_paths

fname = 'input.txt'
with open(fname, 'r') as f:
    patterns = f.readline().strip().split(', ')
    f.readline()
    designs = [l.strip() for l in f]

total_possible = 0
total_combos = 0
for design in designs:

    # Construct graph of matched substrings
    nodes = []
    for pattern in patterns:
        nodes.extend([m.span() for m in regex.finditer(pattern, design, overlapped=True)])

    graph = StringGraph(len(design), nodes)

    # Is the graph traversable?
    n = graph.find_path(0, len(design))
    total_possible += bool(n)
    total_combos += n

print("Part 1: ", total_possible)
print("Part 2: ", total_combos)

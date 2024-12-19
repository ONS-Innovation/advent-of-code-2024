import regex

def find_path(graph, start, end):
    # initialise visit stack with neighbours of start
    stack = graph[start]
    visited = [start]

    while stack:
        next_node = stack.pop()
        if next_node is end: return True
        if not next_node in visited:
            stack.extend(graph[next_node])
            visited.append(next_node)

    return False

fname = 'input.txt'
with open(fname, 'r') as f:
    patterns = f.readline().strip().split(', ')
    f.readline()
    designs = [l.strip() for l in f]

total_possible = 0
for design in designs:

    # Construct graph of matched substrings
    graph = {i:[] for i in range(len(design))}
    for pattern in patterns:
        nodes = [m.span() for m in regex.finditer(pattern, design, overlapped=True)]
        for n in nodes:
            graph[n[0]].append(n[1])

    # Is the graph traversable?
    total_possible += find_path(graph, 0, len(design))


print("Part 1: ", total_possible)

from collections import defaultdict

with open("input.txt") as f:
    input = f.read().splitlines()

graph = defaultdict(list)

for line in input:
    from_cave = line.split("-")[0]
    to_cave = line.split("-")[1]
    graph[from_cave].append(to_cave)
    graph[to_cave].append(from_cave)

paths = []


def traverse_graph_part_one(graph, current_node, path):
    path.append(current_node)
    for v in graph[current_node]:
        if v not in path or v.isupper():
            traverse_graph_part_one(graph, v, path.copy())
    if path[-1] == "end":
        paths.append(path)


traverse_graph_part_one(graph, "start", [])
print("Part A: " + str(len(paths)))


def path_only_single_small_cave_twice(path):
    lowercases = [n for n in path if n.islower()]
    return len(lowercases) == len(set(lowercases))


paths = []


def traverse_graph_part_two(graph, current_node, path):
    path.append(current_node)
    for v in graph[current_node]:
        if v not in path or v.isupper() or path_only_single_small_cave_twice(path):
            traverse_graph_part_two(graph, v, path.copy())
    if path[-1] == "end" and path.count("end") == 1 and path.count("start") == 1:
        paths.append(path)


traverse_graph_part_two(graph, "start", [])

print("Part B: " + str(len(paths)))

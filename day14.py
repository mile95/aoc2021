from collections import Counter
from collections import defaultdict

with open("input.txt") as f:
    input = f.read().splitlines()
 
insertions = dict()
template = ""

for line in input:
    if line and " -> " in line:
        left = line.split(" -> ")[0]
        right = line.split(" -> ")[1]
        insertions[left] = right
    elif line:
        template = line

def compute(steps):
    occurences = defaultdict(int)
    for i in range(len(template) - 1):
        occurences[template[i:i+2]] += 1

    for _ in range(steps):
        copy = occurences.copy()
        for k,v in occurences.items():
            if v > 0:
                new_char = insertions.get(k)
                new_pair_1 = k[0] + new_char
                new_pair_2 = new_char + k[1]
                copy[new_pair_1] += v
                copy[new_pair_2] += v
                copy[k] -= v
                if copy[k] < 0:
                    raise Exception
        occurences = copy

    chars = ""
    for c in occurences.keys():
        chars += c

    chars = set(chars)
    counts = defaultdict(int)
    for c in chars:
        for k in occurences.keys():
            if c == k[0]:
                counts[c] += occurences[k]

    counts[template[-1]] += 1
    return max(counts.values()) - min(counts.values())


print(f"Part A: {compute(10)}")
print(f"Part B: {compute(40)}")

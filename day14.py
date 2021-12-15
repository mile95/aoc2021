from collections import Counter

with open("input.txt") as f:
    input = f.read().splitlines()


STEPS = 10

insertions = dict()
template = ""

for line in input:
    if line and " -> " in line:
        left = line.split(" -> ")[0]
        right = line.split(" -> ")[1]
        insertions[left] = right
    elif line:
        template = line


for _ in range(STEPS):
    new_template = template[0]
    for i in range(len(template) - 1):
        pair = template[i : i + 2]
        new_template += insertions.get(pair) + pair[1]
    template = new_template

sorted_occurences = Counter(template).most_common()

print(f"Part A: {sorted_occurences[0][1] - sorted_occurences[-1][1]}")

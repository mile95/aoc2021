from collections import defaultdict

with open("input.txt") as f:
    input = f.read().splitlines()

def horizontal(grid, y_line):
    folded = set()
    for x, y in grid:
        folded.add((x, y if y < y_line else 2 * y_line - y))
    return folded

def vertical(grid, x_line):
    folded = set()
    for x, y in grid:
        folded.add((x if x < x_line else 2 * x_line - x, y))
    return folded

cords = set()
instructions = []
for line in input:
    if "fold" in line:
        instructions.append(line)
    elif line:
        x = int(line.split(',')[0])
        y = int(line.split(',')[1])
        cords.add((x,y))

for ins in instructions:
    axis = ins.split()[2].split('=')[0]
    val = int(ins.split()[2].split('=')[1])
    if axis == 'x':
        cords = vertical(cords, val)
    else:
        cords = horizontal(cords, val)


max_x = max(x for x, _ in cords)
max_y = max(y for _, y in cords)
output = []
for i in range(max_y + 1):
    output.append([' '] * (max_x + 1))

for x, y in cords:
    output[y][x] = '*'

print("Part B:")
print('\n'.join(''.join(row) for row in output))

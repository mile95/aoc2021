with open("input.txt") as f:
    input = f.read().split('\n')

horizontal = depth = 0

for ins in input:
    action, value = ins.split()
    if "down" in action:
        depth += int(value)
    if "up" in action:
        depth -= int(value)
    if "forward" in action:
        horizontal += int(value)

print("Part A: " + str(horizontal*depth))

horizontal = aim = depth = 0

for ins in input:
    action, value = ins.split()
    if "down" in action:
        aim += int(value)
    if "up" in action:
        aim -= int(value)
    if "forward" in action:
        horizontal += int(value)
        depth = depth + aim * int(value)

print("Part B: " + str(horizontal*depth))

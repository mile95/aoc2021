with open("input.txt") as f:
    input = f.read().split('\n')

gamma = ""
for i in range(len(input[0])):
    x = []
    for binary in input:
        x.append(binary[i])
    gamma += str(max(set(x), key=x.count))

epsilon = ''.join(["1" if g == "0" else "0" for g in gamma])

print("Part A: " + str(int(gamma, 2) * int(epsilon, 2)))

def ox(index, numbers):
    if len(numbers) == 1:
        return numbers[0]
    xs = []
    for binary in numbers:
        xs.append(binary[index])
    ones = xs.count("1")
    zeros = xs.count("0")
    new_numbers = []
    if ones >= zeros:
        positions = [i for i, val in enumerate(xs) if val == "1"]
        positions = positions[:ones]
        new_numbers = [numbers[p] for p in positions]
        return ox(index + 1, new_numbers)
    positions = [i for i, val in enumerate(xs) if val == "0"]
    positions = positions[:zeros]
    new_numbers = [numbers[p] for p in positions]
    return ox(index + 1, new_numbers)

def co(index, numbers):
    if len(numbers) == 1:
        return numbers[0]
    xs = []
    for binary in numbers:
        xs.append(binary[index])
    ones = xs.count("1")
    zeros = xs.count("0")
    new_numbers = []
    if zeros <= ones:
        positions = [i for i, val in enumerate(xs) if val == "0"]
        positions = positions[:zeros]
        new_numbers = [numbers[p] for p in positions]
        return co(index + 1, new_numbers)
    positions = [i for i, val in enumerate(xs) if val == "1"]
    positions = positions[:ones]
    new_numbers = [numbers[p] for p in positions]
    return co(index + 1, new_numbers)

print("Part B: " + str(int(ox(0, input),2) * int(co(0, input),2)))
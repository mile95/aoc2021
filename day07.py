with open("input.txt") as f:
    input = f.read().split(',')

numbers = list(map(int, input))

cost = dict()
for i in range(min(numbers), max(numbers) + 1):
    for n in numbers:
        cost[i] = cost.get(i, 0) + abs(n - i)

print("Part A: " + str(min(cost.values())))

cost = dict()
for i in range(min(numbers), max(numbers) + 1):
    for n in numbers:
        cost[i] = cost.get(i, 0) + sum(list(range(1, abs(n-i) + 1)))

print("Part B: " + str(min(cost.values())))

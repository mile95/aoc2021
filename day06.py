from collections import deque

with open("input.txt") as f:
    input = f.read().split(',')

numbers = list(map(int, input))


def compute(lanterns, days):
    state = deque([0] * 9)
    for lantern in lanterns:
        state[lantern] += 1

    for _ in range(days):
        new_lanterns = state.popleft()
        state[-2] += new_lanterns
        state.append(new_lanterns)

    return sum(state)

print("Part A: " + str(compute(numbers, 80)))
print("Part B: " + str(compute(numbers, 256)))

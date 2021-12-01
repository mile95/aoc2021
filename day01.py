with open("input.txt") as f:
    input = f.read().split('\n')

numbers = list(map(int, input))

c = sum([numbers[i] < numbers[i+1] for i in range(0, len(numbers) - 1)])
print('Part A: ' + str(c))

numbers = [sum(numbers[x:x+3]) for x in range(0, len(numbers), 1)]
c = sum([numbers[i] < numbers[i+1] for i in range(0, len(numbers) - 1)])
print('Part B: ' + str(c))

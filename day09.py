with open("input.txt") as f:
    input = f.read().splitlines()

data = [list(x) for x in input]
data = [map(int, x) for x in data]

def find_neighbours(row, column):
    neighbours = []
    neighbours.append((row + 1, column))
    neighbours.append((row, column + 1))
    if row > 0:
        neighbours.append((row - 1, column))
    if column > 0:
        neighbours.append((row, column - 1))
    return neighbours

s = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        neighbours = find_neighbours(i, j)
        oks = []
        for neigbour in neighbours:
            n_r, n_c = neigbour
            try:
                oks.append(data[n_r][n_c] > data[i][j])
            except IndexError:
                pass
        if all(oks):
            s += (data[i][j] + 1)
print("Part A: " + str(s))
        



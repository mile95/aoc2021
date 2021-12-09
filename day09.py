from typing import DefaultDict
import math

with open("input.txt") as f:
    input = f.read().splitlines()

data = [list(x) for x in input]
data = [list(map(int, x)) for x in data]


def find_neighbours(point):
    row, column = point[0], point[1]
    neighbours = []
    neighbours.append((row + 1, column))
    neighbours.append((row, column + 1))
    if row > 0:
        neighbours.append((row - 1, column))
    if column > 0:
        neighbours.append((row, column - 1))
    return neighbours


s = 0
lows = []
for i in range(len(data)):
    for j in range(len(data[i])):
        neighbours = find_neighbours((i, j))
        oks = []
        for neigbour in neighbours:
            n_r, n_c = neigbour
            try:
                oks.append(data[n_r][n_c] > data[i][j])
            except IndexError:
                pass
        if all(oks):
            s += data[i][j] + 1
            lows.append((i, j))
print("Part A: " + str(s))


def find_candidates(searched, current_candidates, accepted):
    if len(current_candidates) == 0:
        # There's a bug below. Atm, accepted can contain the same point more than once,
        # hence the set() call. I will see if I want to debug and fix sometime or not. Probably not.
        return len(set(accepted))
    new_candidates = []
    for c in current_candidates:
        try:
            if data[c[0]][c[1]] != 9:
                accepted.append(c)
                for n in find_neighbours(c):
                    if n not in searched or n not in accepted:
                        new_candidates.append(n)
        except IndexError:
            pass
        searched.append(c)
        current_candidates.remove(c)

    return find_candidates(searched, current_candidates + new_candidates, accepted)


lows_basin = {}
for low in lows:
    lows_basin[low] = find_candidates(
        searched=[], current_candidates=find_neighbours(low), accepted=[]
    )

print("Part B: " + str(math.prod(sorted(list(lows_basin.values()))[-3:])))

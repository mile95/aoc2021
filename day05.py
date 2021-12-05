with open("input.txt") as f:
    input = f.read().split('\n')

diagram = dict()

for entry in input:
    start, stop = entry.split("->")
    x1, y1 = list(map(int, start.split(',')))
    x2, y2 = list(map(int, stop.split(',')))
    if (x1 == x2) or (y1 == y2):
        xs = (list(range(min(x1,x2), max(x1,x2) + 1)))
        ys = (list(range(min(y1,y2), max(y1,y2) + 1)))
        if len(xs) == 1:
            for y in ys:
                key = str(xs[0]) + ":" + str(y)
                diagram[key] = diagram.get(key, 0) + 1
        elif len(ys) == 1:
            for x in xs:
                key = str(x) + ":" + str(ys[0])
                diagram[key] = diagram.get(key, 0) + 1

print("Part A: " + str(sum([x > 1 for x in diagram.values()])))

diagram = dict()

for entry in input:
    start, stop = entry.split("->")
    x1, y1 = list(map(int, start.split(',')))
    x2, y2 = list(map(int, stop.split(',')))
    xs = (list(range(min(x1,x2), max(x1,x2) + 1)))
    ys = (list(range(min(y1,y2), max(y1,y2) + 1)))
    if x1 > x2:
        xs.reverse()
    if y1 > y2:
        ys.reverse()
    if len(xs) == len(ys):
        for x,y in zip(xs, ys):
            key = str(x) + ":" + str(y)
            diagram[key] = diagram.get(key, 0) + 1
    elif len(xs) == 1:
        for y in ys:
            key = str(xs[0]) + ":" + str(y)
            diagram[key] = diagram.get(key, 0) + 1
    elif len(ys) == 1:
        for x in xs:
            key = str(x) + ":" + str(ys[0])
            diagram[key] = diagram.get(key, 0) + 1

print("Part B: " + str(sum([x > 1 for x in diagram.values()])))

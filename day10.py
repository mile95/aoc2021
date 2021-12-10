with open("input.txt") as f:
    input = f.read().splitlines()

def get_closing(c):
    if c == '<':
        return '>'
    if c == '(':
        return ')'
    if c == '[':
        return ']'
    if c == '{':
        return '}'

s = 0
openings = ['[', '<', '{', '(']
closing = [']', '>', '}', ')']
points1 = {')':3, ']':57, '}':1197, '>':25137}
remains = []
for line in input:
    open = []
    for c in line:
        if c in openings:
            open.append(c)
        elif c in closing:
            i = closing.index(c)
            if open[-1] == openings[i]:
                open = open[:-1]
            else:
                s += points1[c]
                break
    else:
        if len(open) > 0:
            remains.append([get_closing(o) for o in reversed(open)])
print(s)

scores = []
points2 = {')':1, ']':2, '}':3, '>':4}
for remain in remains:
    score = 0
    for c in remain:
        score = score * 5
        score += points2[c]
    scores.append(score)

middle_index = int((len(scores) - 1) / 2)
scores.sort()
print(scores[middle_index])

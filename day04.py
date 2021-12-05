with open("input.txt") as f:
    input = "".join(line for line in f if not line.isspace()).splitlines()

numbers = input[0].split(",")
numbers = list(map(int, numbers))
del input[0]
boards =  [input[i:i + 5] for i in range(0, len(input), 5)]

for i, board in enumerate(boards):
    for j, row in enumerate(board):
        boards[i][j] = list(map(int, row.split()))

def board_won(board):
    for c in list(zip(*board)):
        c = list(c)
        if c == ['.']*5:
            return True
    for r in board:
        if r == ['.']*5:
            return True
    return False

def compute_score(board, number):
    s = 0
    for r in board:
        s += sum(list(filter(lambda a: a != '.', r)))
    return s * number

def find_first_winner():
    for number in numbers:
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                if number in row:
                    boards[i][j] = ['.' if x==number else x for x in boards[i][j]]
                if board_won(board):
                    return compute_score(board, number)

def find_last_winner():
    winners = set()
    number_of_boards = len(boards)
    for number in numbers:
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                if number in row:
                    boards[i][j] = ['.' if x==number else x for x in boards[i][j]]
                if board_won(board):
                    winners.add(i)
                    if len(winners) == number_of_boards:
                        return compute_score(board, number)

print("Part A: " + str(find_first_winner()))
print("Part B: " + str(find_last_winner()))

        


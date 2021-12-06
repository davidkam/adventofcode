f = open("input.txt", "r")
# f = open("sample.txt", "r")
data = f.read().split("\n")

data.pop()

called_numbers = [int(x) for x in data.pop(0).split(",")]

data.pop(0)

marked_spot = 999

boards = []
board = []
for line in data:
    if line == "":
        boards.append(board)
        board = []
        continue
    board_numbers = [int(x) for x in line.split()]
    board.append(board_numbers)

# append last board
boards.append(board)


print(boards)
def checkRows(board):
    for row in board:
        tot = 0
        for y in range(5):
            if row[y] != marked_spot:
                break
            tot += row[y]
        if tot == (5 * marked_spot):
            return True
    return False


def checkColumns(board):
    first_row = board[0]
    for idx, number in enumerate(first_row):
        if number != marked_spot:
            continue
        tot = 0
        for x in range(1,5):
            if board[x][idx] != marked_spot:
                break
            tot += board[x][idx]
        if tot == (4 * marked_spot):
            return True
    return False


def checkDiagonals(board):
    tot1 = 0
    tot2 = 0
    for x in range(5):
        for y in range(5):
            if board[x][y] != marked_spot:
                return False
            if board[x][4 - y] != marked_spot:
                return False
            tot1 += board[x][y]
            tot2 += board[x][4 - y]
  
    if tot1 == (5 * marked_spot) or tot2 == (5 * marked_spot):
        return True

    return False

def markBoards(called_number, boards):
    for idx1, board in enumerate(boards):
        for idx2, line in enumerate(board):
            for idx3, number in enumerate(line):
                if number == called_number:
                    line[idx3] = marked_spot
            board[idx2] = line
        boards[idx1] = board


def checkWin(boards) :
    for board in boards:
        if checkRows(board):
            return board
        if checkColumns(board):
            return board
        if checkDiagonals(board):
            return board
 
    return None

for called_number in called_numbers:
    markBoards(called_number,boards)
    winning_board = checkWin(boards)

    if winning_board is not None:
        break


if winning_board is None:
    print("broken")

print(winning_board)
total = 0
for line in winning_board:
    for number in line:
        if number != marked_spot:
            total += number

print(total * called_number)

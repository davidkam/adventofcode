f = open("input.txt", "r")
# f = open("sample.txt", "r")
data = f.read().split("\n")

data.pop()

grid_size = 1000

grid = []
for x in range(grid_size):
    line = []
    for y in range(grid_size):
        line.append(0)
    grid.append(line)


def printGrid():
    for line in grid:
       print(line)
    print()

def drawVertical(col, start, ending):
    if start > ending:
        step = -1
    else:
        step = 1
    for y in range(start, ending + step, step):
        grid[y][col] += 1

def drawHorizontal(row, start, ending):
    if start > ending:
        step = -1
    else:
        step = 1
    for x in range(start, ending + step, step):
        grid[row][x] += 1
    
def drawDiagonal(x1, y1, x2, y2):
    print("diag")
    print(x1,y1,x2,y2)
    if x1 > x2:
       step = -1
    else:
       step = 1
    # y = mx + b
    slope = int((y2 - y1) / (x2 - x1))
    b = y1 - (slope * x1)
    for x in range(x1, x2 + step, step):
        y = (slope * x) + b
        grid[y][x] += 1

for line in data:
    points = line.split(" -> ")
    starting = [int(x) for x in points[0].split(",")]
    ending = [int(x) for x in points[1].split(",")]
    starting_x = starting[0]
    starting_y = starting[1]
    ending_x = ending[0]
    ending_y = ending[1]

    is_diagonal = False
    diff_x = ending_x - starting_x
    diff_y = ending_y - starting_y
    if diff_x == (-1 * diff_y) or diff_x == diff_y:
        is_diagonal = True
    if not(is_diagonal) and (starting_x != ending_x) and (starting_y != ending_y) and (diff_x == (-1 * diff_y)):
        continue

    if is_diagonal:
        drawDiagonal(starting_x, starting_y, ending_x, ending_y)
        continue

    if starting_x == ending_x:
        drawVertical(starting_x, starting_y, ending_y)
        continue
    if starting_y == ending_y:
        drawHorizontal(starting_y, starting_x, ending_x)
        continue

tot = 0
for line in grid:
    for point in line:
        if point > 1:
            tot += 1



print(tot)


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
    


for line in data:
    points = line.split(" -> ")
    starting = [int(x) for x in points[0].split(",")]
    ending = [int(x) for x in points[1].split(",")]
    starting_x = starting[0]
    starting_y = starting[1]
    ending_x = ending[0]
    ending_y = ending[1]

    if starting_x != ending_x and starting_y != ending_y:
        continue

    if starting_x == ending_x:
        drawVertical(starting_x, starting_y, ending_y)

    if starting_y == ending_y:
        drawHorizontal(starting_y, starting_x, ending_x)


tot = 0
for line in grid:
    for point in line:
        if point > 1:
            tot += 1



print(tot)


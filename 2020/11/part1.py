class SeatMap(object):
    OCCUPIED = '#'
    EMPTY    = 'L'
    FLOOR    = '.'

    def __init__(self, grid):
        self.__toggle_map = []
        self.__grid = grid
        self.__num_rows = len(grid)
        self.__num_cols = len(list(grid[0]))
        self.__num_rows_val = self.__num_rows - 1
        self.__num_cols_val = self.__num_cols - 1

    def getGrid(self):
        return self.__grid

    def resetToggle(self):
        self.__toggle_map = []
        for y in range(self.__num_rows):
            line = []
            for x in range(self.__num_cols):
                line.append(False)
            self.__toggle_map.append(line)

    def toggle(self):
        self.resetToggle()
        self.makeToggle()
        self.applyToggle()

    def printGrid(self):
        line = ""
        for y in range(self.__num_rows):
            for x in range(self.__num_cols):
                line += self.__grid[y][x]
            line += "\n"
        return line

    def makeToggle(self):
        for y in range(self.__num_rows):
            for x in range(self.__num_cols):
                self.checkToggle(y,x)
  
    def checkToggle(self, y, x):
        toggle_flag = False
        if self.__grid[y][x] == self.EMPTY:
            num_occupied = self.getNeighbors(y,x)
            if num_occupied == 0:
                toggle_flag = True

        if self.__grid[y][x] == self.OCCUPIED:
            num_occupied = self.getNeighbors(y,x)
            if num_occupied >= 4:
                toggle_flag = True

        self.__toggle_map[y][x] = toggle_flag

    def getNeighbors(self,y,x):
        nw = self.checkNW(y,x)
        n  = self.checkN(y,x)
        ne = self.checkNE(y,x)
        w  = self.checkW(y,x)
        e  = self.checkE(y,x)
        sw = self.checkSW(y,x)
        s  = self.checkS(y,x)
        se = self.checkSE(y,x)
        num_occupied = nw + n + ne + w + e + sw + s + se
        return num_occupied

    def applyToggle(self):
        for y in range(self.__num_rows):
            for x in range(self.__num_cols):
                if self.__toggle_map[y][x]:
                    self.toggleSeat(y,x)

    def toggleSeat(self, y, x):
        if self.__grid[y][x] == self.OCCUPIED:
            self.__grid[y][x] = self.EMPTY
        elif self.__grid[y][x] == self.EMPTY:
            self.__grid[y][x] = self.OCCUPIED

    def checkNW(self,y,x):
        if y == 0 or x == 0:
            return 0
        return 1 if self.__grid[y - 1][x - 1] == self.OCCUPIED else 0

    def checkN(self,y,x):
        if y == 0:
            return 0
        return 1 if self.__grid[y - 1][x] == self.OCCUPIED else 0

    def checkNE(self,y,x):
        if y == 0 or x == self.__num_cols_val:
            return 0
        return 1 if self.__grid[y - 1][x + 1] == self.OCCUPIED else 0

    def checkW(self,y,x):
        if x == 0:
            return 0
        return 1 if self.__grid[y][x -1] == self.OCCUPIED else 0

    def checkE(self,y,x):
        if x == self.__num_cols_val:
            return 0
        return 1 if self.__grid[y][x + 1] == self.OCCUPIED else 0

    def checkSW(self,y,x):
        if x == 0 or y == self.__num_rows_val:
            return 0
        return 1 if self.__grid[y + 1][x - 1] == self.OCCUPIED else 0

    def checkS(self,y,x):
        if y == self.__num_rows_val:
            return 0
        return 1 if self.__grid[y + 1][x] == self.OCCUPIED else 0

    def checkSE(self,y,x):
        if y == self.__num_rows_val or x == self.__num_cols_val:
            return 0
        return 1 if self.__grid[y + 1][x + 1] == self.OCCUPIED else 0
    
    def countOccupied(self):
        return sum(x.count(self.OCCUPIED) for x in self.__grid)
        
def copyGrid(orig_grid):
    copy_grid = []
    for line in orig_grid:
        copy_grid.append(line.copy())
    return copy_grid

f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

old_grid = []
for line in data:
    old_grid.append(list(line))

new_grid = copyGrid(old_grid)

done = False
while not done:
    seat = SeatMap(new_grid)
    seat.toggle()
    if seat.getGrid() == old_grid:
        done = True
    old_grid = copyGrid(seat.getGrid())


print(seat.countOccupied())

class Turtle:
    EAST = 'E'
    WEST = 'W'
    NORTH = 'N'
    SOUTH = 'S'
    DIRMAP = {
        0: NORTH,
        90: EAST,
        180: SOUTH,
        270: WEST
    }

    def __init__(self):
        self.orientation = self.EAST
        self.degrees = 90
        self.x = 0
        self.y = 0

    def run(self,line):
        command = line[0:1]
        units = line[1:]
        units = int(units)
        
        if command == 'F':
            self.forward(units)
        if command == 'N':
            self.moveN(units)
        if command == 'S':
            self.moveS(units)
        if command == 'W':
            self.moveW(units)
        if command == 'E':
            self.moveE(units)
        if command == 'L':
            self.turnLeft(units)
        if command == 'R':
            self.turnRight(units)

    def moveN(self,units):
        self.y += units

    def moveS(self,units):
        self.y -= units

    def moveW(self,units):
        self.x -= units

    def moveE(self,units):
        self.x += units

    def turnLeft(self,units):
        self.degrees += (360 - units)
        self.degrees = self.degrees % 360
        self.setOrientation()

    def turnRight(self,units):
        self.degrees += units
        self.degrees = self.degrees % 360
        self.setOrientation()

    def forward(self,units):
        dir = self.DIRMAP[self.degrees]
        func = 'move' + dir
        getattr(self,func)(units)

    def setOrientation(self):
        deg = self.degrees % 360
        if deg == 0:
            self.orientation = self.NORTH
        if deg == 90:
            self.orientation = self.EAST
        if deg == 180:
            self.orientation = self.SOUTH
        if deg == 270:
            self.orientation = self.WEST

    def getManhattan(self):
        return abs(self.x) + abs(self.y)

f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

turtle = Turtle()
for line in data:
    turtle.run(line)

print(turtle.getManhattan())

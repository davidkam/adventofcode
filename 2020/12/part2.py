import numpy

class Turtle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypointx = 10
        self.waypointy = 1

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
        self.waypointy += units

    def moveS(self,units):
        self.waypointy -= units

    def moveW(self,units):
        self.waypointx -= units

    def moveE(self,units):
        self.waypointx += units

    def turnLeft(self,units):
        units = units % 360
        self.rotate(units)

    def turnRight(self,units):
        units = 360 - units
        units = units % 360
        self.rotate(units)

    def rotate(self, units):
        waypoint_offset_x = self.x
        waypoint_offset_y = self.y

        waypointx = self.waypointx - self.x
        waypointy = self.waypointy - self.y
        theta = numpy.radians(units)
        r = numpy.array(
            (
                (numpy.cos(theta), -numpy.sin(theta)),
                (numpy.sin(theta),  numpy.cos(theta))
            )
        )
        wp = numpy.array((waypointx,waypointy))
        waypoint = numpy.rint(r.dot(wp))
        waypoint = waypoint.astype(int)
        self.waypointx = waypoint[0] + waypoint_offset_x
        self.waypointy = waypoint[1] + waypoint_offset_y

    def forward(self,units):
        stepx = self.waypointx - self.x
        stepy = self.waypointy - self.y

        self.x += (stepx * units)
        self.y += (stepy * units)

        self.waypointx = self.x + stepx
        self.waypointy = self.y + stepy

    def getManhattan(self):
        return abs(self.x) + abs(self.y)

f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

turtle = Turtle()
for line in data:
    turtle.run(line)

print(turtle.getManhattan())

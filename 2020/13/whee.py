import math

f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

t = int(data[0])
buses = data[1]
buses = {int(bus) for bus in buses.split(',') if bus != 'x'}
wait, bus = min((-t % bus, bus) for bus in buses)
print(wait * bus)

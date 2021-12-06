f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

x = 0
y = 0
for line in data:
    line_data = line.split(' ')
    ins = line_data[0]
    num = int(line_data[1])
    if ins == "forward":
        x += num
    if ins == "up":
        y -= num
    if ins == "down":
        y += num



print(x * y)

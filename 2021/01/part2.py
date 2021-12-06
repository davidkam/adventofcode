f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

cnt = 0
A = 0
B = 0
C = 0
prev = 1000000000
for x in data:
    C = B
    B = A
    A = int(x)
    total = A + B + C
    if total > prev:
        cnt += 1
    prev = total


print(cnt - 2)


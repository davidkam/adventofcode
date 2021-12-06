f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

cnt = 0
prev = 1000000000
for x in data:
    if int(x) > prev:
        cnt += 1
    prev = int(x)

print(cnt)

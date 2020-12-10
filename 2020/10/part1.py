f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

data = [int(i) for i in data]
data.sort()

num_elements = len(data)

tally = [0,1,0,1]


for x in range(num_elements - 1):
    cur_num = data[x]
    next_num = data[x + 1]
    diff = next_num - cur_num
    tally[diff] = tally[diff] + 1


print(tally)
print(tally[1] * tally[3])

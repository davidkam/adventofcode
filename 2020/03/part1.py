f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

num_rows = len(data)
num_cols = len(data[0])

num_trees = 0
x_pos = 0
for x in range(1,num_rows):
    x_pos += 3
    x_pos_mod = x_pos % num_cols
    if data[x][x_pos_mod] == '#':
        num_trees += 1

print(num_trees)



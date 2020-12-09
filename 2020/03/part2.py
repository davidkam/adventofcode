f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()


def countTrees(data,right,down):
    num_rows = len(data)
    num_cols = len(data[0])

    num_trees = 0
    x_pos = 0
    x = 0
    while x < num_rows - 1:
        x += down
        x_pos += right
        x_pos_mod = x_pos % num_cols
        if data[x][x_pos_mod] == '#':
            num_trees += 1

    return num_trees


run_1 = countTrees(data,1,1)
run_2 = countTrees(data,3,1)
run_3 = countTrees(data,5,1)
run_4 = countTrees(data,7,1)
run_5 = countTrees(data,1,2)
print(run_1 * run_2 * run_3 * run_4 * run_5)





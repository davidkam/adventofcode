import math

f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

data = [int(i) for i in data]
data.sort()

tot = 1
def calcRun(cur_run, tot):
    num_run = len(cur_run)
    if num_run > 2:
       if num_run == 5:
           tot *= 7
       else:
           power = num_run - 2
           tot *= int(math.pow(2, power))
    return tot

num_elements = len(data)
cur_run = [0]
cur_num = 0
for x in range(num_elements):
    next_num = data[x]
    diff = next_num - cur_num
    if diff == 1:
        cur_run.append(next_num)
    else:
        tot = calcRun(cur_run, tot)
        cur_run = [next_num]
    cur_num = data[x]

tot = calcRun(cur_run, tot)

print(tot)

f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

all_done = False
num_elements = len(data)

for x in range(num_elements - 2):
    first_num = data[x]
    for y in range(x + 1, num_elements - 1):
        second_num = data[y]
        if int(first_num) + int(second_num) == 2020:
            all_done = True
            break
    if all_done:
        break


print(int(first_num) * int(second_num))

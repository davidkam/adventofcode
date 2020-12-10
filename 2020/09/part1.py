f = open("input.txt", "r")
data = f.read().split("\n")

preamble = 25

data.pop()

num_elements = len(data)
for x in range(num_elements - preamble - 1):
    done = False
    value = int(data[x + preamble])
    
    sliced = [int(i) for i in data[x:(x + preamble)]] 
    sliced.sort()
    last_num = sliced[preamble - 1]
    
    for first_num in sliced:
        if first_num + last_num < value:
            continue
        for second_num in sliced:
            if first_num == second_num:
                continue
            sum_num = first_num + second_num
            if sum_num == value:
                done = True
                break
            if sum_num > value:
                break
        if done:
            break

    if not done:
        break

print(value)

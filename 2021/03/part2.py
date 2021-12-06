f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

orig = tuple(data)

def count(digit,data):
    cnt = 0
    for line in data:
        line_data = list(line)
        cnt += int(line_data[digit])
    return cnt


def keep_list(digit, val, data):
    return_data = []
    for line in data:
        line_data = list(line)
        if int(line_data[digit]) == val:
            return_data.append(line)
    
    return return_data


for x in range(12):
    num_bit = count(x,data)
    if num_bit < (len(data) / 2):
        data = keep_list(x, 0, data)
    else:
        data = keep_list(x, 1, data)

    if len(data) == 1:
        break


num1 = data
print(num1)

data = list(orig)
for x in range(12):
    num_bit = count(x,data)
    if num_bit < (len(data) / 2):
        data = keep_list(x, 1, data)
    else:
        data = keep_list(x, 0, data)

    if len(data) == 1:
        break

num2 = data
print(num2)


bin1 = "".join(num1)
bin2 = "".join(num2)


dec1 = int(bin1,2)
dec2 = int(bin2,2)
print(dec1 * dec2)

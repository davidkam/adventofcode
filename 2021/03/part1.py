f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

stats = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
]
for line in data:
    line_data = list(line)
    for idx, digit in enumerate(line_data):
        stats[idx] += int(digit)


num1 = []
num2 = []
for idx, stat in enumerate(stats):
    if stat < 500:
        num1.append("1")
        num2.append("0")
    else:
        num1.append("0")
        num2.append("1")


bin1 = "".join(num1)
bin2 = "".join(num2)


dec1 = int(bin1,2)
dec2 = int(bin2,2)
print(dec1 * dec2)

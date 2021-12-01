import math

f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

factor = int(data[0])
nums = data[1]
nums = nums.replace(',x','')
nums = [int(i) for i in nums.split(',')]
nums.sort()

diff = 10000
bus = None
for num in nums:
    x = -factor % num
    if x < diff:
        bus = num
        diff = x
print(bus * diff)


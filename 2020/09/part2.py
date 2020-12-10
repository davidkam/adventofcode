f = open("input.txt", "r")
data = f.read().split("\n")

needle = 57195069

data.pop()

done = False
pos = 0

key = data.index(str(needle))
sliced = [int(i) for i in data[0:key]]
num_elements = len(sliced)
    
while not done:
    for x in range(2,num_elements):
        inner_slice = sliced[pos:pos + x]
        tot = sum(inner_slice)
        if tot == needle:
            done = True
        if tot > needle:
            pos += 1
            break

inner_slice.sort()
print(inner_slice[0] + inner_slice[-1])



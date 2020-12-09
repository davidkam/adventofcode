def isLineValid(line):
    valid = False
    [data, str] = line.split(':')
    [occurences,char] = data.split(' ')
    [min,max] = occurences.split('-')
    min = int(min)
    max = int(max)
    num_occur = str.count(char)
    if num_occur >= min and num_occur <= max:
        valid = True
    return valid
    
f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

num_valid = 0
for line in data:
    if(isLineValid(line)):
        num_valid += 1

print(num_valid)


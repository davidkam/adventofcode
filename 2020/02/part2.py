def isLineValid(line):
    valid = False
    [data, password] = line.split(':')
    [occurences,char] = data.split(' ')
    [pos1,pos2] = occurences.split('-')
    pos1 = int(pos1)
    pos2 = int(pos2)
    if (password[pos1] == char or password[pos2] == char) and (password[pos1] != password[pos2]):
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


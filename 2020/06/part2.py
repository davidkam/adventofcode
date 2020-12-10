def getNumYes(answers):
    uniques = 'abcdefghijklmnopqrstuvwxyz'
    uniques = list(uniques)
    for answer in answers:
        answer = list(answer)
        uniques = list(set(uniques) & set(answer))
    return len(uniques)

f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()
num_yes = 0
group_data = []
for line in data:
    if line == '':
        num_yes += getNumYes(group_data)
        group_data = []
        continue
    group_data.append(line)

num_yes += getNumYes(group_data)
print(num_yes)

def getNumYes(answers):
    all_answers = list(''.join(answers))
    unique_answers = list(set(all_answers))
    return(len(unique_answers))

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

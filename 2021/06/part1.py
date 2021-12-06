f = open("input.txt", "r")
# f = open("sample.txt", "r")
data = sorted([int(x) for x in f.read().split(",")])

num_days = 80
new_fish = 7

fishes = {}
for fish in data:
    if fish not in fishes:
        fishes[fish] = 1
    else:
        fishes[fish] += 1


for x in range(num_days):
    temp_fish = {}
    for fish in fishes:
        num = fishes[fish]
        if fish == 0:
            fish = new_fish
            temp_fish[8] = num
        fish -= 1
        if fish in temp_fish:
            temp_fish[fish] += num
        else:
            temp_fish[fish] = num

    fishes = temp_fish


tot = 0
for fish in fishes:
    tot += fishes[fish]


print(tot)

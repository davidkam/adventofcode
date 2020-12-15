f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()
spoken = {}



def makeCalc(num, turn):
    if num in spoken:
        last = spoken[num]["last"]
        second_last = spoken[num]["second_last"]
        spoken[num] = {
            "last": turn,
            "second_last": last
        }
        last = spoken[num]["last"]
        second_last = spoken[num]["second_last"]
        if second_last == 0:
            next_num = turn - last
        else:
            next_num = last - second_last
    else:
        spoken[num] = {
            "last": turn,
            "second_last": 0
        }
        next_num = 0
    return next_num




turn = 0
seeds = data[0].split(',')
for seed in seeds:
    turn += 1
    last_num = makeCalc(int(seed),turn)

while turn < 30000000:
    prev_num = last_num
    turn += 1
    last_num = makeCalc(last_num,turn)


print(turn)
print(prev_num)

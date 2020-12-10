f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

acc = 0
executed = []
stack_pos = 0
done = False

while not(done):
    line = data[stack_pos]
    [ins,value] = line.split(' ')
    if ins == 'nop':
        stack_pos += 1

    if ins == 'acc':
        stack_pos += 1
        acc += int(value)
    if ins == 'jmp':
        stack_pos += int(value)

    if stack_pos not in executed:
        executed.append(stack_pos)
    else:
        done = True


print(acc)

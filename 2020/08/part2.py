f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()




def runProgram(program):
    acc = 0
    executed = []
    stack_pos = 0
    shorted = False
    done = False

    while not(done):
        line = program[stack_pos]
        [ins,value] = line.split(' ')
        if ins == 'nop':
            stack_pos += 1
    
        if ins == 'acc':
            stack_pos += 1
            acc += int(value)
        if ins == 'jmp':
            stack_pos += int(value)
    
        if stack_pos >= len(data):
            done = True
        if stack_pos not in executed:
            executed.append(stack_pos)
        else:
            shorted = True
            done = True

    return shorted, acc


invalid = True
changed = False
line_changed = []
num_lines = len(data)
while invalid:
    f = open("input.txt", "r")
    data = f.read().split("\n")

    data.pop()
    program = data
    for x in range(num_lines):
        line = program[x]
        [ins,value] = line.split(' ')
        if x not in line_changed:
            if ins == 'nop':
                if value != '+0' and value != '-0':
                    program[x] = 'jmp ' + value
                    line_changed.append(x)
                    break
            if ins == 'jmp':
                program[x] = 'nop ' + value
                line_changed.append(x)
                break
    invalid, tot = runProgram(program)

print(tot)

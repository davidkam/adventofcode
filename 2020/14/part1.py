f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

mask = []
memory = {}


for line in data:
    parts = line.split(' ')
    command = parts[0]
    mem = parts[2]
    if command == "mask":
        mask = list(mem)
    else:
        mask_length = len(mask)
        address = command
        address = int(address.replace('mem[','').replace(']',''))
        num = int(mem)
        bin = list(f'{num:036b}')
        for x in range(mask_length):
            mask_char = mask[x]
            if mask_char != 'X':
                bin[x] = mask_char
        new_num = int(''.join(bin), 2)
        memory[address] = new_num


print(sum(memory.values()))

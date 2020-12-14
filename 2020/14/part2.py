import math

f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

mask = []
memory = {}


for line in data:
    parts = line.split(' ')
    command = parts[0]
    value = parts[2]
    if command == "mask":
        mask = list(value)
    else:
        mask_length = len(mask)
        address = int(command.replace('mem[','').replace(']',''))
        address = list(f'{address:036b}')
        num_mask = 0
        for x in range(mask_length):
            mask_char = mask[x]
            if mask_char == 'X':
                ascii_mask_char = 65 + num_mask
                num_mask += 1
                address[x] = chr(ascii_mask_char)
            if mask_char == '1':
                address[x] = '1'
 
        address = ''.join(address)
        combos = int(math.pow(2,num_mask))
        for x in range(combos):
            bin_val = f'{x:036b}'
            bin_val = list(bin_val[-num_mask:])
            work_address = address
            for y in range(num_mask):
                num_val = bin_val[y]
                ascii_key = chr(65 + y)
                work_address = work_address.replace(ascii_key,num_val)
            memory[work_address] = int(value)

print(sum(memory.values()))

f = open("input.txt", "r")
data = f.read().split("\n")
data.pop()


row = 0
part_numbers = []
for line in data:
  col = 0
  buf = ''
  for char in line:
    if char.isdigit():
      buf += char
    else:
      if buf != '':
        part_numbers.append({buf: {'x': row + 1, 'y': col - len(buf) + 1}})
        buf = ''
    col += 1
  if buf != '':
    part_numbers.append({buf: {'x': row + 1, 'y': col - len(buf) + 1}})
    buf = ''
  row += 1


engine_mask = []
empty_line = [0] * (len(line) + 2)
engine_mask.append(empty_line)
for line in data:
  mask_line = [0]
  for char in line:
    if not char.isdigit() and char != '.':
      mask_line.append(1)
    else:
      mask_line.append(0)
  mask_line.append(0)
  engine_mask.append(mask_line)

engine_mask.append(empty_line)

for line in engine_mask:
  for char in line:
    print(char, end="")
  print()

sum = 0
for info in part_numbers:
  num = list(info.keys())[0]
  x = info[num]['x']
  y = info[num]['y']
  print(num,x,y)
  if (engine_mask[x][y + len(num)] == 1 or engine_mask[x][y - 1] == 1 or
      engine_mask[x - 1][y + len(num)] == 1 or engine_mask[x - 1][y - 1] == 1 or
      engine_mask[x + 1][y + len(num)] == 1 or engine_mask[x + 1][y - 1] == 1
      ):
    print('adding1',num,x,y)
    sum += int(num)
    continue
  for i in range(len(num)):
    if engine_mask[x - 1][y + i] == 1 or engine_mask[x + 1][y + i] == 1:
      print('adding2',num,x,y)
      sum += int(num)
      break

print(sum)

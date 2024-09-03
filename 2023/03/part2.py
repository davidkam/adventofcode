f = open("input.txt", "r")
data = f.read().split("\n")
data.pop()


row = 0
part_numbers = []
parts = []
for line in data:
  parts.append([])
  col = 0
  buf = ''
  for char in line:
    if char.isdigit():
      buf += char
    else:
      if buf != '':
        part_numbers.append({buf: {'x': row, 'y': col - len(buf)}})
        buf = ''
    col += 1
    if char == '*':
      parts[row].append('*')
    else:
      parts[row].append(0)
  if buf != '':
    part_numbers.append({buf: {'x': row, 'y': col - len(buf)}})
    buf = ''
  row += 1

for part in part_numbers:
  num = list(part.keys())[0]
  x = part[num]['x']
  y = part[num]['y']
  for i in range(len(num)):
    parts[x][y + i] = int(num)


padded_parts = []
empty_line = [0] * (len(parts[0]) + 2)
padded_parts.append(empty_line)
for line in parts:
  mask_line = [0]
  mask_line.extend(line)
  mask_line.append(0)
  padded_parts.append(mask_line)

padded_parts.append(empty_line)

sum = 0
for y in range(len(padded_parts)):
  line = padded_parts[y]
  for x in range(len(line)):
    char = padded_parts[y][x]
    if char == '*':
      gears = []
      # check row above
      num = padded_parts[y-1][x-1]
      if num and num != '*' and num not in gears:
        gears.append(num)
      num = padded_parts[y-1][x]
      if num and num != '*' and num not in gears:
        gears.append(num)
      num = padded_parts[y-1][x+1]
      if num and num != '*' and num not in gears:
        gears.append(num)
      # check same row
      num = padded_parts[y][x+1]
      if num and num != '*':
        gears.append(num)
      num = padded_parts[y][x-1]
      if num and num != '*':
        gears.append(num)
      # check row below
      num = padded_parts[y+1][x-1]
      if num and num != '*' and num not in gears:
        gears.append(num)
      num = padded_parts[y+1][x]
      if num and num != '*' and num not in gears:
        gears.append(num)
      num = padded_parts[y+1][x+1]
      if num and num != '*' and num not in gears:
        gears.append(num)
 

      if len(gears) == 2:
        sum += (gears[0] * gears[1])
      elif len(gears) == 1:
        pass
      else:
        print(gears)


print()
print(sum)

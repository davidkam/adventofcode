import re

with open('input.txt', 'r') as f:
  data = f.read().split("\n")
data.pop()


info = data.pop(0)
data.pop(0)
info = info.replace('L','0')
info = info.replace('R','1')
steps = list(info)

map = {}
for line in data:
  print(line)
  (key, value) = line.split(" = ")
  stuff = re.findall(r'(\w+), (\w+)', value)
  map[key] = stuff[0]

print(map)
start = 'AAA'
done = False
cnt = 0
while not done:
  step = int(info[cnt % len(steps)])
  cnt += 1
  dest = map[start][step]
  print(dest)
  if dest == 'ZZZ':
    done = True
  start = dest

print(cnt)

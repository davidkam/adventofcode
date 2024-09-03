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
starts = []
ends = []
for line in data:
  (key, value) = line.split(" = ")
  stuff = re.findall(r'(\w+), (\w+)', value)
  map[key] = stuff[0]
  if key[-1] == 'A':
    starts.append(key)
  if key[-1] == 'Z':
    ends.append(key)

done = False
cnt = 0
while not done:
  step = int(info[cnt % len(steps)])
  cnt += 1
  
  tstarts = []
  tdone = []
  tends = []
  for start in starts:
    dest = map[start][step]
    tends.append(dest)
    if dest in ends:
      tdone.append(True)
    else:
      tdone.append(False)
    tstarts.append(dest)

  print(step, tstarts, tends, cnt)
  starts = tstarts
  if False not in tdone:
    done = True

print(cnt)

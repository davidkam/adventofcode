import re

with open('input.txt', 'r') as f:
  data = f.read().split("\n")


durations = re.findall(r'\d+', data[0])
records = re.findall(r'\d+', data[1])

mult = 1
for x in range(len(durations)):
  duration = int(durations[x])
  record = int(records[x])
  distances = [(i * (duration - i) for i in range(duration + 1))]
  
  print('info',duration,record)
  cnt = 0
  for x in distances:
    for y in x:
      if y > record:
        cnt += 1

  mult *= cnt


print(mult)
      

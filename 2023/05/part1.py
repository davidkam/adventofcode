f = open("sample.txt", "r")
data = f.read().split("\n")
data.pop()


def pprint(list_data, additional_params = ''):
  for char in list_data:
    if char == 'X':
      char = 0
    print('%02d ' % char, end="")

  if additional_params != '':
    print('',additional_params, end="")
  print()

seed_line = data.pop(0)
(junk, seed_list) = seed_line.split(': ')
seeds = [int(i) for i in seed_list.split()]

data.pop(0)

# find largest number
max_num = 0
sections = 0
for line in data:
  if line == '':
    sections += 1
    continue
  if not [*line][0].isdigit():
    continue
  
  nums = [int(i) for i in line.split()]
  if nums[0] + nums[2] > max_num:
    max_num = nums[0] + nums[2]



sections += 2

container = [[]]*sections

container[0] = [i for i in range(max_num)]
for x in range(1,sections):
  line =[0]*max_num
  container[x] = line
  for y in range(max_num):
    container[x][y] = 'X'


section_cnt = 1
for line in data:
  print('line',line,section_cnt)
  if line == '': 
    pprint(container[0])
    pprint(container[section_cnt - 1], container[section_cnt-1][79])
    if section_cnt > 1:
      pprint(container[section_cnt - 2], container[section_cnt-2][79])
    pprint(container[section_cnt])
    for x in range(max_num):
      if container[section_cnt][x] == 'X':
        if container[section_cnt][x] != x:
          container[section_cnt][x] = container[section_cnt - 1][x]
        else:
          container[section_cnt][x] = x
    pprint(container[section_cnt], container[section_cnt][79])
    print()
        
    section_cnt += 1
    continue
  if not [*line][0].isdigit():
    continue

  (destination, source, steps) = [int(i) for i in line.split()]
  for i in range(steps):
    print(section_cnt, source + i)
    container[section_cnt][source + i] = destination + i



for seed in seeds:
  for i in range(len(container)):
    print(container[i][seed])
  print()


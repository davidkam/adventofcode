import re

with open('input.txt', 'r') as f:
    puzzle_input = f.read()

segments = puzzle_input.split('\n\n')
seed_info = re.findall(r'\d+', segments[0])

min_location = float('inf')
for stuff in range(int(len(seed_info) / 2)):
  seed_start = int(seed_info[2 * stuff])
  seed_range = int(seed_info[2 * stuff + 1])
  print('ss', seed_start, seed_range)
  for x in range(seed_start, seed_start +seed_range):
    print('i', stuff, x, seed_start, seed_start + seed_range)
    for seg in segments[1:]:
        for conversion in re.findall(r'(\d+) (\d+) (\d+)', seg):
            destination, start, delta = map(int, conversion)
            if x in range(start, start + delta):
                x += destination - start
                break

    min_location = min(x, min_location)



print(min_location)

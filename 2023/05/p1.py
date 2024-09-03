import re

with open('input.txt', 'r') as f:
    puzzle_input = f.read()

segments = puzzle_input.split('\n\n')
print('segments', segments)
seeds = re.findall(r'\d+', segments[0])
print('seeds',seeds)

min_location = float('inf')
for x in map(int, seeds):
    for seg in segments[1:]:
        print('seg',seg)
        for conversion in re.findall(r'(\d+) (\d+) (\d+)', seg):
            destination, start, delta = map(int, conversion)
            if x in range(start, start + delta):
                x += destination - start
                print('x',x)
                break

    min_location = min(x, min_location)



print(min_location)

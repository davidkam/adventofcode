f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

needle = 'shiny_gold'
needles = []
bag_map = {}
for line in data:
    line = line.replace('.','')
    [key_str, map_str] = line.split(' contain ')
    key_str = key_str.replace(' ','_')
    key_str = key_str.replace('_bags','')
    maps = map_str.split(', ')
    if maps != ['no other bags']:
        bag_map[key_str] = {}
        for map in maps:
            [num, adj, color, junk] = map.split(' ')
            bag_key_str = adj + '_' + color
            bag_map[key_str][bag_key_str] = num
            if bag_key_str == needle:
                if key_str not in needles:
                    needles.append(key_str)
    else:
        bag_map[key_str] = {}

def walkBags(bag_key, spacer):
    if bag_key in needles or bag_key == needle:
        return True
    for inner_bag in bag_map[bag_key]:
        found = walkBags(inner_bag,spacer + '  ')
        if found:
            if bag_key not in needles:
               needles.append(bag_key)
            return True
    return False


for outer_bag in bag_map:
    if outer_bag != needle:
        if walkBags(outer_bag,''):
          if outer_bag not in needles:
              needles.append(outer_bag)
        

print(len(needles))

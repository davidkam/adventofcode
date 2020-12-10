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
    tot_bags = 1
    inner_bags = bag_map[bag_key]
    if inner_bags == {}:
        return 1
    for inner_bag in bag_map[bag_key]:
        num = bag_map[bag_key][inner_bag]
        tot_bags += (int(num) * walkBags(inner_bag,spacer + '  '))
   
    return tot_bags



num_bags = walkBags('shiny_gold','')
print(num_bags - 1)

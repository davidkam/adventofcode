f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

buses = {}
nums = data[1].split(',')
for x in range(len(nums)):
    num = nums[x]
    if num != 'x':
        buses[int(num)] = x
    

sorted_buses = sorted(buses.keys())

largest_bus = sorted_buses[-1]
largest_bus_offset = buses[largest_bus]

del(buses[largest_bus])

done = False
x = 0
while not done:
    broken = False
    x += 1
 
    num_check = largest_bus * x - largest_bus_offset
    for bus in buses:
        offset = buses[bus]
        if (num_check + offset) % bus != 0:
            broken = True
            break
    if broken:
        continue  
    done = True


print(num_check)

f = open("input.txt", "r")
data = f.read().split("\n")

data.pop()

cycles = 1
start_dimensions = len(data)
final_dimensions = start_dimensions + (2 * cycles)

cube = []


def checkNeighbors(x,y,z):
    num_active = 0
    for check_x in range(x - 1, x + 2):
        for check_y in range(y - 1, y + 2):
            for check_z in range(z - 1, z + 2):
                if x == check_x and y == check_y and z == check_z:
                    continue
                if cube[check_x][check_y][check_z] == '#':
                    num_active += 1
    return num_active

def initCube():
    new_cube = []
    for x in range(final_dimensions):
        y_array = []
        for y in range(final_dimensions):
            z_array = []
            for z in range(final_dimensions):
                z_array.append(".")
            y_array.append(z_array)
        new_cube.append(y_array)
    return new_cube

def cloneCube():
    clone_cube = []
    for x in range(final_dimensions):
        clone_y_array = []
        for y in range(final_dimensions):
            clone_z_array = []
            for z in range(final_dimensions):    
                clone_z_array.append(cube[x][y][z])
            clone_y_array.append(clone_z_array)
        clone_cube.append(clone_y_array)
    return clone_cube

def cycle():
    print(cube)
    clone_cube = cloneCube()
    for x in range(1,final_dimensions- 1):
        for y in range(1,final_dimensions - 1):
            for z in range(1,final_dimensions - 1):
                current_pos = cube[x][y][z]
                print(current_pos)
                num_neighbors = checkNeighbors(x,y,z)
                if current_pos == '.':
                    if num_neighbors == 3:
                        print("inactive flip")
                        clone_cube[x][y][z] == '#'
                        print(str(x) + ':' + str(y) + str(z))
                if current_pos == '#':
                    if num_neighbors != 2 and num_neighbors != 3:    
                        print("active flip")
                        clone_cube[x][y][z] == '.'
    return clone_cube

cube = initCube()

offset = cycles 

for x, line in enumerate(data):
    for y, element in enumerate([char for char in line]):
        cube[x + offset][y + offset][0] = element


for cnt in range(cycles):
    clone_cube = cycle()
    print(cube)
    print()
    print(clone_cube)

def get_active_neighbors(cube, x, y, z):
    count = 0
    for x_dir in range(-1, 2):
        for y_dir in range(-1, 2):
            for z_dir in range(-1, 2):
                cube_to_check = (x + x_dir, y + y_dir, z + z_dir)
                if cube_to_check != (x, y, z) and cube_to_check in cube and cube[cube_to_check] == '#':
                    count += 1 
    return count

def cycle(cube, x_min, x_max, y_min, y_max, z_min, z_max):
    new_cube = {}
    new_x_min = x_min
    new_x_max = x_max
    new_y_min = y_min
    new_y_max = y_max
    new_z_min = z_min
    new_z_max = z_max

    for x in range(x_min - 1, x_max + 2):
        for y in range(y_min - 1 , y_max + 2):
            for z in range(z_min - 1, z_max + 2):
                cube_to_check = (x, y, z)
                active_neighbors = get_active_neighbors(cube, x, y, z)
                if active_neighbors == 3 or active_neighbors == 2 and cube_to_check in cube and cube[cube_to_check] == '#':
                    new_cube[cube_to_check] = '#'
                    if x < new_x_min:
                        new_x_min = x
                    if x > new_x_max:
                        new_x_max = x
                    if y < new_y_min:
                        new_y_min = y
                    if y > new_y_max:
                        new_y_max = y
                    if z < new_z_min:
                        new_z_min = z
                    if z > new_z_max:
                        new_z_max = z
    return new_cube, new_x_min, new_x_max, new_y_min, new_y_max, new_z_min, new_z_max

def get_active_neighbors2(cube, x, y, z, w):
    count = 0
    for x_dir in range(-1, 2):
        for y_dir in range(-1, 2):
            for z_dir in range(-1, 2):
                for w_dir in range(-1, 2):
                    cube_to_check = (x + x_dir, y + y_dir, z + z_dir, w + w_dir)
                    if cube_to_check != (x, y, z, w) and cube_to_check in cube and cube[cube_to_check] == '#':
                        count += 1 
    return count

def cycle2(cube, x_min, x_max, y_min, y_max, z_min, z_max, w_min, w_max):
    new_cube = {}
    new_x_min = x_min
    new_x_max = x_max
    new_y_min = y_min
    new_y_max = y_max
    new_z_min = z_min
    new_z_max = z_max
    new_w_min = w_min
    new_w_max = w_max

    for x in range(x_min - 1, x_max + 2):
        for y in range(y_min - 1 , y_max + 2):
            for z in range(z_min - 1, z_max + 2):
                for w in range(w_min - 1, w_max + 2):
                    cube_to_check = (x, y, z, w)
                    active_neighbors = get_active_neighbors2(cube, x, y, z, w)
                    if active_neighbors == 3 or active_neighbors == 2 and cube_to_check in cube and cube[cube_to_check] == '#':
                        new_cube[cube_to_check] = '#'
                        if x < new_x_min:
                            new_x_min = x
                        if x > new_x_max:
                            new_x_max = x
                        if y < new_y_min:
                            new_y_min = y
                        if y > new_y_max:
                            new_y_max = y
                        if z < new_z_min:
                            new_z_min = z
                        if z > new_z_max:
                            new_z_max = z
                        if w < new_w_min:
                            new_w_min = w
                        if w > new_w_max:
                            new_w_max = w
    return new_cube, new_x_min, new_x_max, new_y_min, new_y_max, new_z_min, new_z_max, new_w_min, new_w_max

def main():
    cube = {}
    big_cube = {}
    with open('input/input17.txt', 'r') as input:
        y = 0
        for line in input:
            x_max = len(line.strip())
            for x in range(x_max):
                cube[(x, y, 0)] = line[x]
                big_cube[(x, y, 0, 0)] = line[x]
            y += 1
    
    x_min = 0
    x_max -= 1
    y_min = 0
    y_max = y - 1
    z_min = 0
    z_max = 0
    w_min = 0
    w_max = 0

    for i in range(6):
        cube, x_min, x_max, y_min, y_max, z_min, z_max = cycle(cube, x_min, x_max, y_min, y_max, z_min, z_max)
        big_cube, x_min, x_max, y_min, y_max, z_min, z_max, w_min, w_max = cycle2(big_cube, x_min, x_max, y_min, y_max, z_min, z_max, w_min, w_max)

    print("Part 1: ", len(cube))
    print("Part 2: ", len(big_cube))

if __name__ == "__main__":
    main()

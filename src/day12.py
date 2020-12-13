def new_direction_left(start, degrees):
    num_dirs = degrees / 90 % 4 
    directions = ['N', 'E', 'S', 'W']
    if num_dirs == 4:
        return start
    if num_dirs == 1 and start == 'N':
        return 'W'
    if num_dirs == 2 and start == 'N':
        return 'S'
    if num_dirs == 3 and start == 'N':
        return 'E'
    if num_dirs == 1 and start == 'E':
        return 'N'
    if num_dirs == 2 and start == 'E':
        return 'W'
    if num_dirs == 3 and start == 'E':
        return 'S'
    if num_dirs == 1 and start == 'S':
        return 'E'
    if num_dirs == 2 and start == 'S':
        return 'N'
    if num_dirs == 3 and start == 'S':
        return 'W'
    if num_dirs == 1 and start == 'W':
        return 'S'
    if num_dirs == 2 and start == 'W':
        return 'E'
    if num_dirs == 3 and start == 'W':
        return 'N'
    return

def new_direction_right(start, degrees):
    num_dirs = degrees / 90 % 4 
    directions = ['N', 'E', 'S', 'W']
    if num_dirs == 4:
        return start
    if num_dirs == 1 and start == 'N':
        return 'E'
    if num_dirs == 2 and start == 'N':
        return 'S'
    if num_dirs == 3 and start == 'N':
        return 'W'
    if num_dirs == 1 and start == 'E':
        return 'S'
    if num_dirs == 2 and start == 'E':
        return 'W'
    if num_dirs == 3 and start == 'E':
        return 'N'
    if num_dirs == 1 and start == 'S':
        return 'W'
    if num_dirs == 2 and start == 'S':
        return 'N'
    if num_dirs == 3 and start == 'S':
        return 'E'
    if num_dirs == 1 and start == 'W':
        return 'N'
    if num_dirs == 2 and start == 'W':
        return 'E'
    if num_dirs == 3 and start == 'W':
        return 'S'
    return

def manhattan_distance(east_west, north_south):
    return abs(east_west) + abs(north_south)

def rotate_right(x, y, waypoint_x, waypoint_y, degrees):
    x_diff = waypoint_x - x
    y_diff = waypoint_y - y
    num_dirs = degrees / 90 % 4 
    if num_dirs == 1:
        return x + y_diff, y - x_diff
    if num_dirs == 2:
        return x - x_diff, y - y_diff
    if num_dirs == 3:
        return x - y_diff, y + x_diff
    return

def rotate_left(x, y, waypoint_x, waypoint_y, degrees):
    x_diff = waypoint_x - x
    y_diff = waypoint_y - y
    num_dirs = degrees / 90 % 4 
    if num_dirs == 3:
        return x + y_diff, y - x_diff
    if num_dirs == 2:
        return x - x_diff, y - y_diff
    if num_dirs == 1:
        return x - y_diff, y + x_diff
    return

def main():
    with open('input/input12.txt', 'r') as input:
        instructions = [(line.strip()[0], int(line.strip()[1:])) for line in input]

    # (-) W --- E (+) x axis
    # (-) S --- N (+) y axis
    direction = 'E'
    x = 0
    y = 0
    for instruction in instructions:
        if instruction[0] == 'E':
            x += instruction[1]
        elif instruction[0] == 'W':
            x -= instruction[1]
        elif instruction[0] == 'N':
            y += instruction[1]
        elif instruction[0] == 'S':
            y -= instruction[1]
        elif instruction[0] == 'F':
            if direction == 'E':
                x += instruction[1]
            elif direction == 'W':
                x -= instruction[1]
            elif direction == 'N':
                y += instruction[1]
            elif direction == 'S':
                y -= instruction[1]
        elif instruction[0] == 'L':
            direction = new_direction_left(direction, instruction[1])
        elif instruction[0] == 'R':
            direction = new_direction_right(direction, instruction[1])
    print("Part 1: ", manhattan_distance(x, y))
    
    # PART 2
    # x, y is ship
    waypoint_x = 10
    waypoint_y = 1
    x = 0
    y = 0
    for instruction in instructions:
        if instruction[0] == 'E':
            waypoint_x += instruction[1]

        elif instruction[0] == 'W':
            waypoint_x -= instruction[1]

        elif instruction[0] == 'N':
            waypoint_y += instruction[1]

        elif instruction[0] == 'S':
            waypoint_y -= instruction[1]
        
        # move to waypoint that number of itmes
        elif instruction[0] == 'F':
            move_x = waypoint_x - x
            move_y = waypoint_y - y
            x += move_x * instruction[1]
            y += move_y * instruction[1]
            waypoint_x += move_x * instruction[1]
            waypoint_y += move_y * instruction[1]

        elif instruction[0] == 'L':
            waypoint_x, waypoint_y = rotate_left(x, y, waypoint_x, waypoint_y, instruction[1])
        elif instruction[0] == 'R':
            waypoint_x, waypoint_y = rotate_right(x, y, waypoint_x, waypoint_y, instruction[1])
    
    print("Part 2: ", manhattan_distance(x, y))

if __name__ == "__main__":
    main()
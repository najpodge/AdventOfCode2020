def get_num_occupied_part1(row, col, seats):
    occupied = 0
    num_rows = len(seats)
    num_cols = len(seats[0])
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not (x == 0 and y == 0) and row + x < num_rows and row + x >= 0 and col + y < num_cols and col + y >= 0:
                if seats[row + x][col + y] == '#':
                    occupied += 1
    return occupied

def occupied_seat_visible(row, col, row_increment, col_increment, seats):
    row += row_increment
    col += col_increment
    num_rows = len(seats)
    num_cols = len(seats[0])
    while row < num_rows and row >= 0 and col < num_cols and col >= 0:
        if seats[row][col] == '#':
            return True
        elif seats[row][col] == 'L':
            return False
        row += row_increment
        col += col_increment
    return False

def get_num_occupied_part2(row, col, seats):
    occupied = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not (x == 0 and y == 0):
                occupied += occupied_seat_visible(row, col, x, y, seats)
    return occupied    

def apply_rules(original_seats, tolerance, occupied_function):
    new_seats = [row[:] for row in original_seats]
    for row in range(len(original_seats)):
        for col in range(len(original_seats[0])):
            seat = original_seats[row][col]
            adjacent_occupied = 0
            if not seat == '.':
                adjacent_occupied = occupied_function(row, col, original_seats)# if part == 1 else get_num_occupied_part2(row, col, original_seats)
            if seat == 'L' and adjacent_occupied == 0:
                new_seats[row][col] = '#'
            elif seat == '#' and adjacent_occupied >= tolerance:
                new_seats[row][col] = 'L'
    return new_seats, new_seats != original_seats

def print_seat(seats):
    for row in seats:
        temp = ""
        for col in row:
            temp += col
        print(temp)

def count_occupied(seats):
    count = 0
    for row in seats:
        for col in row:
            if col == '#':
                count += 1
    return count

def main():
    with open('input/input11.txt', 'r') as input:
        seats = [list(line.strip()) for line in input]

    seats_part1, changed = apply_rules(seats, 4, get_num_occupied_part1)
    while changed:
        seats_part1, changed = apply_rules(seats_part1, 4, get_num_occupied_part1)
    print("Part 1 answer: ", count_occupied(seats_part1))

    seats_part2, changed  = apply_rules(seats, 5, get_num_occupied_part2)
    while changed:
        seats_part2, changed = apply_rules(seats_part2, 5, get_num_occupied_part2)
    print("Part 2 answer: ", count_occupied(seats_part2))

if __name__ == "__main__":
    main()

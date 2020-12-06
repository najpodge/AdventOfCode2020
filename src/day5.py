import math

def go_lower(lower,upper):
    return math.floor((upper + lower) / 2)

def go_higher(lower, upper):
    return math.ceil((upper + lower) / 2)

def get_value(code):
    lower = 0
    upper = math.pow(2, len(code)) - 1
    for letter in code:
        if letter == 'F' or letter == 'L':
            upper = go_lower(lower, upper)
        else:
            lower = go_higher(lower, upper)
    return lower

def main():
    boarding_passes = []
    with open('input/input5.txt', 'r') as input:
        for line in input:
            boarding_passes.append((line[0:7],line[7:].strip()))

    seat_ids = []
    possible_seat_ids = range(0, 1023)
    for boarding_pass in boarding_passes:
        row = get_value(boarding_pass[0])
        col = get_value(boarding_pass[1])
        seat_ids.append(row * 8 + col)
    
    # For part 2, I should be validating that all of the adjacent seats are there,
    # but being lazy because I only had one missing seat anyway.
    seat_ids.sort()
    missing = [x for x in range(seat_ids[0], seat_ids[-1]+1) if x not in seat_ids] 
    print(seat_ids)
    print(missing)
    print("Part 1: ", max(seat_ids))
    print("Part 2: ", missing[0])

if __name__ == "__main__":
    main()
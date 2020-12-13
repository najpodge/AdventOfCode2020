import math
import sys

def get_start_time(start_time, increment, bus1, bus2, index2):
    assertion = (start_time + index2) % bus2
    while assertion != 0:
        start_time += increment
        assertion = (start_time + index2) % bus2
    return start_time

def get_increment(start_time, increment, bus1, bus2, index2):
    next_time = get_start_time(start_time + increment, increment, bus1, bus2, index2)
    return next_time - start_time

def main():
    buses = []
    with open('input/input13.txt', 'r') as input:
        depart_time = int(input.readline().strip())
        index = 0
        for bus in input.readline().split(','):
            if bus != 'x':
                buses.append((int(bus), index))
            index += 1
    
    # PART ONE
    earliest_bus = 0
    earliest_departure = sys.maxsize
    for bus, index in buses:
        bus_time = math.ceil(depart_time / bus) * bus
        if bus_time < earliest_departure:
            earliest_bus = bus
            earliest_departure = bus_time
    part1 = (earliest_departure - depart_time) * earliest_bus
    print("Part 1 answer: ", part1)

    # PART TWO
    not_found = True
    multiple = 1
    increment = buses[0][0]
    start_time = 0
    for bus, index in buses[1:]:
        start_time = get_start_time(start_time, increment, buses[0][0], bus, index)
        increment = get_increment(start_time, increment, buses[0][0], bus, index)
    print("Part 2 answer: ", start_time)

if __name__ == "__main__":
    main()

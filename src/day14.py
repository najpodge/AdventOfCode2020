import math

def get_binary_value(value):
    power = 35
    binary_value = ""
    for power in range (35, -1, -1):
        num = math.pow(2, power)
        if value >= num:
            binary_value += '1'
            value -= num
        else:
            binary_value += '0'
    return binary_value

def mask_value(mask, value):
    binary_value = get_binary_value(value)
    value = 0
    for i in range(0, len(mask)):
        if mask[i] != 'X':
            value += math.pow(2, 35 - i) * int(mask[i])
        else:
            value += math.pow(2, 35 - i) * int(binary_value[i])
    return value

def mask_locations(mask, location):
    locations = [0]
    binary_location = get_binary_value(location)
    for i in range(0, len(mask)):
        if mask[i] == '1':
            for j in range(0, len(locations)):
                locations[j] += math.pow(2, 35 - i) * int(mask[i])
        elif mask[i] == '0':
            for j in range(0, len(locations)):
                locations[j] += math.pow(2, 35 - i) * int(binary_location[i])
        else:
            temp_locations = locations[:]
            for j in range(0, len(locations)):
                locations[j] += math.pow(2, 35 - i)
            locations = locations + temp_locations
    return locations

def main():
    mem_part1 = {}
    mem_part2 = {}
    with open('input/input14.txt', 'r') as input:
        for line in input:
            line_values = line.strip().split(' = ')
            if line_values[0] == 'mask':
                mask = line_values[1]
            else:
                location = line_values[0][4:-1]
                mem_part1[location] = mask_value(mask, int(line_values[1]))
                locations = mask_locations(mask, int(location))
                for l in locations:
                    mem_part2[l] = int(line_values[1])

    part1 = sum(mem_part1.values())
    print("Part 1: ", part1)
    part2 = sum(mem_part2.values())
    print("Part 2: ", part2)

if __name__ == "__main__":
    main()

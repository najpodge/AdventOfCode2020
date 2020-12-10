def num_ways_to_arrange(jolts, seen):
    if len(jolts) == 1:
        return 1
    
    next = 1
    if jolts[next] - jolts[0] > 3:
        return 0
    
    if jolts[0] in seen:
        return seen[jolts[0]]

    total = 0
    while next < len(jolts) and jolts[next] - jolts[0] <= 3:
        total += num_ways_to_arrange(jolts[next:], seen)
        next += 1
    seen[jolts[0]] = total
    return total

def main():
    with open('input/input10.txt', 'r') as input:
        jolts = [int(line.strip()) for line in input]

    jolts.append(0)
    jolts.sort()
    jolts.append(jolts[-1] + 3)
    one_difference = 0
    three_difference = 0
  
    for i in range(0, len(jolts) - 1):
        difference = jolts[i + 1] - jolts[i]
        if difference == 1:
            one_difference += 1
        elif difference == 3:
            three_difference += 1
    
    part1 = one_difference * three_difference
    print("Part 1 answer: ", part1)

    part2 = num_ways_to_arrange(jolts, {})
    print("Part 2 answer: ", part2)

if __name__ == "__main__":
    main()
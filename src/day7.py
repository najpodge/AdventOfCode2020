import re

def contains_gold(bag, bags):
    found_gold = False
    if bags[bag] == []:
        return False
    for (quantity, sub_bag) in bags[bag]:
        if sub_bag  == 'shiny gold':
            found_gold = True
        found_gold = found_gold or contains_gold(sub_bag, bags)
    return found_gold

def num_bags_inside(bag, bags):
    num_bags = 0
    if bags[bag] == []:
        return 0
    for (quantity, sub_bag) in bags[bag]:
        num_bags += int(quantity) + int(quantity) * num_bags_inside(sub_bag, bags)
    return num_bags

def main():
    bags = {}
    #contains_gold = {}
    with open('input/input7.txt', 'r') as input:
        for line in input:
            line = line.replace('.', '').replace('bags', '').replace('bag', '')
            bag_contents = re.split(' contain ', line.strip())
            bag = bag_contents[0].strip()
            contents = [] if bag_contents[1] == 'no other' else re.split(' , ', bag_contents[1])
            pairs = []
            for pair in contents:
                pairs.append(tuple(pair.split(' ', 1)))
            bags[bag] = pairs

    part1 = 0
    for bag in bags:
        part1 += contains_gold(bag, bags)  
    part2 = num_bags_inside('shiny gold', bags)
    print("Part 1 answer: ", part1)
    print("Part 2 answer: ", part2)

if __name__ == "__main__":
    main()
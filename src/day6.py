def main():
    answers = []
    with open('input/input6.txt', 'r') as input:
        group = []
        individual = set()
        for line in input:
            if line == '\n':
                answers.append(group)
                group = []
            else:
                for letter in line.strip():
                    individual.add(letter)
                group.append(individual)
                individual = set()
        answers.append(group)

    part1 = 0
    for group in answers:
        part1 += len(set.union(*group))
    
    part2 = 0
    for group in answers:
        part2 += len(set.intersection(*group))

    print("Part 1 answer: ", part1)
    print("Part 2 answer: ", part2)

if __name__ == "__main__":
    main()
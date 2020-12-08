def execute(instructions):
    acc = 0
    index = 0
    (operation, argument, seen) = instructions[index]
    while not seen:
        instructions[index] = (operation, argument, True)
        if operation == 'acc':
            acc += argument
            index += 1
        elif operation == 'jmp':
            index += argument
        else:
            index += 1
        if index < len(instructions) and index > 0:
            (operation, argument, seen) = instructions[index]
        else:
            break
    return (acc, index)

def main():
    instructions = []
    with open('input/input8.txt', 'r') as input:
        for line in input:
            split_line = line.strip().split()
            instructions.append((split_line[0], int(split_line[1]), False))

    print("Part 1 answer: ", execute(list(instructions))[0])

    fixed_instructions = instructions[:]
    length = len(instructions)
    for index in range(0, length):
        (operation, argument, seen) = instructions[index]
        if operation == 'jmp':
            fixed_instructions[index] = ('nop', argument, seen)
            (acc, index) = execute(fixed_instructions)
            if index == length:
                break
        elif operation == 'nop':
            fixed_instructions[index] = ('jmp', argument, seen)
            (acc, index) = execute(fixed_instructions)
            if index == length:
                break
        fixed_instructions = instructions[:]

    print("Part 2 answer: ", acc)

if __name__ == "__main__":
    main()
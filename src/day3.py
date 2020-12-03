def numTrees(map, right, down):
    numTrees = 0
    x = 0
    y = 0
    width = len(map[0])
    while y < len(map):
        numTrees += 1 if map[y][x] == '#' else 0
        y += down
        x = (x + right) % width
    return numTrees

def main():
    with open('input/input3.txt', 'r') as input:
        map = [line.strip() for line in input]
    
    part1 = numTrees(map, 3, 1)
    part2 = numTrees(map, 1, 1) * part1 * numTrees(map, 5, 1) * numTrees(map, 7, 1) * numTrees(map, 1, 2)

    print("Part 1 answer: ", part1)
    print("Part 2 answer: ", part2)

if __name__ == "__main__":
    main()
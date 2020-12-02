def sum2entries(entries):
    for i in range(len(entries) - 1):
        for j in range(i + 1, len(entries)):
            if (entries[i] + entries[j] == 2020):
                return entries[i] * entries[j]

def sum3entries(entries):
    for i in range(len(entries) - 2):
        for j in range(i + 1, len(entries) - 1):
            for k in range (j + 1, len(entries)):
                if (entries[i] + entries[j] + entries[k] == 2020):
                    return entries[i] * entries[j] * entries[k]

def main():
    with open('input/input1.txt', 'r') as input:
        entries = [int(line.strip()) for line in input]

    print("Part 1 answer: ", sum2entries(entries))
    print("Part 2 answer: ", sum3entries(entries))

if __name__ == "__main__":
    main()
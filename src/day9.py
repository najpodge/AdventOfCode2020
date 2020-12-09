def validate(index, data, preamble_length):
    for x in range(index - preamble_length, index - 1):
        for y in range (index - preamble_length + 1, index):
            if not x == y and data[x] + data[y] == data[index]:
                return True
    return False

def find_set(index, data):
    for x in range(0, index):
        sum = data[x]
        additional_digits = 0
        while sum < data[index] and x + additional_digits < index:
            additional_digits += 1
            sum += data[x + additional_digits]
        if sum == data[index]:
            return min(data[x:x + additional_digits + 1]) + max(data[x:x + additional_digits + 1])

def main():
    with open('input/input9.txt', 'r') as input:
        data = [int(line.strip()) for line in input]

    preamble_length = 25
    for index in range(preamble_length, len(data)):
        if not validate(index, data, preamble_length):
            break

    print("Part 1 answer: ", data[index])
    print("Part 2 answer: ", find_set(index, data))

if __name__ == "__main__":
    main()
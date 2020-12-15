def insert_num(num, last_seen, turn):
    if not num in last_seen:
        last_seen[num] = []
    last_seen[num].append(turn)

def get_num_at_turn(num_turns, starting_nums):
    last_seen = {}
    turn = 0
    last_turn_value = 0
    for i in range(len(starting_nums)):
        turn += 1
        insert_num(starting_nums[i], last_seen, turn)
        last_turn_value = starting_nums[i]   
    while turn < num_turns:
        turn += 1
        if len(last_seen[last_turn_value]) == 1:
            insert_num(0, last_seen, turn)
            last_turn_value = 0
        else:
            this_turn_value = last_seen[last_turn_value][-1] - last_seen[last_turn_value][-2]
            insert_num(this_turn_value, last_seen, turn)
            last_turn_value = this_turn_value
    return last_turn_value

def main():
    with open('input/input15.txt', 'r') as input:
        starting_nums = [int(i) for i in input.readline().strip().split(',')]

    print("Part 1: ", get_num_at_turn(2020, starting_nums))
    print("Part 2: ", get_num_at_turn(30000000, starting_nums))

if __name__ == "__main__":
    main()

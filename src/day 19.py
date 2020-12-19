def rule_solver(unsolved_rule, rule_input, solved_rules):
    if unsolved_rule in solved_rules:
        return solved_rules

    #maybe need to check if solved here and add it to rules

    rule_letters = []
    for nums in rule_input[unsolved_rule]:
        combos = []
        letters = ''
        if nums.isalpha():
            rule_letters.append(i)

# for each of it's unsolved pieces
# loop through
# if a number is solved and it only has one value, build a string with that value
# if a numb er is solved and has more than one, build that many strings
# if it's not solved, kikck off a rule solver for it
# for each ordering, append the next orderings
    if 

    
    return solved_rules

def get_rules(rule_input):
    rule_solved = []
    solved_rules = {}
    for unsolved_rule in rule_input:
        if not unsolved_rule in solved_rules:
            solved_rules = rule_solver(unsolved_rule, rule_input, solved_rules)
        

def main():
    rule_input = {}
    messages = []
    with open('input/input19.txt', 'r') as input:
        for line in input:
            if ':' in line:
                nums = line.strip().split(' ')
                rule_num = nums[0][:-1]
                rule_input[rule_num] = []
                num_group = ''
                for num in nums[1:]:
                    if num != '|':  
                        num_group += num.strip('\"')
                    else:
                        rule_input[rule_num].append(num_group)
                        num_group = ''
                rule_input[rule_num].append(num_group)
            elif 'a' in line or 'b' in line:
                messages.append(line.strip())

    rules = get_rules(rule_input)
    print(rule_input)
    print(messages)
    #print("Part 1: ", sum(out_of_range))
    #print("Part 2: ", product)

if __name__ == "__main__":
    main()

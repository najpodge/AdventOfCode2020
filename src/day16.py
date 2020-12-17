import copy

def add_rule_values(rule, span, rules):
    beginning = int(span[0:span.index('-')])
    end = int(span[span.index('-') + 1:]) + 1
    for i in range(beginning, end):
        rules[rule].append(i)

def valid_rule_in_order(rule, rules, tickets):
    for ticket in tickets:
        if not ticket[0] in rules[rule]:
            return False
    return rule

def get_order(rules, tickets):
    for rule in rules:
        print(rule)
        order = []
        valid_rule = valid_rule_in_order(rule, rules, tickets)
        if valid_rule:
            order.append(valid_rule)
            next_rules = copy.deepcopy(rules)
            next_rules.pop(rule)
            next_tickets = [t[1:] for t in tickets]
            order = order + get_order(next_rules, next_tickets)
            if len(order) == len(rules):
                return order  
    return []

def main():
    rules = {}
    tickets = []
    with open('input/input16.txt', 'r') as input:
        section = ''
        for line in input:
            if 'or' in line:
                rule_line = line.strip().split(': ')
                rule_values = rule_line[1].split(' or ')
                rules[rule_line[0]] = []
                add_rule_values(rule_line[0], rule_values[0], rules)            
                add_rule_values(rule_line[0], rule_values[1], rules)
            elif 'nearby' in line:
                section = 'nearby'
            elif 'your' in line:
                section = 'your'
            elif section == 'nearby':
                tickets.append([int(a) for a in line.strip().split(',')])
            elif section == 'your':
                tickets.append([int(a) for a in line.strip().split(',')])
                section = ''

    out_of_range = []
    mark_for_delete = []
    for ticket in tickets:
        valid = True
        for value in ticket:
            found = False
            for rule in rules:
                if value in rules[rule]:
                    found = True
                    break
            if not found:
                out_of_range.append(value)
                valid = False
        if not valid:
            mark_for_delete.append(ticket)
    
    for ticket in mark_for_delete:
        tickets.remove(ticket)

    order = get_order(rules, tickets)
    print(len(order))
    print(len(rules))
    product = 1
    for i in range(len(order)):
        if 'departure' in order[i]:
            #print(order[i],tickets[0][i])
            product *= tickets[0][i]

    print(order)
    print("Part 1: ", sum(out_of_range))
    print("Part 2: ", product)

if __name__ == "__main__":
    main()

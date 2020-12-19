import copy

def add_rule_values(rule, span, rules):
    beginning = int(span[0:span.index('-')])
    end = int(span[span.index('-') + 1:]) + 1
    for i in range(beginning, end):
        rules[rule].append(i)

def get_valid_columns(rules, tickets):
    columns = len(tickets[0])
    num_tickets = len(tickets)
    rule_order = {} 
    for rule in rules:
        rule_order[rule] = []
        for i in range(columns):
            sum = 0
            for ticket in tickets:
                if ticket[i] in rules[rule]:
                    sum += 1
            if sum == num_tickets:
                rule_order[rule].append(i)
    return rule_order

def delete_column(rule_columns, column):
    for rule in rule_columns:
        if column in rule_columns[rule]:
            rule_columns[rule].remove(column)
    return rule_columns

def get_next_rule(rule_columns):
    for rule in rule_columns:
        if len(rule_columns[rule]) == 1:
            column = rule_columns[rule][0]
            return rule, column, delete_column(rule_columns, column)

def get_rule_order(rule_columns):
    order = {}
    while rule_columns:
        next_rule, column, rule_columns = get_next_rule(rule_columns)
        rule_columns.pop(next_rule)
        order[column] = next_rule
    return order

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
    print("Part 1: ", sum(out_of_range))

    for ticket in mark_for_delete:
        tickets.remove(ticket)
    rule_columns = get_valid_columns(rules, tickets)
    order = get_rule_order(rule_columns)
    product = 1
    for column in order:
        if 'departure' in order[column]:
            product *= tickets[0][column]
    print("Part 2: ", product)

if __name__ == "__main__":
    main()

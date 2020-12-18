def get_type(value):
    if value in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return 'int'
    elif '(' in value:
        return 'open'
    elif ')' in value:
        return 'close'
    else: 
        return 'operator'

def evaluate(expression):
    operands = []
    operator = None
    while len(expression) > 0:
        op_type = get_type(expression[0])
        if op_type == 'int':
            operands.append(int(expression[0]))
            expression = expression[1:]
        elif op_type == 'operator':
            operator = expression[0]
            expression = expression[1:]
        elif op_type == 'open':
            new_operand, expression = evaluate(expression[1:])
            operands.append(new_operand)
        elif op_type == 'close':
            return operands[0], expression[1:]
        if len(operands) >= 2:
            new_operand = operands[-1] + operands[-2] if operator == '+' else operands[-1] * operands[-2]
            operands = operands[:-2]
            operands.append(new_operand)
    return operands[0], expression

def insert_right_paren(expression):
    if get_type(expression[0]) == 'int':
        return expression[0] + ')' + expression[1:]    
    paren_count = 0
    for i in range(len(expression)):
        op_type = get_type(expression[i])        
        if get_type(expression[i]) == 'open':
            paren_count -= 1
        elif get_type(expression[i]) == 'close':
            paren_count += 1
        if paren_count == 0:
            return expression[:i + 1] + ')' + expression[i + 1:]

def insert_left_paren(expression):
    if get_type(expression[-1]) == 'int':
        return expression[:-1] + '(' + expression[-1:]
    paren_count = 0
    for i in range(len(expression) - 1, -1, -1):
        op_type = get_type(expression[i])        
        if get_type(expression[i]) == 'close':
            paren_count -= 1
        elif get_type(expression[i]) == 'open':
            paren_count += 1
        if paren_count == 0:
            return expression[:i + 1] + '(' + expression[i + 1:]

def mutate(expression):
    index = 0
    while index < len(expression):
        if expression[index] == '+':
            expression = insert_left_paren(expression[:index]) + '+' + insert_right_paren(expression[index + 1:])
            index += 1
        index += 1
    return expression

def main():
    expressions = []
    with open('input/input18.txt', 'r') as input:
        expressions = [line.strip().replace(' ', '') for line in input]

    part1 = 0
    part2 = 0
    for expression in expressions:
        part1 += evaluate(expression)[0]
        part2 += evaluate(mutate(expression))[0]

    print('Part 1: ', part1)
    print('Part 2: ', part2)

if __name__ == "__main__":
    main()

def find_next_symbol(eq, last_symbol_index):
    for x in range(last_symbol_index+1, len(eq)):
        if eq[x] in ["+", "-", "/", "*"]:
            return x

    return len(eq)

def solve(equation):
    operations = {
        "+": lambda x,y: float(x)+float(y),
        "-": lambda x,y: float(x)-float(y),
        "*": lambda x,y: float(x)*float(y),
        "/": lambda x,y: float(x)/float(y)
    }

    # calculate the result of the first two numbers
    curr_symbol_index = find_next_symbol(equation, 0)
    num1 = equation[:curr_symbol_index]
    symbol = equation[curr_symbol_index]
    num2 = equation[curr_symbol_index+1:find_next_symbol(equation, curr_symbol_index)]
    result = operations[symbol](num1.strip(), num2.strip())

    # calculate the result of the rest of the numbers
    while find_next_symbol(equation, curr_symbol_index) != len(equation):
        curr_symbol_index = find_next_symbol(equation, curr_symbol_index)
        symbol = equation[curr_symbol_index]
        num = equation[curr_symbol_index+1:find_next_symbol(equation, curr_symbol_index)]
        result = operations[symbol](result, num.strip())

    return result

def find_next_specific_symbol(eq, symbol_to_find, last_symbol_index):
    for x in range(last_symbol_index+1, len(eq)):
        if eq[x] == symbol_to_find:
            return x

    return len(eq)

def find_previous_symbol(eq, max_index):
    for x in reversed(range(0, max_index)):
        if eq[x] in ["+", "-", "/", "*"]:
            return x

    return 0

def process_operation(equation, symbol, op_func):
    next_op_index = 0

    while (next_op_index:=find_next_specific_symbol(equation, symbol, next_op_index)) != len(equation):
        prev_symbol_index = find_previous_symbol(equation, next_op_index)
        next_symbol_index = find_next_symbol(equation, next_op_index)

        if prev_symbol_index != 0:
            prev_symbol_index += 1

        num1 = equation[prev_symbol_index:next_op_index]
        num2 = equation[next_op_index+1:next_symbol_index]

        result = op_func(num1, num2)
        equation = equation[:prev_symbol_index] + str(result) + equation[next_symbol_index:]

    return equation

def solve_in_order(equation):
    result = process_operation(equation, "/", lambda x,y: float(x)/float(y))
    result = process_operation(result, "*", lambda x,y: float(x)*float(y))
    result = process_operation(result, "+", lambda x,y: float(x)+float(y))
    result = process_operation(result, "-", lambda x,y: float(x)-float(y))

    return result


equation = input("Enter equation: ")
result = solve_in_order(equation)
print(f"{equation} = {result}")

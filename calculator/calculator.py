def find_next_symbol(eq, last_symbol_index):
    for x in range(last_symbol_index+1, len(eq)):
        if eq[x] in ["+", "-", "/", "*"]:
            return x

    return len(eq)

def solve(equation):
    operations = {
        "+": lambda x,y: int(x)+int(y),
        "-": lambda x,y: int(x)-int(y),
        "*": lambda x,y: int(x)*int(y),
        "/": lambda x,y: int(x)/int(y)
    }

    curr_symbol_index = find_next_symbol(equation, 0)
    num1 = equation[:curr_symbol_index]
    symbol = equation[curr_symbol_index]
    num2 = equation[curr_symbol_index+1:find_next_symbol(equation, curr_symbol_index)]
    result = operations[symbol](num1.strip(), num2.strip())

    while find_next_symbol(equation, curr_symbol_index) != len(equation):
        curr_symbol_index = find_next_symbol(equation, curr_symbol_index)
        symbol = equation[curr_symbol_index]
        num = equation[curr_symbol_index+1:find_next_symbol(equation, curr_symbol_index)]
        result = operations[symbol](result, num.strip())

    return result


equation = input("Enter equation: ")
result = solve(equation)
print(f"{equation} = {result}")



def evaluate(eq):
    if "(" in eq:
        res = find_set_of_paren(eq)
        if res:
            new_eq = eq[res[0]+1:res[1]]
            print(f"new_eq: {new_eq}")
            eval_result = evaluate(new_eq)
            return eval_result
    else:
        return eq


def find_set_of_paren(eq):
    paren_count = 0
    first_paren = -1
    for x in range(len(eq)):
        # this if statement finds the location of 
        # the first opening parenthesis in eq
        if eq[x] == "(" and paren_count == 0:
           first_paren = x
           paren_count += 1 # == paren_count = paren_count + 1
        # this if statement determines if we are looking 
        # at the corresponding closing paren for the opening
        # paren we found earlier and saved in first_paren
        elif eq[x] == ")" and paren_count - 1 == 0:
            return (first_paren, x)
        elif eq[x] == "(":
            paren_count += 1
        elif eq[x] == ")":
            paren_count -= 1 # == paren_count = paren_count - 1

    # if we get here, that means no matching set of paren were found
    return None


eq = input("Enter equation: ")

print(f"end result: {evaluate(eq)}")

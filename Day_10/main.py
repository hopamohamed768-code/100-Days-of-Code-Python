import art

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": sub,
              "*": mul,
              "/": div}

def calculator():
    print(art.logo)
    f_num = float(input("What is the first number: "))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        s_num = float(input("What is the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(f_num, s_num)
        print(f"{f_num} {operation_symbol} {s_num} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer},"
                       " or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            f_num = answer
        else:
            should_continue = False
            calculator()
calculator()




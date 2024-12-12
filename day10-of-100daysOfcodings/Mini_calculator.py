def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    return n1 - n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}


def calculator():


    num1 = float(input("What is your number: "))


    calculate_on = True

    while calculate_on:

        for symbols in operations:
            print(symbols)


        operation_symbols = input("select symbols for calculations: ")
        num2 = float(input("What is your next number: "))
        calculate_result = operations[operation_symbols](n1=num1, n2=num2)
        n1_output = '{0:g}'.format(num1)
        n2_output = '{0:g}'.format(num2)
        output = '{0:g}'.format(calculate_result)
        print(f"{n1_output}{operation_symbols}{n2_output} = {output}")

        choose = input("Do you want to continue previous calculation yes - y or want to frest calculation no - n or if want to stop use s: ").lower()[0]

        if choose == 'y':
           num1 = calculate_result
        elif choose == 's':
            calculate_on = False
        else:
            calculate_on = False
            calculator()

  
calculator()



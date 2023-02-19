from src.algorithms.postfix import to_postfix
from src.algorithms.count import count
from src.variables import Variables

variables = Variables()

while True:

    try:
        calculation = input('\ncalculation: \n\n')
    except:
        print(f"\nerror with ^, make sure to press twice and then space")
        continue

    if calculation == 'quit':
        print('\nBye!')
        break

    if '=' in calculation:
        vars = calculation.split("=")
        expression = variables.fetch_variables(vars[-1])
        value = count(to_postfix(expression))
        try:
            int(value)
        except ValueError:
            print(value)
            continue

        if value < 0:
            value = f"({str(value)})"

        variables.add_variable(vars[0], str(value))
        print(f"{vars[0]} = {value}\n")
        print('Variable added!')
        continue

    check_variables = variables.fetch_variables(calculation)

    try:
        value = count(to_postfix(check_variables))
        print(f"\n= {value}\n")
    except IndexError:
        print('Incorrect input')

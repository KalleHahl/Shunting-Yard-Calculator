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
        break

    if '=' in calculation:
        vars = calculation.split("=")
        value = count(to_postfix(vars[-1]))
        variables.add_variable(vars[0], str(value)) 
        print(f"= {value}\n")
        print('variable added!')
        continue

    check_variables = variables.fetch_variables(calculation)
    value = count(to_postfix(check_variables))
    print(f"\n= {value}\n")

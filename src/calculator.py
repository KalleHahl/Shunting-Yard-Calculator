from src.algorithms.postfix import ShuntingYard
from src.algorithms.count import Count
from src.variables import Variables
from src.errors.error import IncorrectInput, CommaError, MismatchedParentheses, EmptyFunction, SquareRootOfNegative, DivisionByZero



class Calculator:

    def __init__(self):
        self.variables = Variables()
        self.input = None
        self.calculation = None

    def start(self):

        while True:

            self.input = input('\ncalculation: \n\n')
            
            if self.input == 'quit':
                print('\nBye!')
                break

            elif '=' in self.input:
                self.add_variables()
                continue
            elif self.input == '':
                print('Write expression')
                continue

            check_variables = self.variables.fetch_variables(self.input)
            self.shunt(check_variables)
            
            if self.calculation == None:
                continue
            value = self.output()

            if value != None:
                print(f"\n= {value}\n")
            self.calculation = None



    def add_variables(self):
        vars = self.input.split("=")
        self.shunt(self.variables.fetch_variables(vars[-1]))
        if self.calculation == None:
            return
        value = self.output()
        if value == None:
            self.calculation = None
            return
        if value < 0:
            value = f"({str(value)})"

        self.variables.add_variable(vars[0], str(value))
        print(f"{vars[0]} = {value}\n")
        print('Variable added!')
        self.calculation = None
    
    def output(self):
        try:
            return Count(self.calculation).count()
        except IncorrectInput:
            print('\nIncorrect input')
        except SquareRootOfNegative:
            print("\nCan't solve squareroot of negative")
        except DivisionByZero:
            print("\nCan't divide by zero")
        except IndexError:
            print('\nIncorrect input')
    
    def shunt(self, x):
        try:
            self.calculation = ShuntingYard(x).to_postfix()
        except IncorrectInput:
            print('\nIncorrect input')
        except CommaError:
            print('\nIncorrect use of a comma')
        except MismatchedParentheses:
            print('\nMismatched parentheses')
        except EmptyFunction:
            print('\nUsed an empty function')
        
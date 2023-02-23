from src.algorithms.postfix import ShuntingYard
from src.algorithms.count import Count
from src.algorithms.variables import Variables
from src.errors.error import (IncorrectInput, CommaError, MismatchedParentheses,
                              EmptyFunction, SquareRootOfNegative, DivisionByZero)


class Calculator:

    def __init__(self):
        print("Type 'help' for instructions, 'quit' to exit program")
        self.variables = Variables()
        self.input = None
        self.calculation = None

    def start(self):
        """
        Main loop, takes input and calls a function based on the input.
        Breaks when input is 'quit'.
        """
        while True:

            self.input = input('\ncalculation: \n\n')

            if self.input == 'quit':
                print('\nBye!')
                break

            if self.input == 'help':
                self.instructions()
                continue

            if '=' in self.input:
                self.add_variables()
                continue

            if self.input == '':
                print('Type an expression')
                continue

            # checks if variables are used, if found, replaces them with correct values
            check_variables = self.variables.fetch_variables(self.input)

            self.shunt(check_variables)

            if self.calculation is None:
                continue
            value = self.output()

            if value is not None:
                print(f"\n= {value}\n")
            self.calculation = None

    def add_variables(self):
        """
        Function that first splits the input from =, then counts
        correct value by calling the shunt and output functions
        and saves variable to variables class
        """
        parts = self.input.split("=")
        self.shunt(self.variables.fetch_variables(parts[-1]))
        if self.calculation is None:
            return
        value = self.output()
        if value is None:
            self.calculation = None
            return
        if value < 0:
            value = f"({str(value)})"
        if parts[0].isdigit() or parts[0].islower() or len(parts[0]) != 1:
            print('Use single capital letters for variables!')
            return
        self.variables.add_variable(parts[0], str(value))
        print(f"{parts[0]} = {value}\n")
        print('Variable added!')
        self.calculation = None

    def output(self):
        """
        Returns value of the postfix expression,
        deals with raised errors
        """
        try:
            return Count(self.calculation).count()
        except IncorrectInput:
            print('\nIncorrect input')
            return None
        except SquareRootOfNegative:
            print("\nCan't solve squareroot of negative")
            return None
        except DivisionByZero:
            print("\nCan't divide by zero")
            return None
        except IndexError:
            print('\nIncorrect input')
            return None
        except OverflowError:
            print('\nThe value of the given calculation is too big')
            return None

    def shunt(self, expression):
        """
        Transfers the expressions into a postfix form by calling to_postfix from the Shunting
        yard class, deals with raised errors
        """
        try:
            self.calculation = ShuntingYard(expression).to_postfix()
        except IncorrectInput:
            print('\nIncorrect input')
        except CommaError:
            print('\nIncorrect use of a comma')
        except MismatchedParentheses:
            print('\nMismatched parentheses')
        except EmptyFunction:
            print('\nUsed an empty function')

    def instructions(self):  # pragma: no cover
        """
        Prints instructions, in a very unclean way
        """
        longest = ' Add variables by typing X=5+5, use single capital letters '
        print2 = 'Available operators: (+, -, /, *, ^)'
        print3 = 'Available functions: (sin, cos, tan, sqrt, min, max)'
        print4 = 'Sin, cos and tan count radians'
        print5 = 'When using min or max, divide values with a comma'
        print("╔"+len(longest)*'=' + "╗")
        print('║'+len(longest)*' '+'║')
        print('║'+longest+'║')
        print('║'+len(longest)*' '+'║')
        print('║'+(len(longest)-len(print2))//2*' ' +
              print2+(len(longest)-len(print2))//2*' '+' ║')
        print('║'+len(longest)*' '+'║')
        print('║'+(len(longest)-len(print5))//2*' ' +
              print5+(len(longest)-len(print5))//2*' '+'║')
        print('║'+len(longest)*' '+'║')
        print('║'+(len(longest)-len(print4))//2*' ' +
              print4+(len(longest)-len(print4))//2*' '+' ║')
        print('║'+len(longest)*' '+'║')
        print('║'+(len(longest)-len(print3))//2*' ' +
              print3+(len(longest)-len(print3))//2*' '+' ║')
        print('║'+len(longest)*' '+'║')
        print("╚"+len(longest)*'=' + "╝")

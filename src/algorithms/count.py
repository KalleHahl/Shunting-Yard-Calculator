from collections import deque
import operator
import math
from src.errors.error import SquareRootOfNegative, IncorrectInput, DivisionByZero


class Count:
    """
    Class for iterating the given list and doing operations based on the popped character.
    End result is the correct value for the given expression.
    """

    def __init__(self, expression):
        self.char = None
        self.expression = expression
        # initialize the main stack
        self.the_stack = deque()
        # all available operatorts, sin,cos,tan count radians
        self.operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'sqrt': math.sqrt,
            'min': min,
            'max': max
        }

    def count(self):
        """
        Main function, loops the deque and pops one index at a time.
        If popped character is an operation, one of two functions is called,
        else character is appended to the_stack
        """
        while len(self.expression) != 0:

            self.char = self.expression.popleft()

            if self.char in self.operators:

                if self.char in ("sin", "cos", "tan", "sqrt"):
                    self.functions()
                else:
                    self.operations()
                continue

            try:
                self.the_stack.append(float(self.char))
            except Exception as exc:
                raise IncorrectInput from exc

        return self.the_stack.pop()

    def functions(self):
        """
        If the given character is a unary function, correct operation is first
        fetched from the dictionary. Then the digit ontop of the_stack is popped
        and operated. Given result is then appended back ontop of the_stack
        """
        operation = self.operators.get(self.char)
        number = self.the_stack.pop()
        try:
            value = operation(number)
        except Exception as exc:
            raise SquareRootOfNegative from exc

        self.the_stack.append(value)

    def operations(self):
        """
        If the given character is an operation like */^+-max,min, then operation is fetched
        from the dictionary, the first digit popped from the_stack is for the right side
        and the second for the left. After operating these digits the result is then appended
        back ontop of the_stack
        """
        operation = self.operators.get(self.char)
        right = self.the_stack.pop()
        left = self.the_stack.pop()

        if right == 0 and self.char == '/':
            raise DivisionByZero

        value = operation(left, right)

        self.the_stack.append(value)

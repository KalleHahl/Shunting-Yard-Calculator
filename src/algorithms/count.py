from collections import deque
import operator
import math
from src.errors.error import SquareRootOfNegative, IncorrectInput, DivisionByZero
class Count:

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

        while len(self.expression) != 0:

            self.char = self.expression.popleft()

            # check if popped character is an operator
            if self.char in self.operators:

                # since these operations only take one number,
                # pop the number from main stack--> count the value
                # --> append to main stack --> continue
                if self.char in ("sin", "cos", "tan", "sqrt"):
                    self.functions()
                else:
                    self.operations()
                continue

            # if not an operator, append operand to main stack
            try:
                self.the_stack.append(float(self.char))
            except Exception as exc:
                raise IncorrectInput from exc

        return self.the_stack.pop()

    def functions(self):
        operation = self.operators.get(self.char)
        number = self.the_stack.pop()
        try:
            value = operation(number)
        except Exception as exc:
            raise SquareRootOfNegative from exc

        self.the_stack.append(value)

    def operations(self):
        # pop operand from main stack for left and right side of calculation
        operation = self.operators.get(self.char)
        right = self.the_stack.pop()
        left = self.the_stack.pop()
        # check division by zero
        if right == 0 and operation == self.operators['/']:
            raise DivisionByZero

        # count value --> append to the main stack
        value = operation(left, right)

        self.the_stack.append(value)

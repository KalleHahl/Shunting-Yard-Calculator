from collections import deque
import operator
import math
from src.algorithms.postfix import to_postfix


def count(postfix):

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan
    }

    

    the_stack = deque()

    while len(postfix) != 0:
        try:
            char = postfix.popleft()
        except:
            return postfix

        if char in operators:

            operation = operators.get(char)

            if char in 'sincostan':
                number = the_stack.pop()
                value = operation(number)
                the_stack.append(value)
                continue

            right = the_stack.pop()
            left = the_stack.pop()
            if right == 0 and operation == operators['/']:
                return ("Can't divide by zero")

            value = operation(left, right)

            the_stack.append(value)
            continue

        the_stack.append(float(char))

    return the_stack.pop()

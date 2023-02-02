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
        char = postfix.popleft()

        if char in operators:

            operation = operators.get(char)

            if char in 'sincostan':
                number = the_stack.pop()
                value = operation(number)
                the_stack.append(value)
                continue

            right = the_stack.pop()
            left = the_stack.pop()
            value = operation(left, right)

            the_stack.append(value)
            continue

        the_stack.append(float(char))
            
    return the_stack.pop()

print(count(to_postfix('2*cos(4)')))

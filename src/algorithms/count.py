from collections import deque
import operator
from src.algorithms.postfix import to_postfix


def count(postfix):

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow
    }

    the_stack = deque()

    while len(postfix) != 0:
        char = postfix.popleft()

        if char in operators:
            operation = operators.get(char)

            right = the_stack.pop()
            left = the_stack.pop()
            value = operation(left, right)

            the_stack.append(value)
            continue

        the_stack.append(float(char))
            
    return the_stack.pop()


print(count(to_postfix('1.2+4')))


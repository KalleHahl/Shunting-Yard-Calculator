from collections import deque
import operator
import math


def count(postfix):

    # all available operatorts, sin,cos,tan count radians
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'sqrt': math.sqrt
    }

    # initialize the main stack
    the_stack = deque()

    while len(postfix) != 0:

        # try popping,
        # if not possible then the value returned by to_postfix
        # is an error message --> return error message
        try:
            char = postfix.popleft()
        except AttributeError:
            return postfix

        # check if popped character is an operator
        if char in operators:

            # fetch the correct operation from operations
            operation = operators.get(char)

            # since these operations only take one number,
            # pop the number from main stack--> count the value
            # --> append to main stack --> continue
            if char in 'sincostansqrt':
                number = the_stack.pop()
                value = operation(number)
                the_stack.append(value)
                continue

            # pop operand from main stack for left and right side of calculation
            right = the_stack.pop()
            left = the_stack.pop()
            # check division by zero
            if right == 0 and operation == operators['/']:
                return "Can't divide by zero"

            # count value --> append to the main stack
            value = operation(left, right)

            the_stack.append(value)
            continue

        # if not an operator, append operand to main stack
        try:
            the_stack.append(int(char))
        except ValueError:
            the_stack.append(float(char))

    return the_stack.pop()

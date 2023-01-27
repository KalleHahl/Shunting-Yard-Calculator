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

        if char.isdigit():
            the_stack.append(int(char))
        
        elif char in operators:
            operation = operators.get(char)

            right = the_stack.pop()
            left = the_stack.pop()
            value = operation(left, right)

            the_stack.append(value)

    return the_stack.pop()

print(to_postfix('(1+2)*(10/2)^(2+1)'))
print(count(to_postfix('(1+2)*(10/2)^(2+1)')))


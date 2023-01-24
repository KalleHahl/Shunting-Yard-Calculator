from collections import deque
import operator

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



print(count(deque(['3', '4', '5', '*', '+'])))
print(count(deque(['5', '1', '2', '+', '4', '*', '3', '-', '+'])))
print(count(deque(['1', '2', '+', '3', '4', '/', '^', '5', '6', '+', '*'])))
print(count(deque(['3', '5', '2', '^', '+'])))
print(count(deque(['5', '5', '^'])))



from collections import deque


def to_postfix(string):
    operators = '+-^*/()'
    equation = deque(string)
    operator_stack = deque()
    the_stack = deque()

    num = ''

    while len(equation) != 0:

        char = equation.popleft()
        
        if char.isdigit():
            num += char

        elif char in operators:
            if len(num) != 0:
                the_stack.append(num)
                num = ''

            if char in '+-':
                if len(operator_stack) == 0:
                    operator_stack.append(char)

                elif operator_stack[-1] in '*/^':
                    operator = operator_stack.pop()
                    the_stack.append(operator)
                    operator_stack.append(char)
                else:
                    operator_stack.append(char)
            
            elif char in '*/':
                if len(operator_stack) == 0:
                    operator_stack.append(char)
                    continue
                elif operator_stack[-1] in '+-':
                    operator_stack.append(char)
                    continue
                elif operator_stack[-1] == '(':
                    operator_stack.append(char)
                    continue
                operator = operator_stack.pop()
                the_stack.append(operator)
                operator_stack.append(char)
                
            elif char == '(':
                operator_stack.append(char)
            
            elif char == ')':
                while True:
                    operator = operator_stack.pop()
                    if operator == '(':
                        break
                    else:
                        the_stack.append(operator)

            elif char == '^':
                if operator_stack[-1] == char:
                    operator = operator_stack.pop()
                    the_stack.append(operator)
                operator_stack.append(char)
        
        if len(equation) == 0:
            if len(num) != 0:
                the_stack.append(num)
            while len(operator_stack) != 0:
                operator = operator_stack.pop()
                the_stack.append(operator)
        
    return the_stack






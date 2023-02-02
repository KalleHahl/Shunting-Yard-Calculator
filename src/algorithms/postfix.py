from collections import deque
from string import ascii_letters

def to_postfix(string):
    operators = '+-^*/()'
    other_operators = 'sincostan'
    equation = deque(string)
    operator_stack = deque()
    the_stack = deque()

    num = ''

    while True:

        # if the input string has been iterated, check if there is anything in num and then add all operators from the operator stack to the_stack
        if len(equation) == 0:
            if len(num) != 0:
                print('juu')
                the_stack.append(num)
            while len(operator_stack) != 0:
                print('juu')
                operator = operator_stack.pop()
                the_stack.append(operator)
            break

        char = equation.popleft()

        if char.isdigit() or char=='.':
            num += char
        
        elif char in ascii_letters:
            if num.isdigit():
                the_stack.append(num)
                num = char
            else:
                num += char
                
            

        elif char in operators:
            if len(num) != 0:
                if num in other_operators:
                    operator_stack.append(num)
                    num = ''
                else:
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
                if operator_stack[-1] in '+-':
                    operator_stack.append(char)
                    continue
                if operator_stack[-1] == '(':
                    operator_stack.append(char)
                    continue
                operator = operator_stack.pop()
                the_stack.append(operator)
                operator_stack.append(char)

            elif char == '(':
                operator_stack.append(char)

            elif char == ')':
                if operator_stack[-1] == '(':
                    operator_stack.pop()
                    operator = operator_stack.pop()
                    the_stack.append(operator)
                    continue

                while True:
                    operator = operator_stack.pop()
                    if operator == '(':
                        break
                    the_stack.append(operator)

            elif char == '^':
                if operator_stack[-1] == char:
                    operator = operator_stack.pop()
                    the_stack.append(operator)
                operator_stack.append(char)
        
        
    

        

    return the_stack
print(to_postfix('2*cos(4)'))
from collections import deque


def to_postfix(string):
    operators = '+-^*/()'
    other_operators = 'sincostan'
    calculation = deque(string)
    operator_stack = deque()
    the_stack = deque()

    num = ''

    previous = ''
    size = len(string)

    if calculation[-1] in '+-*^/sincostan':
        return 'Incorrect input'

    print('')
    print(f"{''.join(calculation):{size}} --> ")


    while True:

        # if the input string has been iterated, check if there is anything in num and then add all operators from the operator stack to the_stack
        if len(calculation) == 0:
            if len(num) != 0:
                the_stack.append(num)
            while len(operator_stack) != 0:
                operator = operator_stack.pop()
                if operator == '(':
                    return 'No closing parentheses'
                the_stack.append(operator)
            break

        char = calculation.popleft()

        if char.isdigit() or char == '.' or char in other_operators:
            num += char

        elif char in operators:

            if char in '/+-*^' and previous in '/+-*^' and char not in '()':
                return 'Incorrect input'

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
                    try:
                        operator = operator_stack.pop()
                    except:
                        return 'No opening parentheses'

                    if operator == '(':
                        break
                    the_stack.append(operator)

            elif char == '^':
                if len(operator_stack) == 0:
                    operator_stack.append(char)
                    continue
                
                if operator_stack[-1] == char:
                    operator = operator_stack.pop()
                    the_stack.append(operator)
                operator_stack.append(char)

        previous = char

        print(f"{''.join(calculation):{size}} -->  {' '.join(the_stack):10}")
    print(f"{''.join(calculation):{size}} -->  {' '.join(the_stack):10}")
    
    return the_stack

#print(to_postfix('2^2'))
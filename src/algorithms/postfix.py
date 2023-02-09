from collections import deque


def to_postfix(string):

    operators = '+-^*/(),'
    other_operators = 'sincostan'

    # deque the string, to have popleft function
    calculation = deque(string)

    # stack to store operators
    operator_stack = deque()
    # stack to store the postfix form
    the_stack = deque()

    # variable for numbers or sin, cos tan
    num = ''

    # variable to keep track of previous operator
    previous = ''
    size = len(string)

    # if calculation ends in an operator, return incorrect input
    if calculation[-1] in '+-*^/sincostan':
        return 'Incorrect input'

    if calculation[0] == '-':
        calculation.appendleft('0')

    print('')
    print(f"{''.join(calculation):{size}} --> ")

    while calculation:

        # take the leftmost character in the calculation
        char = calculation.popleft()

        # adds to the num variable if character is a number, a float point, or is included in the other_operators string
        if char.isdigit() or char == '.' or char in other_operators:
            num += char

        elif char in operators:

            # uses the previous variable to see if the calculation incorrectly has 2 or more operators next to eachother
            if char in '/+-*^' and previous in '/+-*^' and char not in '()':
                return 'Incorrect input'

            # this prevents the algo from adding an empty space to the_stack, if num is sin, cos or tan, it gets added to operator_stack. If it's a number, it's added to the_stack
            if len(num) != 0:
                if num in other_operators:
                    operator_stack.append(num)
                    num = ''
                else:
                    the_stack.append(num)
                    num = ''

            # +- have to lowest precedence, so the operator stack gets cleared until there is no higher precedence operators in it
            if char in '+-':
                while operator_stack and operator_stack[-1] in '*/^':
                    operator = operator_stack.pop()
                    the_stack.append(operator)

                # chained substractions have to be added differentry since 555-- doesn't give -5 when counted with the second algo, instead it gives 5
                # This solves the problem by adding chained substractions like 55-5- into the_stack
                if operator_stack and operator_stack[-1] == '-':
                    the_stack.append(operator_stack.pop())
                operator_stack.append(char)

            # */ have the second lowest/highest precedence, so the operator stack gets cleared until there are no higher precedence operators
            elif char in '*/':

                while operator_stack and operator_stack[-1] == '^':
                    operator = operator_stack.pop()
                    the_stack.append(operator)

                operator_stack.append(char)

            # highest precedence, immediately gets appended to the operatorstack
            elif char == '(':
                operator_stack.append(char)

            # once encountered, 2 options
            elif char == ')':

                # if the operator on top of the operatorstack is an opening bracket, it means an operator from otheroperators variable has been used
                # pop the parentheses from the stack, then pop again and you have either sin,cos or tan that you then append to the_stack
                if operator_stack[-1] == '(':
                    operator_stack.pop()
                    operator = operator_stack.pop()
                    the_stack.append(operator)
                    continue

                # if the if-statement is not true, loop the operatorstack, pop and append to the_stack, until opening parentheses is found
                # if there is no opening parentheses, return error
                while True:
                    try:
                        operator = operator_stack.pop()
                    except:
                        return 'No opening parentheses'

                    if operator == '(':
                        break
                    the_stack.append(operator)

            # highest precedence, append on top of operator stack
            elif char == '^':
                operator_stack.append(char)

        print(f"{''.join(calculation):{size}} -->  {' '.join(the_stack):10}")

        # change previous to char for next loop
        previous = char

    # checks if num variable has something in it, append to the_stack if it does
    if len(num) != 0:
        the_stack.append(num)

    # loop the remaining operators from the operatorstack and append them to the_stack, return error if an opening parentheses is found in this stage
    while len(operator_stack) != 0:
        operator = operator_stack.pop()
        if operator == '(':
            return 'No closing parentheses'
        the_stack.append(operator)
        print(f"{''.join(calculation):{size}} -->  {' '.join(the_stack):10}")

    return the_stack

# print(to_postfix('2^2^2^2*5*5*5'))

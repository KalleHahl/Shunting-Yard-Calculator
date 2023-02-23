from collections import deque
from src.errors.error import MismatchedParentheses, EmptyFunction, CommaError, IncorrectInput


class ShuntingYard:

    def __init__(self, string):
        self.other_operators = 'sincostansqrtminmaxabs'
        self.calculation = deque(string)
        self.operator_stack = deque()
        self.the_stack = deque()
        self.current = ''
        self.num = ''
        self.previous = ''
        self.next = ''
        self.size = len(string)
        self.function_dictionary = {
            '+': self.precedence_1,
            '-': self.precedence_1,
            '*': self.precedence_2,
            '/': self.precedence_2,
            '(': self.opening_parentheses,
            ')': self.closing_parentheses,
            ',': self.comma,
            '^': self.pow,
        }

    def to_postfix(self):
        """
        Main function for iterating the expression and transforming it into
        its postfix notation, returns a deque.
        """
        self.initial_check()
        print('')
        self.visualize()

        while self.calculation:
            self.current = self.calculation.popleft()

            if self.calculation:
                self.next = self.calculation[0]

            if self.current.isdigit() or self.current == '.' \
                    or self.current in self.other_operators:

                self.num += self.current
                self.previous = self.current
                continue

            if self.current in '/+-*^' and self.previous in '/+-*^':
                raise IncorrectInput

            self.previous = self.current

            self.clear_num()

            try:
                self.function_dictionary[self.current]()
            except KeyError:
                continue

            self.visualize()

        self.end_loop()

        return self.the_stack

    def initial_check(self):
        """
        Checks if the input starts with a negative or ends in an operator
        """
        if not self.calculation[-1].isdigit() and self.calculation[-1] not in '()':
            raise IncorrectInput

        if self.calculation[0] == '-':
            self.num = self.calculation.popleft()

    def precedence_1(self):
        """
        Precedence 1 includes + and -, loops the operator stack, pops and
        appends operators to the_stack until no higher precedence operators
        are found.
        """
        while self.operator_stack and self.operator_stack[-1] in '*/^':
            operator = self.operator_stack.pop()
            self.the_stack.append(operator)
        if self.operator_stack and self.operator_stack[-1] == '-':
            self.the_stack.append(self.operator_stack.pop())
        self.operator_stack.append(self.current)

    def precedence_2(self):
        """
        Includes */, loops operator stack and appends operators to the_stack
        until no more higher precedence operators are found.
        """
        while self.operator_stack and self.operator_stack[-1] == '^':
            operator = self.operator_stack.pop()
            self.the_stack.append(operator)

        self.operator_stack.append(self.current)

    def opening_parentheses(self):
        """
        Immediately check is next char is a negative mark and adds it to the num
        variable. Then checks if the next char is a closing parentheses and raises
        an error if it is. Otherwise just appends the opening parentheses to
        the operator stack
        """
        if self.next == '-':
            self.num = self.calculation.popleft()
        elif self.next == ')':
            raise EmptyFunction
        self.operator_stack.append(self.current)

    def closing_parentheses(self):
        """
        Loops the operatorstack, pops and adds the operator from operator_stack to
        the_stack until closing parentheses is found. If not found then an error is
        raised. If ( is found, if the operator on top of the operator_stack is
        a function, it is also popped onto the_stack
        """
        while True:
            try:
                operator = self.operator_stack.pop()
            except IndexError as exc:
                raise MismatchedParentheses from exc

            if operator == '(':

                if self.operator_stack and self.operator_stack[-1] in self.other_operators:
                    self.the_stack.append(self.operator_stack.pop())
                break

            self.the_stack.append(operator)

    def comma(self):
        """
        Comma acts much like the closing parentheses, loop the operator stack and
        append to the_stack until opening parentheses is found
        """
        try:
            while self.operator_stack[-1] != '(':
                self.the_stack.append(self.operator_stack.pop())
        except IndexError as exc:
            raise CommaError from exc

    def pow(self):
        """
        Small function for operating ^
        """
        self.operator_stack.append(self.current)

    def end_loop(self):
        """
        After the expression has been iterated, append the num variable onto the_stack
        and iterate the operator stack and append rest of the operators
        """
        if len(self.num) != 0:
            self.the_stack.append(self.num)

        while len(self.operator_stack) != 0:
            operator = self.operator_stack.pop()
            if operator == '(':
                raise MismatchedParentheses
            self.the_stack.append(operator)
            self.visualize()

    def clear_num(self):
        """
        This function appends and clears the num variable after
        it is found that the current char in the main loop
        is not a digit, floating point or a string
        """
        if len(self.num) != 0:
            if self.num in self.other_operators:
                self.operator_stack.append(self.num)
                self.num = ''
            else:
                self.the_stack.append(self.num)
                self.num = ''

    def visualize(self):
        print(
            f"{''.join(self.calculation):{self.size}} -->  {' '.join(self.the_stack):10}")

import unittest
from src.algorithms.postfix import ShuntingYard
from src.errors.error import EmptyFunction, CommaError, MismatchedParentheses, IncorrectInput
from collections import deque


class TestTo_postfix(unittest.TestCase):

    # tests that the function appends correctly to the_stack by skipping spaces in input
    def test_skip_spaces(self):
        test = ShuntingYard('4 + 2 + 4 + 5')

        result = test.to_postfix()

        self.assertEqual(result, deque(['4', '2', '4', '5', '+', '+', '+']))

    # test for correct order of operators and operands in simple addition, if this works theres no reason to test subtraction since the are valued as equals in the algorithm
    def test_RPN__addition(self):

        test = ShuntingYard('1+2+3+4')

        result = test.to_postfix()

        self.assertEqual(result, deque(['1', '2', '3', '4', '+', '+', '+']))

    # test for correct order when multiplication and division is included
    def test_RPN_division_and_multiplication(self):

        test = ShuntingYard('2+5*10-4/2')
        result = test.to_postfix()
        self.assertEqual(result, deque(
            ['2', '5', '10', '*', '4', '2', '/', '-', '+']))

    # test for correct order when equation has power of
    def test_RPN_power_of(self):

        test = ShuntingYard('2+4*10+2^2^2+4/2')

        result = test.to_postfix()
        self.assertEqual(result, deque(
            ['2', '4', '10', '*', '2', '2', '2', '^', '^', '4', '2', '/', '+', '+', '+']))

    # test for correct order when equation has parentheses
    def test_RPN_parentheses(self):
        test = ShuntingYard('(1+2)*(10/2)^(2+1)')

        result = test.to_postfix()

        self.assertEqual(result, deque(
            ['1', '2', '+', '10', '2', '/', '2', '1', '+', '^', '*']))

    # test for correct order in ewuation with only division and multiplication
    def test_RPN_div_mul(self):

        test = ShuntingYard('5/5*5*5')
        result = test.to_postfix()
        self.assertEqual(result, deque(
            ['5', '5', '5', '5', '*', '*', '/']
        ))

    # test correct postfix for equation with float
    def test_RPN_float(self):

        test = ShuntingYard('1.2+4')
        result = test.to_postfix()
        self.assertEqual(result, deque(
            ['1.2', '4', '+']
        ))

    # function gives error if there is no opening parentheses
    def test_no_opening_parentheses(self):

        test = ShuntingYard('5+5+5*4)+4+5+5')
        with self.assertRaises(MismatchedParentheses):
            test.to_postfix()

    # function gives error if there is no closing parentheses

    def test_no_closing_parentheses(self):

        test = ShuntingYard('5+5+5+(+10/2')
        with self.assertRaises(MismatchedParentheses):
            test.to_postfix()

    def test_cos(self):

        test = ShuntingYard('5+5*10+cos(4)')
        result = test.to_postfix()
        self.assertEqual(result, deque(
            ['5', '5', '10', '*', '4', 'cos', '+', '+']))

    def test_sin(self):

        test = ShuntingYard('4+5+sin(4)-10*2')
        result = test.to_postfix()
        self.assertEqual(result, deque(
            ['4', '5', '4', 'sin', '10', '2', '*', '-', '+', '+']))

    def test_tan(self):

        test = ShuntingYard('9+9*tan(4)-5')
        result = test.to_postfix()
        self.assertEqual(result, deque(
            ['9', '9', '4', 'tan', '*', '5', '-', '+']))

    def test_another_incorrect_input(self):

        test = ShuntingYard('5++5')
        with self.assertRaises(IncorrectInput):
            test.to_postfix()

    # test correct order for calculation with negative number in beginning

    def test_negative_number_in_beginning(self):

        test = ShuntingYard('-5-5')
        result = test.to_postfix()
        self.assertEqual(result, deque(['-5', '5', '-']))

    # test for correct order for chained pows, since power of is righ associated, meaning it is counted from the right, the pow symbols need to all be at the end of the chain
    def test_correct_order_for_many_pow(self):

        test = ShuntingYard('2^2^2^2')
        result = test.to_postfix()

        self.assertEqual(result, deque(['2', '2', '2', '2', '^', '^', '^']))

    # test correct order for squareroot with multiple variables

    def test_correct_order_for_sqrt_multiple(self):

        test = ShuntingYard('5+5*sqrt(4)^2')
        result = test.to_postfix()

        self.assertEqual(result, deque(
            ['5', '5', '4', 'sqrt', '2', '^', '*', '+']))

    # test correct order for expression where negative number is in the middle
    def test_correct_order_with_negative(self):

        test = ShuntingYard('2+5*(-5)+2')
        result = test.to_postfix()

        self.assertEqual(result, deque(
            ['2', '5', '-5', '*', '2', '+', '+']
        ))

    # test empty unary function
    def test_empty_unary(self):

        test = ShuntingYard('5+cos()+4')

        with self.assertRaises(EmptyFunction):
            test.to_postfix()

    def test_min(self):

        test = ShuntingYard('min(16,20)')
        result = test.to_postfix()

        self.assertEqual(result, deque(['16', '20', 'min']))

    def test_max(self):

        test = ShuntingYard('max(1,12)')
        result = test.to_postfix()

        self.assertEqual(result, deque(['1', '12', 'max']))

    def test_incorrect_comma(self):

        test = ShuntingYard('5+5*2,2+3')

        with self.assertRaises(CommaError):
            test.to_postfix()

    def test_abs(self):

        test = ShuntingYard('abs(-15)')
        result = test.to_postfix()
        self.assertEqual(result, deque(['-15', 'abs']))

    def test_false_floating_point(self):

        test = ShuntingYard('5+.5')
        with self.assertRaises(IncorrectInput):
            test.to_postfix()

    def test_log(self):
        test = ShuntingYard('log(1000,10)')
        result = test.to_postfix()
        self.assertEqual(result, deque(['1000', '10', 'log']))

    def test_log_long(self):
        test = ShuntingYard('log(5^2*40,(2+3)*2)')
        result = test.to_postfix()
        self.assertEqual(result, deque(
            ['5', '2', '^', '40', '*', '2', '3', '+', '2', '*', 'log']))

    def test_incorrect_comma_again(self):
        test = ShuntingYard('log(,4,4)')
        with self.assertRaises(CommaError):
            test.to_postfix()

    def test_eulers(self):
        test = ShuntingYard('10+e')
        result = test.to_postfix()
        self.assertEqual(result, deque(['10', 'e', '+']))

    def test_pi(self):
        test = ShuntingYard('pi+15')
        result = test.to_postfix()
        self.assertEqual(result, deque(['pi', '15', '+']))

    def test_incorrect_input_bracket(self):
        test = ShuntingYard('5+[5')
        with self.assertRaises(IncorrectInput):
            test.to_postfix()

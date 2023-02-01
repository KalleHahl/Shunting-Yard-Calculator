import unittest
from src.algorithms.postfix import to_postfix
from collections import deque


class TestTo_postfix(unittest.TestCase):

    def setUp(self):
        self.test = to_postfix

    # tests that the function appends correctly to the_stack by skipping spaces in input
    def test_skip_spaces(self):

        result = self.test('4 + 2 + 4 + 5')

        self.assertEqual(result, deque(['4', '2', '4', '5', '+', '+', '+']))

    # test for correct order of operators and operands in simple addition, if this works theres no reason to test subtraction since the are valued as equals in the algorithm
    def test_RPN__addition(self):

        result = self.test('1+2+3+4')

        self.assertEqual(result, deque(['1', '2', '3', '4', '+', '+', '+']))

    # test for correct order when multiplication and division is included
    def test_RPN_division_and_multiplication(self):

        result = self.test('2+5*10-4/2')

        self.assertEqual(result, deque(
            ['2', '5', '10', '*', '4', '2', '/', '-', '+']))

    # test for correct order when equation has power of
    def test_RPN_power_of(self):

        result = self.test('2+4*10+2^2^2+4/2')

        self.assertEqual(result, deque(
            ['2', '4', '10', '*', '2', '2', '^', '2', '^', '4', '2', '/', '+', '+', '+']))

    # test for correct order when equation has parentheses
    def test_RPN_parentheses(self):

        result = self.test('(1+2)*(10/2)^(2+1)')

        self.assertEqual(result, deque(
            ['1', '2', '+', '10', '2', '/', '2', '1', '+', '^', '*']))

    # test for correct order in ewuation with only division and multiplication
    def test_RPN_div_mul(self):

        result = self.test('5/5*5*5')

        self.assertEqual(result, deque(
            ['5', '5', '/', '5', '*', '5', '*']
        ))
    
    # test correct postfix for equation with float
    def test_RPN_float(self):

        result = self.test('1.2+4')

        self.assertEqual(result, deque(
            ['1.2','4','+']
        ))

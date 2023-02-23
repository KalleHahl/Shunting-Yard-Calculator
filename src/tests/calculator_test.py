import unittest
from io import StringIO
from unittest.mock import patch
from src.calculator import Calculator
from collections import deque


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
        self.calc.variables.add_variable('Z', '6.0')

    def test_add_variables(self):
        self.calc.input = "X=3+4"
        self.calc.add_variables()
        self.assertEqual(self.calc.variables.vars['X'], '7.0')

    def test_add_variables_negative(self):
        self.calc.input = "Y=-4*5"
        self.calc.add_variables()
        self.assertEqual(self.calc.variables.vars['Y'], '(-20.0)')

    def test_add_variables_invalid_input(self):
        self.calc.input = "z = 2 +"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.calc.add_variables()
        self.assertEqual(fake_output.getvalue().strip(), 'Incorrect input')

    def test_output(self):
        self.calc.calculation = deque(['3', '4', '+'])
        self.assertEqual(self.calc.output(), 7.0)

    def test_output_invalid_input(self):
        self.calc.calculation = deque(['3', '+'])
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.calc.output()
        self.assertEqual(fake_output.getvalue().strip(), 'Incorrect input')

    def test_shunt(self):
        self.calc.shunt('2 + 3')
        self.assertEqual(self.calc.calculation, deque(['2', '3', '+']))

    def test_shunt_invalid_input(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.calc.shunt('2 + *')
        self.assertEqual(fake_output.getvalue().strip(), 'Incorrect input')

    def test_sqrt_negative(self):
        self.calc.calculation = deque(['-25', 'sqrt'])
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.calc.output()
        self.assertEqual(fake_output.getvalue().strip(),
                         "Can't solve squareroot of negative")

    def test_division_by_zero(self):
        self.calc.calculation = deque(['5', '0', '/'])
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.calc.output()
        self.assertEqual(fake_output.getvalue().strip(),
                         "Can't divide by zero")

    def test_overflow(self):
        self.calc.calculation = deque(['5', '5', '5', '^', '^'])
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.calc.output()
        self.assertEqual(fake_output.getvalue().strip(),
                         "The value of the given calculation is too big")

    def test_incorrect_input_for_output(self):
        self.calc.calculation = deque(['15', 'sqrtd'])
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.calc.output()
        self.assertEqual(fake_output.getvalue().strip(), "Incorrect input")

    def test_commaerror_in_input(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.calc.shunt('5,5+12')
        self.assertEqual(fake_output.getvalue().strip(),
                         '5,5+12 -->            \n\nIncorrect use of a comma')

    def test_mismatched_parentheses_as_input(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.calc.shunt('(5+5*2')
        result = ' '.join(fake_output.getvalue().strip().split(' ')[-2:])
        self.assertEqual(result, '\n\nMismatched parentheses')

    def test_input_empty_function(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.calc.shunt('sin()+2')
        result = ' '.join(fake_output.getvalue().strip().split(' ')[-4:])
        self.assertEqual(result, '\n\nUsed an empty function')

    def test_start_calls_add_variables_when_input_contains_equals_sign(self):
        with patch.object(self.calc, 'add_variables') as mock_add_variables:
            with patch('builtins.input', side_effect=['x=5+3', 'quit']):
                self.calc.start()
            mock_add_variables.assert_called_once()

    def test_start_quits_when_user_enters_quit(self):
        with patch('builtins.input', return_value='quit'):
            with patch('sys.stdout', new_callable=StringIO) as fake_output:
                self.calc.start()
            self.assertEqual(fake_output.getvalue().strip(), 'Bye!')

    def test_start_prints_error_message_for_empty_input(self):
        with patch('builtins.input', side_effect=['', 'quit']):
            with patch('sys.stdout', new_callable=StringIO) as fake_output:
                self.calc.start()
            self.assertEqual(fake_output.getvalue().strip().split('\n')[
                             0], 'Type an expression')

    def test_help(self):
        with patch.object(self.calc, 'instructions') as mock_instructions:
            with patch('builtins.input', side_effect=['help', 'quit']):
                self.calc.start()
            mock_instructions.assert_called_once()

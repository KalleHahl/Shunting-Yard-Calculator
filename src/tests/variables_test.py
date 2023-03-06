from src.algorithms.variables import Variables
import unittest
from io import StringIO
from unittest.mock import patch

class Test_variables(unittest.TestCase):

    def setUp(self):
        self.variables = Variables()
        self.variables.add_variable('X', '5')
        self.variables.add_variable('Y', '16')

    def test_add(self):
        self.assertEqual(self.variables.vars, {'X': '5', 'Y': '16'})

    def test_fetch(self):
        result = self.variables.fetch_variables('5+Y^2+X')
        self.assertEqual(result, '5+16^2+5')

    def test_overwrite(self):
        self.variables.add_variable('X', '10')
        self.assertEqual(self.variables.vars, {'X': '10', 'Y': '16'})

    def test_fetch_with_no_variables(self):
        result = self.variables.fetch_variables('5+10^2-sin(4)')
        self.assertEqual(result, '5+10^2-sin(4)')

    def test_display(self):
        expected_output = "\nX = 5\n\nY = 16\n"
        with patch('sys.stdout', new = StringIO()) as fake_output:
            self.variables.display()
            self.assertEqual(fake_output.getvalue(), expected_output)
    
    def test_display_no_variables(self):
        self.variables.vars = {}
        expected_output = "\nNo variables added!\n"
        with patch('sys.stdout', new = StringIO()) as fake_output:
            self.variables.display()
            self.assertEqual(fake_output.getvalue(), expected_output)
        
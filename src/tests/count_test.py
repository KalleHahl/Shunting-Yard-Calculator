import unittest
from src.algorithms.count import Count
from src.algorithms.postfix import ShuntingYard
from src.errors.error import DivisionByZero, IncorrectInput, SquareRootOfNegative


class Test_Count(unittest.TestCase):

    # test correct value for addition
    def test_count_addition(self):

        test = ShuntingYard('5+5+10+4')
        result = Count(test.to_postfix()).count()
        self.assertEqual(result, 24)

    # test correct value for subtraction
    def test_count_subtraction(self):

        test = ShuntingYard('8+10-4').to_postfix()
        result = Count(test)
        result = result.count()
        self.assertEqual(result, 14)

    # test correct value for multiplication and division
    def test_count_multiplication_and_division(self):
        expression = ShuntingYard('2+5*10-4/2').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 50)

    # test correct value for power of
    def test_count_power_of(self):
        expression = ShuntingYard('2+4*10+2^2^2+4/2').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 60)

    # test correct value for equation with parentheses
    def test_count_parentheses(self):
        expression = ShuntingYard('(1+2)*(10/2)^(2+1)').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 375)

    # test correct value for equation with float
    def test_count_float(self):
        expression = ShuntingYard('1.2+4').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 5.2)

    def test_count_float_mul(self):
        expression = ShuntingYard('1.5*1.5').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 2.25)

    # test correct value for equation with only division and multiplication

    def test_div_mul_only(self):
        expression = ShuntingYard('2*8/4').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 4)

    # test correct value for cosin in radians
    def test_cos(self):
        expression = ShuntingYard('2*cos(4)').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, -1.3072872417272239)

    # test correct value for tangent in radians
    def test_tan(self):
        expression = ShuntingYard('2+5-tan(6)').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 7.291006191384749)

    # test correct value for sin in radians
    def test_sin(self):
        expression = ShuntingYard('2+5-sin(4)/6').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 7.126133749217988)

    # test correct value for calculation with sin,cos and multiplying
    def test_tan_cos(self):
        expression = ShuntingYard('tan(4)*cos(4)').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, -0.7568024953079282)

    # test correct value for calculation with power of and trigonometry
    def test_trigonometric_power(self):
        expression = ShuntingYard('2+tan(4)^2+5').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 8.34055012186162)

    # test a long calculation that has many operators and parentheses
    def test_long_calculation(self):
        expression = ShuntingYard(
            'sin(4)+((4*(7-3))/(2^3))-(10*(5/(2+3)))^2').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, -98.75680249530792)

    # Division by zero gives error
    def test_division_by_zero(self):
        expression = ShuntingYard('5+5+3+10/0+3+34+5').to_postfix()
        with self.assertRaises(DivisionByZero):
            Count(expression).count()

    def test_another_long_calculation(self):
        expression = ShuntingYard('((2*((2^3+4*cos(45))/(sin(30)+1)))-(3*((cos(60)^2)-(sin(45)/2))))+(1/((sin(60)+cos(30))*(cos(45)-sin(60))))'
                                  ).to_postfix()
        result = Count(expression).count()

        self.assertEqual(result, 1678.550503566695)

    # tests correct order when first operator is power of
    def test_first_operator_pow(self):
        expression = ShuntingYard('2^2+4*(2*2)').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 20)

    # tests for correct value with power of and multiplication
    def test_correct_order_pow_and_mul(self):
        expression = ShuntingYard('4+5+4+10/5+2^2*4').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 31)

    # tests for correct value with substracting only
    def test_only_subtracting_only(self):
        expression = ShuntingYard('5-5-5-5').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, -10)

    # this particular calculation gave faulty answer before
    def test_calculation_with_many_operators(self):
        expression = ShuntingYard('5+5+(5*5+5*5)-3-4-5*5*6').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, -97)

    # test that function correctly counts a negative number
    def test_negative_number(self):
        expression = ShuntingYard('-5-5').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, -10)

    # test sqrt
    def test_sqrt(self):
        expression = ShuntingYard('sqrt(4)').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 2)

    # test sqrt with multiple operators
    def test_sqrt_multiple_opps(self):
        expression = ShuntingYard('4^2+5*sqrt(9)/(4+5)^2').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 16.185185185185187)

    # test square root of negative
    def test_sqrt_negative(self):
        expression = ShuntingYard('sqrt(-25)').to_postfix()
        with self.assertRaises(SquareRootOfNegative):
            Count(expression).count()

    # test count with incorrect operator
    def test_incorrect_operator(self):
        expression = ShuntingYard('50+sinc(5)-10').to_postfix()
        with self.assertRaises(IncorrectInput):
            Count(expression).count()

    def test_min(self):
        expression = ShuntingYard('min(16,20)').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 16)

    def test_max(self):
        expression = ShuntingYard('max(2000,23)').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 2000)

    def test_min_max(self):
        expression = ShuntingYard(
            'min(max(30,40), min(500, 200))').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 40)

    def test_min_on_expressions(self):
        expression = ShuntingYard(
            '5+min(4^2+5*sqrt(9)/(4+5)^2,2^2*4-2)*2').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 33)

    def test_expression_with_many_negatives(self):
        expression = ShuntingYard('-5+12*(-2)-(-2)^2').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, -33)

    def test_abs(self):
        expression = ShuntingYard('abs(-15)').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 15)

    def test_abs_longer_expression(self):
        expression = ShuntingYard('2*4+(2+abs(-2))^2').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 24)

    def test_incorrect_input_with_comma(self):
        expression = ShuntingYard('(15,15)').to_postfix()
        with self.assertRaises(IncorrectInput):
            Count(expression).count()

    def test_log(self):
        expression = ShuntingYard('log(1000,10)').to_postfix()
        result = Count(expression).count()
        self.assertAlmostEqual(result, 3)

    def test_log_expresison(self):
        expression = ShuntingYard('((2+log(2^2,2))/2)^2').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 4)

    def test_incorrect_log(self):
        expression = ShuntingYard('log(3)').to_postfix()
        with self.assertRaises(IndexError):
            Count(expression).count()

    def test_ln(self):
        expression = ShuntingYard('ln(10)').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 2.302585092994046)

    def test_incorrect_plusses(self):
        expression = ShuntingYard('5+5+5+').to_postfix()
        with self.assertRaises(IndexError):
            Count(expression).count()

    def test_pi(self):
        expression = ShuntingYard('pi+12').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 15.141592653589793)

    def test_e(self):
        expression = ShuntingYard('2+e').to_postfix()
        result = Count(expression).count()
        self.assertEqual(result, 4.718281828459045)
    
    def test_incorrect_ln(self):
        expression = ShuntingYard('ln(0)').to_postfix()
        with self.assertRaises(ValueError):
            Count(expression).count()
    
    def test_incorrect_log_value_error(self):
        expression = ShuntingYard('log(0,0)').to_postfix()
        with self.assertRaises(ValueError):
            Count(expression).count()

import unittest
from src.algorithms.count import count
from src.algorithms.postfix import to_postfix


class Test_Count(unittest.TestCase):

    def setUp(self):

        self.test = count

    # test correct value for addition
    def test_count_addition(self):

        result = self.test(to_postfix('5+5+10+4'))

        self.assertEqual(result, 24)

    # test correct value for subtraction
    def test_count_subtraction(self):

        result = self.test(to_postfix('8+10-4'))

        self.assertEqual(result, 14)

    # test correct value for multiplication and division
    def test_count_multiplication_and_division(self):

        result = self.test(to_postfix('2+5*10-4/2'))

        self.assertEqual(result, 50)

    # test correct value for power of
    def test_count_power_of(self):

        result = self.test(to_postfix('2+4*10+2^2^2+4/2'))

        self.assertEqual(result, 60)

    # test correct value for equation with parentheses
    def test_count_parentheses(self):

        result = self.test(to_postfix('(1+2)*(10/2)^(2+1)'))

        self.assertEqual(result, 375)

    # test correct value for equation with float
    def test_count_float(self):

        result = self.test(to_postfix('1.2+4'))

        self.assertEqual(result, 5.2)

    def test_count_float_mul(self):

        result = self.test(to_postfix('1.5*1.5'))

        self.assertEqual(result, 2.25)

    # test correct value for equation with only division and multiplication

    def test_div_mul_only(self):

        result = self.test(to_postfix('2*8/4'))

        self.assertEqual(result, 4)

    # test correct value for cosin in radians
    def test_cos(self):

        result = self.test(to_postfix('2*cos(4)'))

        self.assertEqual(result, -1.3072872417272239)

    # test correct value for tangent in radians
    def test_tan(self):

        result = self.test(to_postfix('2+5-tan(6)'))

        self.assertEqual(result, 7.291006191384749)

    # test correct value for sin in radians
    def test_sin(self):

        result = self.test(to_postfix('2+5-sin(4)/6'))

        self.assertEqual(result, 7.126133749217988)

    # test correct value for calculation with sin,cos and multiplying
    def test_tan_cos(self):

        result = self.test(to_postfix('tan(4)*cos(4)'))

        self.assertEqual(result, -0.7568024953079282)

    # test correct value for calculation with power of and trigonometry
    def test_trigonometric_power(self):

        result = self.test(to_postfix('2+tan(4)^2+5'))

        self.assertEqual(result, 8.34055012186162)

    # test a long calculation that has many operators and parentheses
    def test_long_calculation(self):

        result = self.test(to_postfix(
            'sin(4)+((4*(7-3))/(2^3))-(10*(5/(2+3)))^2'))

        self.assertEqual(result, -98.75680249530792)

    # Division by zero gives error
    def test_division_by_zero(self):

        result = self.test(to_postfix('5+5+3+10/0+3+34+5'))

        self.assertEqual(result, "Can't divide by zero")

    # Parentheses error returns None
    def test_parentheses_error(self):

        result = self.test(to_postfix('5+5+5+(10*40+5'))

        self.assertEqual(result, 'No closing parentheses')

    def test_another_long_calculation(self):

        result = self.test(to_postfix(
            '((2*((2^3+4*cos(45))/(sin(30)+1)))-(3*((cos(60)^2)-(sin(45)/2))))+(1/((sin(60)+cos(30))*(cos(45)-sin(60))))'))

        self.assertEqual(result, 1678.550503566695)

    # tests correct order when first operator is power of
    def test_first_operator_pow(self):

        result = self.test(to_postfix('2^2+4*(2*2)'))

        self.assertEqual(result, 20)

    # tests for correct value with power of and multiplication
    def test_correct_order_pow_and_mul(self):

        result = self.test(to_postfix('4+5+4+10/5+2^2*4'))

        self.assertEqual(result, 31)

    # tests for correct value with substracting only
    def test_only_subtracting_only(self):

        result = self.test(to_postfix('5-5-5-5'))

        self.assertEqual(result, -10)

    # this particular calculation gave faulty answer before
    def test_calculation_with_many_operators(self):

        result = self.test(to_postfix('5+5+(5*5+5*5)-3-4-5*5*6'))

        self.assertEqual(result, -97)

    # test that function correctly counts a negative number
    def test_negative_number(self):

        result = self.test(to_postfix('-5-5'))

        self.assertEqual(result, -10)

    # test sqrt
    def test_sqrt(self):

        result = self.test(to_postfix('sqrt(4)'))

        self.assertEqual(result, 2)

    # test sqrt with multiple operators
    def test_sqrt_multiple_opps(self):

        result = self.test(to_postfix('4^2+5*sqrt(9)/(4+5)^2'))

        self.assertEqual(result, 16.185185185185187)

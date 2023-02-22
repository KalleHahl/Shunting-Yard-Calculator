class MismatchedParentheses(Exception):
    """Raised when user inputs incorrect parentheses"""


class CommaError(Exception):
    """Raised when input has invalid use of a comma"""


class EmptyFunction(Exception):
    """Raised when functions are used with no values"""


class IncorrectInput(Exception):
    """Raised when input is incorrect"""


class SquareRootOfNegative(Exception):
    """Raised when input has squareroot of negative"""


class DivisionByZero(Exception):
    """Raised when input has division by zero"""

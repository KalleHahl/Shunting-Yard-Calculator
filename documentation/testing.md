# Testing
At the moment there are four test files: one that tests the to_postfix-function found in postfix.py, one that tests the count-function found in count.py, a small test file for the variables class found in variables.py and tests for the calculator interface found in calculator.py.
The algorithm test files test with all the available operators and have tests with long calculations to ensure the algorithms work properly. The count tests should always give the proper answer to the calculation and the to_postfix tests test that the output is in correct postfix notation form. The variables testfile tests for adding variables to a dictionary and fetching them correctly when a function is called. The calculator testfile tests that correct text is output to the terminal when exceptions arise and that inputs call the correct functions. All of these tests are implemented using pythons unittest module.

Coverage stats can be found here [![codecov](https://codecov.io/gh/KalleHahl/tiralabra/branch/main/graph/badge.svg?token=D9XSGLPQI0)](https://codecov.io/gh/KalleHahl/tiralabra)
# Coverage
Typing ```poetry run invoke coverage-report``` into the commandline runs the pytests, prints the coverage info and writes an HTML report to htmlcov/index.html. Typing ```poetry run invoke coverage-show``` opens the html report in your browser.
# Pylint
Running pylint can be done by typing ```poetry run invoke pylint``` in the command line

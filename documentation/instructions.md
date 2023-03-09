# Installation:
Clone this reposirotry into your desired directory by running the command ```git clone https://github.com/KalleHahl/tiralabra```.
Install dependencies by running ```poetry install```.
# Start:
Start the program by running ```poetry run invoke start``` in the command line, you are now ready to type inputs. For instructions regarding functions and inputs, type 
```help```. To display variables type ```variables```, instructions on how to add variables are found later in this document. Quit the program by typing ```quit```
# Correct inputs:
* Expressions should be written without spaces e.g. ```5+5*2```. Spaces don't affect the value given by the calculator and don't cause any errors, it just adds unnecessary steps that are visualized while parsing.

* Floating numbers use `.` not `,`.

* **Operators:**
  - Addition: `+`
  - Subtraction: `-`
  - Multiplication: `*`
  - Division: `/`
  - Exponentiation: `^`

* **Unary functions:**
  - Sin: `sin(x)`
  - Cos: `cos(x)`
  - Tan: `tan(x)`
  - Square root: `sqrt(x)`
  - Absolute value: `abs(x)`
  - Natural logarithm: `ln(x)`

* **Binary functions:**
  - Minimum value: `min(x,y)`
  - Maximum value: `max(x,y)`
  - Logarithm: `log(value,base)`

* **Mathematical constants:**
  - Pi: `pi`
  - Euler's number: `e`

* Parentheses are used like in normal mathematical expressions e.g. `(5+5)/2`.

* Use parentheses with negative numbers e.g. `5+(-2)`. Parentheses ***are not*** necessary if the number is the first number in the calculation e.g. `-5+2` or if the number is the first number inside parentheses e.g. 
`5+(-2*3)`.

* **Variables:**
  - Add variables by typing e.g. `Y=(5+5)^2`.
  - Add one variable at a time.
  - Use single capital letters for variable names!
  - Once again, using spaces is OK but it will affect the visualization.
  - If the inputs are incorrect, a notification is given and variables will not be added.
# Incorrect inputs:
* If the instructions above are followed, no errors should arise.

* However if the instructions are not followed one of the following errors will be raised:
  - `CommaError`: incorrect use of a comma
  - `DivisionByZero`: expression has division by zero
  - `SquareRootOfNegative`: expression has square root of negative
  - `OverFlowError`: given expression exceeds the value that can be outputted e.g. `5^5^5^5`
  - `MismatchedParentheses`: incorrect use of parentheses
  - `EmptyFunction`: used an empty function e.g. `ln()`
  - `IndexError`: this is usually raised when using a nonexistent function e.g. `sinc(4)`
  - `IncorrectInput`: Some sort of incorrect input is given
 
 * When an error is raised, user is informed with a message in the terminal.
 

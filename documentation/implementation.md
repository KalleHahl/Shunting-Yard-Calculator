# Implementation
## Structure
*This programs structure consists of the interface in calculator.py and the algorithms to_postfix in the ```ShuntingYard``` class and count in the ```Count``` class. A class for variables is also included in the variables.py file*
#### To_postfix:
This algorithm is the heart of this project. It uses the shunting yard algorithm to parse mathematcial expressions written in infix notation into a reverse Polish notation (postfix notation).
The algorithm works with operators (+,-,*,/,^), unary operators (sin,cos,tan,sqrt,abs,ln), min, max, log and parentheses. Parsing is achieved by looping through the input and using two stacks, one for operators and one where the operands and operators are appended in the correct postfix notation.
The idea of this algorithm is to make a mathematical expression into a linear form in which operator precedence has already been taken to account.
#### Count:
This algorithm is the one which produces the correct value from the postfix expression. It works by looping through the expression and appending operands into a stack, once an operator is encountered a correct operation is fetched from a dictionary and the operands are popped from the stack.
If an operator is a normal operator, let's say +, the two top operators from the stack are popped, the first to the left side and the second to the right side of the operation.
Then the given value from the operation is appended back on top of the stack. If the operator is an unary operation, let's say squareroot, only the first operand from the stack is popped and the given value from the operation is appended back into the stack.
Once the expression is looped through, the remaining value in the stack is the answer to the given expression.
## Time complexity
#### To_postfix &rarr; O(n)
The use of two stacks (one for operators and one for operands) ensures that the algorithm's time complexity remains linear, even when dealing with complex expressions that contain nested parentheses and multiple levels of operator precedence. 
In the worst-case scenario, where all the tokens in the expression are parentheses, the time complexity would be O(n^2). However, this is a very unlikely scenario and in most practical cases, the time complexity of the Shunting Yard Algorithm remains linear.
#### Count &rarr; O(n)
Once again, expression is looped through once and the time complexity remains linear. Unlike in the shunting yard algorithm, the input expression can't contain parentheses so no nested loops are needed.
This ensures that even in the worst-case scenario, the time complexity remains O(n).
## Space complexity
Both of the algorithms have a space complexity of O(n) where n is the length of the expression.
## What to improve?
Tokenizing the expression before inputting it into the shunting yard algorithm. This means that instead of looping through every character in the expression, the algorithm would take a list as an input, where each element is a separate token (operator or operand) reducing the time used by the shunting yard algo.
## Sources:
- [Infix to reverse polish using a stack](https://www.youtube.com/watch?v=LQ-iW8jm6Mk)
- [Comp Sci in 5: Shunting Yard Algorithm](https://www.youtube.com/watch?v=Wz85Hiwi5MY)
- [Comp Sci in 5: Post Fix Stack Evaluator](https://www.youtube.com/watch?v=bebqXO8H4eA)
- [Shunting yard wiki](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)


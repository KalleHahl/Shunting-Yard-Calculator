# Week 4
### What I've achieved?
This week I coded a simple interface for the calculator. After typing the expression you want solved, the parsing of the postfix notation is then visualized in the console and a correct value is printed.
I also fixed to major errors with the algorithm and implemented squareroot function.

### Troubles: 
Encountered a major error with the algorithm. First I hadn't taken into consideration that the power of is a left associative operator, meaning chained powers of are counted from the left to the right.
After fixing that I encountered another problem with chained subtractions. Managed to fix this issue aswell.
### What I've learned?
Learned the importance of testing. Even though I had plenty of tests written, which had expressions with multiple operators and parentheses, I still had a major error in the algorithm that the tests didn't detect.
Need to start writing smaller tests which test small operations a time.
### Hours spent:
12
### Goals for next week:
- Implement min, max
- Start working on the option to save values to variables and use them in the expressions

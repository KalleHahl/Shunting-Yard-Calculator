# Definition document
The aim of this project is to code a calculator, which takes a user input of a mathematical expression in infix format, turns it into its reverse polish notation (postfix) and then calculates the correct value.
My goal is to also setup a text UI, from which the user sees the correct value and the postfix form of the expression. This project will be made using python.
## Algorithms, datastructures and time/space complexity
This project uses the shunting yard algorithm created by Edsger W. Dijkstra to first form a postfix version of the given expression and then a separate algorithm to calculate its value. The algorithms use a stack as the main datastructure
to store the operators and operands for later use. Time complexity of O(n) is the goal for any shunting yard algorithm since it really only needs to loop through the input once. Space complexity is also O(n), where n is the tokens (operators&operands) in the input. 
## Details related to this course
Python is the only language I'm capable of coding (very limited knowledge on Java) so it would be best to get projects to peer review which also use python. I am currently enrolled in a Bachelor's degree program in Computer Science. I will be writing the documentation and other related stuff (files, functions and comments in the code) for this course in english.
### Sources:
- [Infix to reverse polish using a stack](https://www.youtube.com/watch?v=LQ-iW8jm6Mk)
- [Comp Sci in 5: Shunting Yard Algorithm](https://www.youtube.com/watch?v=Wz85Hiwi5MY)
- [Comp Sci in 5: Post Fix Stack Evaluator](https://www.youtube.com/watch?v=bebqXO8H4eA)
- [Shunting yard wiki](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)


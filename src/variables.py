"""
    Class for variable storing and fetcing
"""
class Variables:

    def __init__(self):
        self.vars = {}

    def add_variable(self, variable, value):
        self.vars[variable] = value

    def fetch_variables(self, expression):

        #Loop the expression, if a variable is found
        #replace it in the expression
        for character in expression:
            if character in self.vars:
                new = expression.split(character)
                expression = f"{new[0]}{self.vars[character]}{new[-1]}"

        return expression

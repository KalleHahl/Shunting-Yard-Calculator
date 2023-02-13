
class Variables:

    def __init__(self):
        self.vars = {}
    
    def add_variable(self, variable, value):
        self.vars[variable] = value
    
    def fetch_variables(self, expression):

        for keys, values in self.vars.items():
            if keys in expression:
                new = expression.split(keys)
                expression = f"{new[0]}{values}{new[-1]}"
        
        return expression

    def __str__(self):
        return self.vars
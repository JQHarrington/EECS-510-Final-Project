class PDA:
    def __init__(self):
        self.stack = [] # initialize empty stack
        self.current_state = "q0" # start state
        self.result = 0 # stores the result of the equation

    def process_symbol(self, symbol):
        # code for state q0
        if self.current_state == "q0": # checks if current state is start state
            if symbol.isdigit():
                self.stack.append(int(symbol)) # adds symbol to stack
                self.current_state = "q1" # transitions state to q1
            elif symbol == "(":
                self.stack.append(symbol) # adds symbol to stack with no state transition
            else:
                raise ValueError("Invalid start symbol")
        
        # code for state q1
        elif self.current_state == "q1": # checks if current state is q1
            if symbol in ["+", "-"]:
                self.stack.append(symbol) # adds symbol to stack
                self.current_state = "q2" # transitions to state q2
            elif symbol == ")":
                self.reduce_parentheses() # no state transition calls function to compute inner product inside of parantheses
            else:
                raise ValueError("Unexpected symbol after number")

        # code for state q2
        elif self.current_state == "q2": # checks if current state is q2
            if symbol.isdigit():
                self.stack.append(int(symbol)) # adds symbol to stack
                self.current_state = "q1" # transitions to state q1
            elif symbol == "(":
                self.stack.append(symbol) # adds symbol to stack with no state transition
            else:
                raise ValueError("Invalid operator symbol")

    # function used to compute inner product of parentheses
    def reduce_parentheses(self):
        temp_stack = []
        while self.stack:
            top = self.stack.pop()
            if top == "(":
                break
            temp_stack.append(top)
        self.stack.append(self.evaluate(temp_stack[::-1]))


    # function used to compute the product of an equation
    def evaluate(self, expr):
        total = expr[0]
        i = 1
        while i < len(expr):
            operator = expr[i]
            number = expr[i + 1]
            if operator == "+":
                total += number
            elif operator == "-":
                total -= number
            i += 2
        return total
    

    # clean up function
    def finalize(self):
        while len(self.stack) > 1:
            temp_stack = []
            while self.stack:
                temp_stack.append(self.stack.pop())
            self.stack.append(self.evaluate(temp_stack[::-1]))
        self.result = self.stack.pop()

    # helper function for handling 
    def run(self, expression):
        for symbol in expression:
            self.process_symbol(symbol)
        self.finalize()
        return self.result
    

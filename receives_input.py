class receives_input:
    #handles input. 2 numbers (each >0 and <10). assumes input is valid numbers. greater than 0, less than 10. only 2 numbers.
    import performs_calc

    def __init__(self, a,b):
        self.a = a
        self.b = b

        array = [self.a, self.b]

    

    def pick_operation(self):
            print("pick an operation: +, -, *, /")
         
            operation = input()
            self.calc=self.performs_calc()

            switcher = {
                "+": self.calc.add(self.a,self.b),
                "-": self.calc.subtract(self.a,self.b),
                "*": self.calc.multiply(self.a,self.b),
                "/": self.calc.divide(self.a,self.b)
              
            }
        
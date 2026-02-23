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
            self.calc=self.performs_calc(self.array)

            switcher = {
                "+": self.calc.add(self.array[0],self.array[1]),
                "-": self.calc.subtract(self.array[0],self.array[1]),
                "*": self.calc.multiply(self.array[0],self.array[1]),
                "/": self.calc.divide(self.array[0],self.array[1])
              
            }
        
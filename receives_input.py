class receives_input:
    #handles input. 2 numbers (each >0 and <10). assumes input is valid numbers. greater than 0, less than 10. only 2 numbers.
    import performs_calc

    def __init__(self):
        self.a = input("Enter the first number: a number between 0 and 9: ")
        self.b = input("Enter the second number: a number between 0 and 9: ")

      
    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def pick_operation(self, a, b):
        operation = input("Enter the operation you would like to perform: +, -, *, /: ")
        calc = self.performs_calc()
        if operation == "+":
            print(calc.add(a, b))
        elif operation == "-":
            print(calc.subtract(a, b))
        elif operation == "*":
            print(calc.multiply(a, b))
        elif operation == "/":
            print(calc.divide(a, b))
        else:
            print("Invalid operation. Please enter +, -, *, or /.") 
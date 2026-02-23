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

    def pick_operation(self):
        operation = input("Enter the operation you would like to perform: +, -, *, /: ")
        calc = self.performs_calc()
        num1 = self.get_a()
        num2 = self.get_b()
        # use Python 3.10+ match statement as a switch replacement
        match operation:
            case "+":
                print(calc.add(num1, num2))
            case "-":
                print(calc.subtract(num1, num2))
            case "*":
                print(calc.multiply(num1, num2))
            case "/":
                print(calc.divide(num1, num2))
            case _:
                print("Invalid operation. Please enter +, -, *, or /.") 
class receives_input:
    #handles input. 2 numbers (each >0 and <10). assumes input is valid numbers. greater than 0, less than 10. only 2 numbers.
    import performs_calc

    def __init__(self, a,b):
        self.a = a
        self.b = b

      
    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def pick_operation(self):

       
        self.calc = performs_calc(self.a,self.b)
        operation = input("Enter the operation you want to perform: +, -, *, / ")
            
        
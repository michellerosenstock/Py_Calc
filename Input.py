class Input:
 
    def __init__(self ):
        self.a = input("Enter the first number - 0 though 9: ")
        self.b = input("Enter the second number: - 0 though 9:")     

        print(f"Input values:", self.a, self.b)
    def get_a(self):
        return self.a
    def get_b(self):
        return self.b 
        
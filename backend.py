class backend:
  print("this is where the backend will exist")
  #takes in two numbers. each number is already-validated and converted into a float.
  num1=0.0
  num2=0.0

  def __init__(self, num1, num2):

    self.num1 = num1
    self.num2 = num2
  
  def get_num1(self):
    return self.num1

  def get_num2(self):
    return self.num2
    
      
  def __init__(self):
    self.input = Input()
    num1 = self.input.get_a()
    num2 = self.input.get_b()
    print("this takes in the input from the user and stores it in the backend", num1," and ", num2)


  #calculation functions
  #add returns the sum of two numbers
  def add(self, num1, num2):
    return num1 + num2
  #subtract returns the difference of two numbers
  def subtract(self, num1, num2):
    return num1 - num2
  #multiply returns the product of two numbers
  def multiply(self, num1, num2):
    return num1 * num2
  #divide returns the quotient of two numbers
  def divide(self, num1, num2):
    return num1 / num2
 
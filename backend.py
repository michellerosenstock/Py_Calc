class backend:
  print("this is where the backend will exist")
  #takes in two numbers. each number is already-validated and converted into a float.
  num1 = 0.0 
  num2 = 0.0


  def __init__(self):
    self.input = Input()
    num1 = self.input.get_a()
    num2 = self.input.get_b()
    print("this takes in the input from the user and stores it in the backend", num1," and ", num2)


  #calculation functions
  #add returns the sum of two numbers
  def add():
    return num1 + num2
  #subtract returns the difference of two numbers
  def subtract():
    return num1 - num2
  #multiply returns the product of two numbers
  def multiply():
    return num1 * num2
  #divide returns the quotient of two numbers
  def divide():
    return num1 / num2
 
class backend:
  print("this is where the backend will exist")
  #takes in two numbers. each number is already-validated and converted into a float.

  #object constructor
  def __init__(self, a=0.0, b=0.0):
    self.a = a
    self.b = b
    print("this is the default back-end constructor")


  #calculation functions
  #add returns the sum of two numbers
  def add(num1, num2):
    return num1 + num2
  #subtract returns the difference of two numbers
  def subtract(num1, num2):
    return num1 - num2
  #multiply returns the product of two numbers
  def multiply(num1, num2):
    return num1 * num2
  #divide returns the quotient of two numbers
  def divide(num1, num2):
    return num1 / num2
 
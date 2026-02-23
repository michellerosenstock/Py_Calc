
from receives_input import receives_input



inp = receives_input()
  
num1 = float(inp.get_a())
num2 = float(inp.get_b())  

inp.pick_operation(num1, num2)    


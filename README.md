Made a simple basic calculator program to practice what I learned in my Python refresher.

    created objects and functionality spread across 3 classes to gain practice with classes, objects, and dependencies.
    created 2 single variables.  

The "architecture" consists of a 3-class program: main class, receives_input class, performs_calc class.

    main class: calls receives_input class so user can interact with calculator functionality. 
        has an instance of the receives_input class, which connects to the performs_calc class.
            

    receives_input class: accepts input for 1st num, 2nd num, and operation symbol
        is an object in the main class.
        has an instance of the performs_calc class in the pick_operation function.
        

    performs_calc class: performs selected operations on inputted 1st num and 2nd num. 
        is an object in the receives_input class.
 


To keep it simple, this project makes the following assumptions:
    
    only 2 numbers. User enters each number one at a time and hits the enter key each time. 
       
        each number is only a string representation of an inputted positive integer.
       
        each number is converted from string into a floating point number.
       
        each number is inputted in valid format. 

            Only assuming inputs are: '1,2,3,4,5,6,7,8,9'. 
        
        each number is > 0 and < 10. 
            Does not include 0. Does not include 10.
        
        each operation is one of these characters: '+', '-', '*', '/' . 

            only 4 operation choices are valid.

            only 1 operation is selected.

            only 1 operation is performed on the 2 operands.


        each operation is mapped to it's matching calculation function.

            "+" symbol is associated with the sum function. returning a+b.

            "-" symbol is associated with the subtraction function. returning a-b.

            "*" symbol is associated with the multiplication function. returning a*b.

            "/" symbol is associated with the division function. returning a/b.

                assumed that the "b" value is greater than 0 for this function. 

        each calculation function associated witih specific operation symbol performs that operation
    

If I were to further simplify this project, i would consolidate the 3 .py files into the 1 main.py file.

To expand it further, this project could allow for:
    an enhanced control structure.
    more complex logic.
    more flexible and varied data structures.
    more/different structure of classes: refractored code and changing logic as well.
    2 or more numbers, 1 or more operations, an actual UI.
        each number to be positive/negative integer. Inputted as string.
        each number to be other types of numbers outside of integers or floating point numbers.
        each number to be stored in a resizable structure instead of single variables 
            when more than 2 numbers are inputted
        each number to be validated by more than the simple conversion from string to float
            with actual exception-handling logic.
                





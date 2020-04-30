"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def calculate_two_numbers():
    print("Welcome to the Calculator.")

    print('Please enter one of the following operators: add, substract, multiply, divide, square, cube, exponent, or remainder, followed by the numbers you would like to calculate. For example, "add 5 3". Press "q" to exit the calculator.')
    
    calculator_input = input("What would you like to calculate first? ")
    tokens = calculator_input.split(' ')
   
    operator = tokens[0]
    
    num1 = float(tokens[1])
    
    num2 = float(tokens[2])
   
    while True:
        if tokens == 'q':
            break

        elif operator == 'add':
            result = add(num1, num2)
            print(result)
            break

        elif operator == 'substract':
            result = subtract(num1, num2)
            print(result)
            break

        elif operator == 'multiply':
            result = multiply(num1, num2)
            print(result)
            break

        elif operator == 'divide':
            result = divide(num1, num2)
            print(result)
            break

        elif operator == 'square':
            result = square(num1)
            print(result)
            break

        elif operator == 'cube':
            result = cube(num1)
            print(result)
            break

        elif operator == 'exponent':
            result = power(num1, num2)
            print(result)
            break

        elif operator == 'remainder':
            result = mod(num1, num2)
            print(result)
            break
        

        elif operator == 'subtract':
            result = subtract(num1, num2)
                
calculate_two_numbers()


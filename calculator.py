"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


print("Welcome to the Calculator.")

user_calculation = 'Please enter one of the following operators: add, substract, multiply, divide, square, cube, or exponent, followed by the numbers you'd like to calculate. For example, "add 5 3". What would you like to calculate first?')

#while True:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

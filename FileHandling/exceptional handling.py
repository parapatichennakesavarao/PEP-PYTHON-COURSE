#Eceptional Handling in Python
#a mechanism for managing runtime errors (known as exceptions) that disrupt the normal flow of a program
try:
    # Code that might raise an exception
    result = 10 / 0 
except ZeroDivisionError:
    # Code to handle the specific exception
    print("Error: You cannot divide by zero!")

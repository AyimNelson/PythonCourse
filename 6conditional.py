# Conditional Statements
"""
Checks if a contion is True then run a block of code
"""
# if()


# Syntax
"""
if(condition):
    statement/code
    
"""

# Using comparism operators
# Equality operator
if (23 == 23):
    print("The number 23 is equal to 23")
    

# less than or equal to
if(23<=23):
    print("The number 23 is less than or equal to 23")

# Introduction variables
num = 35
if (num>=12):
    print(f"{num} is greater than equal to 12")
    
# Introducing inputs

name = input("Please enter your name: ")

if (name == "Kofi"):
    print(f"Your name is {name}")


# Perform an operation
num1 = int(input("Please enter Num1: "))
num2 = int(input("Please enter Num2: "))

if (num1 == num2):
    print(f"Num1 is equal to Num2")
    
# Authentication
username = "kofi"
password = 1234

username1 = input("Please enter your username: ")
password1 = int(input("Please enter your password: "))

if (username == username1 and password==password1):
    print("Your credentials are correct")
    
# Continuation of conditional...

# Else if (elif)
"""
use elif() to check for multiple conditions

"""
name = 'kofi'

if (name=="k"):
    print("Name is k")
    
elif(name=="ko"):
    print("Name is Ko")
    
elif(name=="kof"):
    print("Name is Kof")
    
elif(name=="kofi"):
    print("Name is Kofi")

# Application

num = int(input("Please enter any number between(1-9): "))

if (num==1):
    print("Number is 1")
elif (num==2):
    print("Number is 2")
elif (num==3):
    print("Number is 3")
elif (num==4):
    print("Number is 4")
elif (num==5):
    print("Number is 5")
elif (num==6):
    print("Number is 6")
elif (num==7):
    print("Number is 7")
elif (num==8):
    print("Number is 8")
elif (num==9):
    print("Number is 9")

    
# Else Statement
"""
syntax

if(condition):
    # if the condition is True
    statement/code
else:
    # if the condition is False
    statement/code

"""

if (2==3):
    print("The condition is True")
else:
    print("The condition is False")


# Application

num3= int(input("Please Enter a number: "))
if (num3 == 23):
    print("The number is True")
else:
    print("The number is False")
    
    
    
# Adding else to the elif 
num4 = int(input("Please enter any number between(1-9): "))

if (num4==1):
    print("Number is 1")
elif (num4==2):
    print("Number is 2")
elif (num4==3):
    print("Number is 3")
elif (num4==4):
    print("Number is 4")
elif (num4==5):
    print("Number is 5")
elif (num4==6):
    print("Number is 6")
elif (num4==7):
    print("Number is 7")
elif (num4==8):
    print("Number is 8")
elif (num4==9):
    print("Number is 9") 
else:
    print("None of the numbers is between 1 - 9")




# Nested if

"""
Nested if() statement contains an if() statement within an if() statement
#Syntax


if(condition):
    # if the outer condition is True
    if(condition):
        # if the condition is True
        statement/code
    else:
        # if the condition is False
        statement/code

else:
    # if the condition is False
    statement/code

        
"""
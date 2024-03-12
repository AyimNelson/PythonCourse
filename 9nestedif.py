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

# Ticketting APP
"""
age = int(input("Please enter your age: "))
is_foreigner = input("Are you a Foreigner? yes/no ")

if(age<=5):
    if(is_foreigner=='yes'):
        print("Pay 5cedis for entry")
    elif(is_foreigner=='no'):
        print("You have access")
    else:
        print("Please enter yes/no in lower case")

elif(age<=15):
    if(is_foreigner=='yes'):
        print("Pay 15cedis for entry")
    elif(is_foreigner=='no'):
        print("Pay 10cedis for entry")
    else:
        print("Please enter yes/no in lower case")
else:
    print("You have to pay 20cedis for entry")

"""

# Travelling condition

busy_road = input("Is there traffic on the road yes/no?: ")
plane_ticket = int(input("What is the price of the planes ticket? "))

if(busy_road=="yes"):
    if(plane_ticket<=200):
        print("Travelling to Kumasi by plane")
    else:
        print("Return to the bus station and board the Bus")
else:
    print("Traveling to Kumasi by Bus")



# The pass keyword

if(23==23):
    pass

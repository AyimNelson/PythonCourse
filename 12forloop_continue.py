"""
The continue Statement
With the continue statement we can stop the current iteration of the loop, and continue with the next:
"""

fruits = ["PineApple", 'Apple', "Mango", "Phone", "Grapes", "Oranges", "Banana"]
print("----For loop with continue-----")
for item in fruits:
    if item=="Phone":
        continue
    print(item)


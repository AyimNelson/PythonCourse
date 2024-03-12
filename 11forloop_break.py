"""
The break Statement
With the break statement we can stop the loop before it looped through all the items:

"""
fruits = ["PineApple", 'Apple', "Mango", "Grapes", "Oranges", "Banana"]
# Running a for loop
for item in fruits:
    print(item)

# Running for loop with break
print("-------For loop with break-----")
for item in fruits:
    if item=="Apple":
        print(item)
        
    if item == "Mango":
        print(item)
        break
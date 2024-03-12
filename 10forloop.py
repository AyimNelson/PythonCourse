"""
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

Syntax

for item in objects:
    codes    
"""
# For loop with list data structure
fruits = ["Mango", "Pear", "Pineapple", "Apple", "Grapes"]

for item in fruits:
    print(item)

# For loop with srting
town = "Kasoa"
for alphabet in town:
    print(alphabet)

# More examples
electronics = ["Iphones", "Samsung", "Chargers", "Batteries", "Earpieces", "Earpods", "Headphones", "Laptops", "MousePads"]

print("--------Items in Shop-------")
for item in electronics:
    print(item)


# More examples with if condition

print("--------Items in Shop-------")
for item in electronics:
    print(item)
    if(item=="Iphones"):
        print("I want to buy an iphone")
        
"""
Access Items
List items are indexed and you can access them by referring to the index number:


Note: The first item has index 0.
"""
fruits = ["mango", "banana", "apple", "pineapple", 'pear', "grapes", "coconut", "Almonds", "starfruit", "tomato", "alasa"]

print(fruits[0])
print(fruits[6])
print(fruits[9])

# Negative Indexing
print("------Negative indexing------")
print(fruits[-1])
print(fruits[-10])


# Range of Indexes
"""
Syntax
List_name[n:M]
n= The starting point of the range
M= The ending point of the range but not included

"""
print("------Range of items------")

print(fruits[5:10])


# Range of Negative Indexes
print("------Negative Range of items------")
print(fruits[-10:-1])
print(fruits[-6:-1])

"""
By leaving out the end value, the range will go on to the end of the list:
"""
print("----Leaving the last value of the range------")
print(fruits[-5:])
print(fruits[5:])

print("----Leaving the first value of the range------")
print(fruits[:5])

# Check if Item Exists
"""
To determine if a specified item is present in a list use the in keyword:
Syntax

if 'item' in List:
    codes
"""
if "tomato" in fruits:
    print("There is tomato in fruits")
    
if 'pineapple' in fruits:
    print("Pineapple")
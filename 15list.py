# List Data Structure
# Syntax
"""
list = []
"""

fruits = ["mango", "Pineapple","Banana", "mango", "Apple", 574, 67.45,True, False, True]

# Index
# The position of an object in a list data structure

for item in fruits:
    print(item)


print("------index 3----")
print(fruits[3])


print("------index 4----")
print(fruits[4])

print("------index 0----")
print(fruits[0])


#  Lenght of an List
# Syntax
# len(list)

print("----- Lenght ------")
print(len(fruits))


# while loop on lenght
count = 0
lenght = len(fruits)
while count<lenght:
    print(f"Fruit count {count}")
    count = count+1



# Duplicates
print("-----Printing Duplicates------")
print(fruits)


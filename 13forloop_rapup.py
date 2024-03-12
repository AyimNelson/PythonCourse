# Else and pass

#  Pass

words = "Man"
for alphabet in words:
    pass

# Else

for alphabet in words:
    print(alphabet)
else:
    print("All Alphabets has been printed successfully!")

# Example
fruits = ["PineApple", 'Apple', "Mango", "Grapes", "Oranges", "Banana"]
print("----For loop with else-----")
for item in fruits:
    print(item)
else:
    print("All items have been printed successfully!")

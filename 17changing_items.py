fruits = ["mango", "banana", "apple", "pineapple", 'pear', "grapes", "coconut", "Almonds"]


print("----adding items-----")
fruits[2]="tomato"
print(fruits[2])

print(fruits)

fruits[1:4]=""
print(fruits)

fruits[1:4]="new"
print(fruits)

fruits[-3:-2] = ""
print(fruits)

fruits[-3:-2] = "toy"
print(fruits)

fruits.insert(2, "starfruits")
print(fruits)

fruits.insert(4, "alasa")
print(fruits)

fruits.insert(-1, "tomato")
print(fruits)


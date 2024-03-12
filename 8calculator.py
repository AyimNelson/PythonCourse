# Building a calculator

num1 = int(input("Please Enter the first Number: "))
num2 = int(input("Please Enter the Second Number: "))

additon = num1 + num2
multiple = num1 * num2
division = num1/num2
floor_division = num1//num2
modulo = num1%num2
subtraction = num1 - num2
exponent = num1**num2

print(f"The addition of {num1} and {num2} is {additon}")
print(f"The multiple of {num1} and {num2} is {multiple}")
print(f"The division of {num1} and {num2} is {division}")
print(f"The floor division of {num1} and {num2} is {floor_division}")
print(f"The reminder of {num1} and {num2} is {modulo}")
print(f"The subtraction of {num1} and {num2} is {subtraction}")
print(f"The Exponent of {num1} and {num2} is {exponent}")

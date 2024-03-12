
"""The while Loop
With the while loop we can execute a set of statements as long as a condition is true."""

i = 1
while i < 6:
  print(i)
  i = i + 1

# Create a password with if, else and break

count = 0
password = "1234"
print("-----Password Validation-----")
while count <= 3:
    pass_input = input("Please enter your password: ")
    if(pass_input == password):
        print("You have access")
        break
    else:
        count = count+1
        print("Your password is not correct")

    if(count==4):
        print("Your account has been blocked")



# Talkertive

talk = 0
while talk<=1000:
    print("I will not talk in class again")
    talk = talk+1


# While loop with continue

a = 0
while a<5:
    a=a+1
    if a == 3:
        continue
    print(f"{a} is less than or equal to 5")
    



"""The else Statement
With the else statement we can run a block of code once when the condition no longer is true:"""

code = 1
while code<10:
    print("Code is less that 10")
    code = code + 2
else:
    print("Code is no longer than 10")



q = 0
while q<45:
    print("Q is less than 45")
    q=q+5
else:
    print("Q is no longer less than 45")
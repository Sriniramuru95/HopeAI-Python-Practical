"""
Extra Assignement question Python 3
"""


# print 'CORRECT' if i == 10 

value= int(input("Enter a number: "))

if value == 10:
    print("CORRECT")
else:
    print("WRONG")

# Check the password, using if and else 
pass1 = "HopeAI123"
password = input("Enter the password: ")
if password == pass1:
    print("Your password is correct")
else:
    print("Your password is incorrect") 

 # Catagory the people by their age like children, adult, citizen, senior citizen... 
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
elif age < 60:
    print("You are an adult")
else:
    print("You are a senior citizen")


 # Find whether given number is positive or negative

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
elif num < 0:
    print("The number is negative.")    

# Check whether the given number is divisible by 5

num1 = int(input("Enter a number to check: "))
if num1 % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")
"""
Python function - def function name (parameters):

Function Assignments-1

"""
import re



# Create Function - 1




def Subfields(list1):
    print("Sub-fields in AI are: ")
    for i in list1:
        print(i)
#Prepare List
list1 = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']

# Call Funcation
print("=" * 60)
print("Create Function - 1 - Subfields()")
Subfields(list1)
print("=" * 60)

# Create Function - 2 - OddEven()

def OddEven(num1):
    print("Enter a number: ",num1) 
    if num1%2 == 1:
        message =  "{} is Odd Number".format(num1)
    else:
        message = "{} is Even Number".format(num1)
    return message

print("=" * 60)
print("Create Function - 2 - OddEven()")
msg = OddEven(int(input("Enter a number: ")))  

print(msg)
print("=" * 60)


# Create Function - 3 - Elegible()

def Elegible(gen,age):
    print("Your Gender: ",gen)
    print("Your age: ",str(age))
    gen=gen.upper()
    if age < 18 and gen ==  "MALE" "FEMALE":
        print("NOT ELIGIBLE")
    elif age > 20 and gen ==  "MALE" :
         print("ELIGIBLE")
    elif age > 18 and gen ==  "FEMALE" :
        print("ELIGIBLE")
    elif age == 20 and gen ==  "MALE" :
        print("YOU WILL ELIGIBLE NEXT YEAR")
    else:
        print("bye")
        print("Input out of range. Given Age is {} and Gender is {} ".format(age,gen))
print("=" * 60)   
print("Create Function - 3 - Elegible()")
age = int(input("Enter your age : "))
gen = input("Enter you Gender:  ")
Elegible(gen,age)
print("=" * 60)

# Create Function - 4 -  percentage()

def  percentage(sub):
    j = 1
    total = 0
    for i in sub:
        print("Subject{} = {}".format(j,i))
        total = total + i
    j=+1
    print("Total : ",total)
    pert = total/len(sub)
    print("Percentage : " ,pert )
print("=" * 60)
print("Create Function - 4 - percentage()")
sublist=[23,45,34,23,23]
percentage(sublist)
print("=" * 60)

# Create Function - 5 - triangle()

# Define Function - triangle()

def triangle():
    Height = float(input("Enter your Height: "))
    Breadth  = float(input("Enter your Breadth: "))
    Area =  (Height * Breadth ) / 2
    print("Area of Triangle:",Area)

    Perimeter_flage = input(" Do you want to check Perimeter Y / N ")

    # Call Function - Perimeter() based on user input
    if Perimeter_flage.lower() == 'y':
        Perimeter()
    else:
        print("Thanks for your input")

# Define Function - Perimeter()
def Perimeter():
    Height1 = float(input("Enter your Height1: "))
    Height2 = float(input("Enter your Height2: "))
    Breadth  = float(input("Enter your Breadth: "))
    Perimeter = Height1 + Height2 + Breadth
    print("Perimeter of Triangle:",Perimeter)
    

# Call Function 
print("=" * 60)
print("Create Function - 5 - triangle()")
triangle()
print("=" * 60)

# Output
'''
============================================================
Create Function - 1 - Subfields()
Sub-fields in AI are: 
Machine Learning
Neural Networks
Vision
Robotics
Speech Processing
Natural Language Processing
============================================================

============================================================
Create Function - 2 - OddEven()
Enter a number: 4
Enter a number:  4
4 is Even Number
============================================================

============================================================
Create Function - 3 - Elegible()
Enter your age : 18
Enter you Gender:  male
Your Gender:  male
Your age:  18
bye
Input out of range. Given Age is 18 and Gender is MALE 
============================================================

============================================================
Create Function - 4 - percentage()
Subject1 = 23
Subject1 = 45
Subject1 = 34
Subject1 = 23
Subject1 = 23
Total :  148
Percentage :  29.6
============================================================

============================================================
Create Function - 5 - triangle()
Enter your Height: 3
Enter your Breadth: 4
Area of Triangle: 6.0
 Do you want to check Perimeter Y / N Y
Enter your Height1: 3
Enter your Height2: 4
Enter your Breadth: 45
Perimeter of Triangle: 52.0
============================================================
'''
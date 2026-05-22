
# Create a class and function, and list out the items in the list 

from email import message


class SubfieldsInAI:
    
    def Subfields(list1):
        
        print("Sub-fields in AI are: ")
        for i in list1:
            print(i)

    def OddEven(num1):
        print("Enter a number: ",num1) 
        if num1%2 == 1:
            message =  "{} is Odd Number".format(num1)
        else:
            message = "{} is Even Number".format(num1)
        return message
    
    def print_msg_first(msg):
        print("=" * 60)
        print(" " * 60) 
        print(msg)
    
    def print_msg_last():
        print(" " * 60)
        print("=" * 60)  

class ElegiblityForMarriage():
    def Elegible(gen,age):
        print("Your Gender: ",gen)
        print("Your age: ",str(age))
        gen=gen.upper()
        if age < 18 and (gen ==  "MALE" or gen == "FEMALE"):
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


class FindPercentage():
        
    def  percentage(sub):
        j = 1
        total = 0
        for i in sub:
            print("Subject{} = {}".format(j,i))
            total = total + i
        j += 1
        print("Total : ",total)
        pert = total/len(sub)
        print("Percentage : " ,pert )

class triangle():
    def triangle():
        Height = float(input("Enter your Height: "))
        Breadth  = float(input("Enter your Breadth: "))
        Area =  (Height * Breadth ) / 2
        print("Area of Triangle:",Area)

        Perimeter_flage = input(" Do you want to check Perimeter Y / N ")

    # Call Function - Perimeter() based on user input
        if Perimeter_flage.lower() == 'y':
            triangle.Perimeter()
        else:
            print("Thanks for your input")

# Define Function - Perimeter()
    def Perimeter():
        Height1 = float(input("Enter your Height1: "))
        Height2 = float(input("Enter your Height2: "))
        Breadth  = float(input("Enter your Breadth: "))
        Perimeter = Height1 + Height2 + Breadth
        print("Perimeter of Triangle:",Perimeter)


#Prepare List
list1 = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
SubfieldsInAI.print_msg_first("Create a class and function, and list out the items in the list ")
SubfieldsInAI.Subfields(list1)
SubfieldsInAI.print_msg_last()


SubfieldsInAI.print_msg_first( "Create a function that checks whether the given number is Odd or Even ")
num1 = int(input("Enter a number: "))
message = SubfieldsInAI.OddEven(num1)
print(message)
SubfieldsInAI.print_msg_last()


SubfieldsInAI.print_msg_first("Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female")

age = int(input("Enter your age : "))
gen = input("Enter you Gender:  ")
ElegiblityForMarriage.Elegible(gen,age)
SubfieldsInAI.print_msg_last()

SubfieldsInAI.print_msg_first("calculate the percentage of your 10th mark ")
sublist=[98,87,95,95,93]
FindPercentage.percentage(sublist)
SubfieldsInAI.print_msg_last()

SubfieldsInAI.print_msg_first("print area and perimeter of triangle using class and functions ")
triangle.triangle()
SubfieldsInAI.print_msg_last()


# Output
'''


============================================================
                                                            
Create a class and function, and list out the items in the list 
Sub-fields in AI are: 
Machine Learning
Neural Networks
Vision
Robotics
Speech Processing
Natural Language Processing
                                                            
============================================================
============================================================
                                                            
Create a function that checks whether the given number is Odd or Even 
Enter a number: 52452
Enter a number:  52452
52452 is Even Number
                                                            
============================================================
============================================================
                                                            
Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
Enter your age : 22
Enter you Gender:  male
Your Gender:  male
Your age:  22
ELIGIBLE
                                                            
============================================================
============================================================
                                                            
calculate the percentage of your 10th mark 
Subject1 = 98
Subject1 = 87
Subject1 = 95
Subject1 = 95
Subject1 = 93
Total :  468
Percentage :  93.6
                                                            
============================================================
============================================================
                                                            
print area and perimeter of triangle using class and functions 
Enter your Height: 32
Enter your Breadth: 34
Area of Triangle: 544.0
 Do you want to check Perimeter Y / N Y
Enter your Height1: 2
Enter your Height2: 4 
Enter your Breadth: 4
Perimeter of Triangle: 10.0
                                                            
============================================================

'''
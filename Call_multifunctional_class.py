
from multifuncational_Class import multifunctional 

#Prepare List
list1 = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
multifunctional.print_msg_first("Create a class and function, and list out the items in the list ")
multifunctional.Subfields(list1)
multifunctional.print_msg_last()


multifunctional.print_msg_first( "Create a function that checks whether the given number is Odd or Even ")
num1 = int(input("Enter a number: "))
message = multifunctional.OddEven(num1)
print(message)
multifunctional.print_msg_last()


multifunctional.print_msg_first("Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female")

age = int(input("Enter your age : "))
gen = input("Enter you Gender:  ")
multifunctional.Elegible(gen,age)
multifunctional.print_msg_last()

multifunctional.print_msg_first("calculate the percentage of your 10th mark ")
sublist=[98,87,95,95,93]
multifunctional.percentage(sublist)
multifunctional.print_msg_last()

multifunctional.print_msg_first("print area and perimeter of triangle using class and functions ")
multifunctional.triangle()
multifunctional.print_msg_last()

'''
output:

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
Enter a number: 5
Enter a number:  5
5 is Odd Number
                                                            
============================================================
============================================================
                                                            
Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
Enter your age : 45
Enter you Gender:  Female
Your Gender:  Female
Your age:  45
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
Enter your Height: 4
Enter your Breadth: 5
Area of Triangle: 10.0
 Do you want to check Perimeter Y / N N
Thanks for your input
                                                            
============================================================

'''
class multifunctional:

    def print_msg_first(msg):
        print("=" * 60)
        print(" " * 60) 
        print(msg)
    
    def print_msg_last():
        print(" " * 60)
        print("=" * 60) 

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
    
    def triangle():
        Height = float(input("Enter your Height: "))
        Breadth  = float(input("Enter your Breadth: "))
        Area =  (Height * Breadth ) / 2
        print("Area of Triangle:",Area)

        Perimeter_flage = input(" Do you want to check Perimeter Y / N ")

    # Call Function - Perimeter() based on user input
        if Perimeter_flage.lower() == 'y':
            multifunctional.Perimeter()
        else:
            print("Thanks for your input")

# Define Function - Perimeter()
    def Perimeter():
        Height1 = float(input("Enter your Height1: "))
        Height2 = float(input("Enter your Height2: "))
        Breadth  = float(input("Enter your Breadth: "))
        Perimeter = Height1 + Height2 + Breadth
        print("Perimeter of Triangle:",Perimeter)
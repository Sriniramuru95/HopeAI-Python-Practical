"""
Extra Assignement question Python 2
"""
#============================
# print 0 to 20 by using range
#============================

for i in range(21):
    print(i)

#============================
# print range 10 to 20
# ============================
 
for i in range(10, 21):
    print(i,end=" ")   
# Print number of items in the list by using 'len' 
list1=[10, 20, 14, 55, 43, 87, 76]
print("\nNumber of items in the list is:",len(list1))

#============================
#Artificial Intelligence"
#============================

string1="Artificial Intelligence"
for i in string1:
    print(i)

#============================
"""
-Your Name- -Your Age- -Your Profession- 
"""
#============================

list2=["Name","Age","Profession"]
list3=[]
j = 0
for i in list2:
    list3.append(input(("Enter the Your " + list2[j] + ": ")))
    j += 1
j=0
for i in list3:
    print("Your "+ list2[j] + " is "+list3[j])
    j+=1

print("Your Name is",list3[0],", Your Age is",list3[1],"and Your Profession is",list3[2])


#============================
#Tuple
#============================
#Create a tuple with 5 elements and print the tuple

tuple1=(1, 'Welcome', 2, 'Hope') 
print(tuple1)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'HOPE')
tuple3 = (Tuple1,Tuple2)   
print(tuple3)

#============================
# print Odd Numbers in the list
#============================

Tuple1 = (20,10,16,19,25,1,276,188) 
for i in Tuple1:
    if i % 2 != 0:
        print( "{} is odd ".format(i))

#============================
# print Even numbers in the list
#============================

for i in Tuple1:
    if i % 2 == 0:
        print( "{} is even ".format(i))

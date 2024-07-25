#----------------------- Control Flow Satatements In Python -------------------------
#Types of control flow statement {1 conditional Statement, 2 Transfer Statement, 3 Iterative Statement}
# Conditional Statement types {1 if statement,2 if-else statement,3 if-elif-else statement}
#Transfer Starement types{1 continue statement, 2 break statement, 3 pass statement }
#Iterative Statement types{1 for loop, 2 while loop }
#collection{1 string, 2 list, 3 tuple, 4 dist}
#-------------syntax of if statement in python---------------------------------
x=input("Enter your age :")# input function by-default string datatype return karta hai
print(type(x))
# we can use  complex,float instad of int to get the correct type of return
y=int(input("Enter your age :"))
print(type(y))
x=int (input("Enter your age :"))
if x>=18:
    print("You are Eligble to vote")
    print("Welcome to first page of python")
    print("thank you for visiting")
if x>=60:
    print("Visit counter no 1")
if x>=40:
    print("Visit counter no 2")
if x>=30:
    print("Visit counter no 3")       
    print(x)
 #-------------syntax of if-else statement in python---------------------------------
y=int(input("Enter Your Age"))
if y >=18:
        print("you are eligble to vote")
else:
        print("you are not eligble to vote")
#-------------syntax of if-elif-else statement in python---------------------------------   
z=int(input("Enter your age :"))
if z>=60:
    print("Visit Counter 1")
elif z>=40:
     print("Visit Counter 2")
elif z>=20:
     print("Visit Counter 3") 

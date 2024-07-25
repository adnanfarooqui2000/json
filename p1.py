print("Good Morning Sunshine")
x=10
y=10
print(id(x))
print(id(y))
#single dot . means current Directory/Folder
#double dot .. means previous Directory/Folder
#../../../.. = 3 Folder
#cd Stands for change Directory
#python -m py_compile p1.py = Machine Language    
#memory are used to call by reference
# rules to create variables & identifiers
#(Variables cannot Start with Number like 012345)
#(Variables can Start with Alphabets Like A To Z,a to z, _)
#{Properties Of Variables}1(Datatype),2(Scope),3(Memory Location)
#python cannot write like this Adnan Farooqui=89
#python can write like this adnan-farooqui=89
tate=10
#python is case Senstive language 
age=78
print(age)
x,y,z=12,14,16
print(x)
print(y)
print(z)
x=y=z=125
print(x)
print(y)
print(z)
import keyword
#in-build function in Python 
# 1 print() 2 type() 3 id() 4 input() 5 max() 6 min() 7 len() 8 ord() 9 chr() 10 str()
#input() are used to take input from the user
name= input("Enter Name :")
age= input("Enter Age :")
#print()are used to print the value on the screen
print("Name :",name)
print("Age :",age)
#type casting are used to convert one datatype into another 
#int(),chr(),str(),list(),tuple(),dict(),set(),oct(),hex(),bin(),float(),complex(),
#x = "Sana"
print(int(x))
x=(10,20,30,40,50,)
print(list(x))
print(set(x))
x={10,20,"Sana",30,10,20}
print(tuple(x))
print(set(x))
print(type(tuple(x)))
print(type(list(x)))
print(type(list(x)))
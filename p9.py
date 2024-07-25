#------------Syntax Iterative Statement for loop, while loop --------------------------
#NOTE :in python (++,--) oprator doesn't Support in -----------------------------------
#NOTE : for loop Doesn't support increment /decrement oprator in python only while loop support 
#------------------- for loop-------------------------------------------------------- 
#------in-build function range(start,end,step)--------------------------------------------
#  with the help of range we can genrate collection in python
x=range(5)
print(x)
print(list(x))
print(tuple(x))
print(set(x))

y=range(2,50,2)
print(list(y))

z=range(2,50,-2)
print(list(z))

for i in range(1,11):
    print(i)
    print("HELLO")
    print("WELCOME")
#print even number using for loop
for i in range(2,21,2):
    if i<=18:
        print(i,end=",")
#print odd number using for loop
for i in range(2,20,):
    if i<=18:
        print(i,end=",")
    else:
        print(i) 
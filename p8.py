#------------Syntax Iterative Statement for loop, while loop --------------------------
# NOTE :in python (++,--) oprator doesn't Support in loop
#------------------- while loop-------------------------------------------------------- 

x=1    # INITALIZE
while (x<=10):  # CONDITION
 print(x)
 x=x+1  # INCREMENT/DECREMENT
 
n=20
n=int(input("Enter Any Digit :"))
i=1
while i<=20:
    if i<=(n-1):
        print(i,end=",")
    else:
        print(i)
    i=i+1

 #------------------even Number-------------------------------------------------------------
z=2
while z<=10:
    if(z%2==0):
        print(z,end=",")
    z=z+1
     #------------------odd Number-------------------------------------------------------------
z=2
while z<=12:
    if(z%2==1):
        print(z,end=",")
    z=z+1

#----------------------Sum Number-------------------------------------------------------------
n=10
sum=0
i=1
while(i<=n):
    i=i+1
    sum=sum+1 
    print(sum)
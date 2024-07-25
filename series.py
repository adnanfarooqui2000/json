#=================== printiing series of 1 to 10 number sum =======================================
x=1
y=10
sum=0
for x in range(1,11):
  sum=sum+x
  if x<=y-1:
    print(x,end=",")
  else:
    print(sum)
# #================= Armstrong Number============================================================

# #================= Prime Number================================================================
x=int(input("Enter any number : "))
count=0
i=1
while i<x:
    if x%i==0:
       count=count+1
    i=i+1
if count>1:
     print("this is not a prime number")
else:
     print("this is a prime number") 
#================================= right Pattern * ========================================================
n=int(input("Enter number of rows : "))
i=1
while i<=n:
    print(i*'*')
    i=i+1
#================================= right Pattern * opposite printing ========================================================
n=int(input("Enter number of rows : "))
i=1
while i<=n:
    print(i*(n+i)*'*')
    i=i+1
# ========================================= triangle pattern * =========================================
n=int(input("Enter number of rows : "))
i=1
while i<=n:
    print((n-i)*' '+i*'* ')
    i=i+1
#========================================= left pattern * =========================================
n=int(input("Enter number of rows : "))
i=1
while i<=n:
    print((n-i)*' '+i*'*')
    i=i+1
#========================================= odd triangle pattern * =========================================
n=int(input("Enter number of rows : "))
i=1
while i<=n:
    print((n-i)*' '+(2*i-1)*'*')
    i=i+1
#========================================= even triangle pattern * =========================================
n=int(input("Enter number of rows : "))
i=1
while i<=n:
    print((n-i)*' '+(2*i)*'*')
    i=i+1
#======================================= Diamond shape pattern * ==========================================

# """ 
# =========================== function in Python ===============================================
# # block of code it is call code
# #y=10
# #sum=x+y
# #print(sum)
# #a(10)
# #print(y)
# #y=20
# #def add(x):
#   #   global y
#  #    y=10
# #sum=x+globals()['y'] # with globals()['']we use for global variable value
# # global is a in-bulid method in python not a in build function 
# #print(sum)
# #add(10)

#  print(y)types of function (1 in-build function , 2 user-defined function)
#  (int,float,str,sum,max,min,complex and so on are in-build function)
#  user-define function are create by user 
#  syntax of user define funcrion (def function name required (parameter): optional
#                                           body(required)
#                                          return    optional       )
#                                  function name required (agrumrnt) optional
# """
# def add(x,y):
#      z=x+y
#      print(z)
# x=add(10,20)
# print(x)
# p=int(input("Enter First Digit :"))
# q=int(input("Enter Secand Digit :"))
# print(add(p,q))
# # print(r)
# def plus(a=0,b=0):
#      c=a+b
#      return c
# x=int(input("enter digit :"))
# y=int(input("enter digit :"))
# p=plus(x)
# p=plus(y)
# print(p)
# """
#  difference between function & loop
#  loop                function
#  1 we cannot reuse      we can reuse function in 
#  loop in program        program.
#  2 we cannot call       we have to call function in
#  loop in program        program then it will execute.
# # """  
# def square(x):
#      square=x*x
#      return square
# z=int(input("enter any digit : "))
# print("hello")
# print("welcome")
# p=square(z)
# print(p)  
# def add(*x):
#     add=0
#     for i in x:
#         add=add+i
#         print("add=",add)
# add(10,20)
# add(10,20,30,40,50,60,70,80,90,100)
# def emp_data(**data):
#     for i,j in data.items():
#         print(i,"=",j)
# emp_data(Name= "Adnan Farooqui", city="Bhopal")
# # # ====================== function Variables in python =======================================================
# y=10
# def add(x):
#     sum=x+y
#     print(sum)
# add(10)
# print(y) 
# def a(x):
#  y=20
# def add(x):
#     global y
#     y=10
#     sum=x+y
#     print(sum)
# y=30
# add(10)
# print(y)
# x=10
# print(x)
# print("Hello")
# x=20
# print(x)
# print("Welcome")
# y=10
# def add(x):
#     global y
#     y=20
#     sum= x+y
#     print(sum)
# add (x)
# print(y)
# y=30
# print(y)
# # # =============================== create calculator using function in python =======================================
# def add(x,y):
#   return x+y
# def sub(x,y):
#  return x-y
# def multi(x,y):
#  return x*y
# def div(x,y):
#  return x/y
# def mode(x,y):
#  return x%y
# def mm(x,y):
#     return x**y
# def dd(x,y):
#     return x//y
# print("Please select operator =>\n","+\n","-\n","*\n","/\n","%\n","**\n","//\n")
# while True:
#   select = int(input("Select operations form 1, 2, 3, 4, 5, 6, 7 :"))
#   p=int(input("Enter First Digit :"))
#   q=int(input("Enter Secand Digit :"))
#   if select == 1:
#          print(p+q)
#          add(p,q)   
#   elif select == 2:
#         print(p-q)
#         sub(p,q)
#   elif select == 3:
#          print(p*q)
#          multi(p,q)
#   elif select == 4:
#          print(p/q)
#          div(p,q)
#   elif select == 5:
#          print(p%q)
#          mode(p,q)
#   elif select == 6:
#          print(p**q)
#          mm(p,q)
#   elif select == 7:
#          print(p//q)
#          dd(p,q)
#   else:
#          print("Invalid Input")
#          break
# # #==========================================================================
# my_list=[10,20,30,40,50]
# new_list=[]
# for i in my_list:
#     x=i+5
#     new_list.append(x)
# print(new_list)
# #====================== Syntax of map function ====================================
# #========================map(function name , collection)==========================
# list=[5,10,15,20,25]
# def add(n): 
#    if n%2==0:
#       return'Even number'
#    else:
#       return 'Odd Number'
# x=tuple(map(add,list))
# print(x)
# # #========================filter Function ==========================================
# my_list=[10,15,20,25,30,35,40,]
# def add(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# x=filter(add,my_list)
# x=tuple(filter(add,my_list))
# print(x)
# """
# ======================== Lamda Function============================================
# lamda (Argument): expression
# """
# x=lambda Name:print("Hello",Name)
# x=("Adnan Farooqui")
# y=input("Enter your name : ")
# x(y)
# x=lambda x,y:x+y
# p=int(input("enter First number :"))
# q=int(input("Enter Secand Number :"))
# print(x(p,q))
# my_list=[2,4,6,8,10]
# x=list(map(lambda x : x**2,my_list))
# print(x)
# my_list=[1,2,3,4,5,6,7,8,9,10]
# x=list(filter(lambda x:x%2==0,my_list))
# print(x)
# #=============================== reduce Function ==============================================
# # ===========(from funtools import reduce) use for importing reduce function in python============
# from functools import reduce
# my_list=[1,5,98,5,85,86,7,8]
# def max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# x=reduce(max,my_list)
# print(x)

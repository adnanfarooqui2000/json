# Tuple 
my_tuple=(1,2,3,4,5,6,7,8,9,10,)
print(my_tuple)
print(my_tuple.count(100))
print(my_tuple.index(7))
print(len(my_tuple))
print(max(my_tuple))
print(min(my_tuple))
print(sum(my_tuple))
print(id(my_tuple))
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[1:4])
x=list(my_tuple)
print(type(x))
x[0]=2
print(x)
y=tuple(x)
print(type(y))
print(y)
print(my_tuple.count(2))
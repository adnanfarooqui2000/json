#dict
x=dict()
print(type(x))
x['Full Name']='Adnan Farooqui'
print(x)
print(x['Full Name'])
x['Age']=23
print(x)
x['Full Name']='Aslihaan'
print(x)
print(len(x))
#print(max(x)) Don't use max in dict of python
#print(min(x)) Don't use min in dict of python
my_dict={'Full Name':'Adnan Farooqui','Age':23,'City':'Bhopal'}
print(my_dict)
#my_dict.clear()
x=my_dict.keys()
print(x)
print(my_dict.values())
print(my_dict.items())
print(my_dict.pop('Age'))
print(my_dict)
del my_dict['City']
print(my_dict)
print(my_dict.copy())
print(my_dict.get('Full Name'))
class Student:
 ''' This class is develop by Neeraj for demo'''
def __init__(self,name,roll,marks,city):
         self.name = name
         self.roll = roll
         self.marks = marks
         self.city = city
def display(self):
  print("my name is", self.name)
  print("my roll no is", self.roll)
  print("my marks is", self.marks)
  print("my city is", self.city)
stu1 = Student("Neeraj",101,"90","Bhopal")
stu2 = Student("Rahul",102,"92","Indore")
print(stu1.name)
print(stu2.name)
stu1.display()
stu2.display()
print(stu1.__dict__)
print(stu2.__dict__)
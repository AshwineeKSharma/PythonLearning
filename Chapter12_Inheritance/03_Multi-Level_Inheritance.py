#       Multi-Level Inheritance
#------(Multi-Level Inheritance) ------->Base CLass -------> Derived Class1-------> Derived Class2. so on..
#i.e Child derives from Base Class and that child itself becomes base(Parent) class for another child class. so on..
#---------------------------------------------------------------------------------------------------





class Employee:
    Mcompany="Google"
    Ecode=3375


class Freelancer:
    Fcompany="Youtube"
    Level= 7

class Programmer(Employee,Freelancer):
    Language="Python"


class Student(Programmer):
    name="Ashwinee Kumar Sharma"
    age=30


s=Student()
print(f"{s.name} of age {s.age} is a {s.Language} programmer of level {s.Level} doing Freelancing in {s.Fcompany} and Works in {s.Mcompany} with Code No : {s.Ecode}")












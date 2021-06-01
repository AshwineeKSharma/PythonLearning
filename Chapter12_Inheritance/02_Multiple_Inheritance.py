#       Multiple Inheritance
#-----------------------(Multiple Inheritance) --------->(Multiple)Base CLasses ---------> Derived Class 
#i.e Child class Inherits from Multiple parent class
#---------------------------------------------------------------------------------------------------


class Employee:
    Mcompany="Google"
    Ecode=3375


class Freelancer:
    Fcompany="Youtube"
    Level= 7

class Programmer(Employee,Freelancer):
    name="Aashman"


p=Programmer()

print(f"Name is {p.name} and does Freelancing in {p.Fcompany} with level {p.Level} and Works at {p.Mcompany} having code {p.Ecode} ")


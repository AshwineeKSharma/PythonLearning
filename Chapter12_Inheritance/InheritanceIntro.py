# Inheritance is the process of Inheriting the base(Parent) Class by the derived(Child) class.
# There are 3 different types of Inheritance, they are:
#--------------------------------------------------------------------------------------------------------
# 1) Single Inheritance ---------> Base CLass ---------> Derived Class 
# i.e Child class only Inherit single parent class
#---------------------------------------------------------------------------------------------------------
# 2) Multiple Inheritance
#-----------------------(Multiple Inheritance) --------->(Multiple)Base CLasses ---------> Derived Class 
#i.e Child class Inherits from Multiple parent class
#---------------------------------------------------------------------------------------------------------
#       Multi-Level Inheritance
#------(Multi-Level Inheritance) ------->Base CLass -------> Derived Class1-------> Derived Class2. so on..
#i.e Child derives from Base Class and that child itself becomes base(Parent) class for another child class. so on..
#----------------------------------------------------------------------------------------------------------





class Employee:
    company="Microsoft"


    def showDetails(self):
        print("This is Employee Details from Employee Class.")






class Programmer(Employee):
    language="Python"

    def getLanguage(self):
        print(f"The Language is {self.language}")


E=Employee()
P=Programmer()
E.showDetails()
P.showDetails()
print(P.company)



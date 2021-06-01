#------------ Single Inheritance -------------------------------------------------------------------------
#  Single Inheritance ---------> Base CLass ---------> Derived Class 
# i.e Child class only Inherit single parent class
#---------------------------------------------------------------------------------------------------




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
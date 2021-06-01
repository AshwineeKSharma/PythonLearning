# WAP to create a class for storing information of few programmers working at Microsoft. 





class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,subunit):
        
        self.name=name
        self.salary=salary
        self.subunit=subunit

    def getDetail(self):
        print(f"The name of the {self.company} Programmer is : {self.name}")
        print(f"The Salary of {self.name} is : {self.salary}")
        print(f"The SubUnit of {self.name} is : {self.subunit}")


name=input("Enter Your Name : ")
salary=input("Enter your Salary : ")
subunit=input("Enter the name of your SubUnit : ")

ash= Programmer(name,salary,subunit)
ash.getDetail()






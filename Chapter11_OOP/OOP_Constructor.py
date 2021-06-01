class Employee:

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Constructor is Called Here.!!")



    def getSalary():
        pass

    def getDetail(self):
        print(f"The name of the Employee is {self.name}")
        print(f"The Salary of  {self.name} is {self.salary}")
        print(f"The Subunit of {self.name} is {self.subunit}")




ashwin=Employee("Ashwinee Kumar Sharma",100000,"Youtube")
ashwin.getDetail()





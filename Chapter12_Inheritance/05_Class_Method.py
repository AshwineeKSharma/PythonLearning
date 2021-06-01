#Class Method is a method which is bound to the class and not the object of a class.
#@classmethod is used as a decorator is used to create a class method.




class Employee:
    company="Fountain"
    salary=7000
    location="Morang"

    # def changeSalary(self,sal):
    #     self.salary=sal
    #     self.__class__.salary=sal       
    @classmethod                # used to change or add class attributes
    def changeSalary(cls,sal):
        cls.salary=sal
              


e=Employee()
print(e.salary)
e.changeSalary(50000)
print(e.salary)
print(Employee.salary)


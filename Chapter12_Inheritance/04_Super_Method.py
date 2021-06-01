# super() method allows to access the methods of a super class in the derived class.
# super().__init__()-----------------> to call the constructor of base class


#Class Method is a method which is bound to the class and not the object of a class.
#@classmethod is used as a decorator is used to create a class method.



class Person:
    country="Nepal"
    def getStatus(self):
        print(" Person : I am Feeling Alive!!!")

class Employee(Person):
    company="Mustang"

    def getSalary(self):
        
        print(f"salary is {self.salary}")

    def getStatus(self):
        super().getStatus()   # returs the value of getStatus from Person Class
        print("Employee : I am having Job that's reassuring!!")


class Programmer(Employee):
    company="Vianet"

    def getStatus(self):
        print(" Programmer: Python is relatively easier to learn than other Language.")
        super().getStatus()   # returs the value of getStatus from Employee Class



    
p= Person()
p.getStatus()
e=Employee()
e.getStatus()
pr=Programmer()
pr.getStatus()







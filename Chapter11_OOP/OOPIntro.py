# Problem solving Approach with the help of object can be defined as object oriented programming.
# OOP gives more emphasis on code reusability. DRY(Do not Repeat Yourself) Principle


# Class : Class can be defined as the template for objects and its behaviour with various codes implementation.
# Object : Object can be defined as the real world entities with it's data, attributes and behaviour.


# Syntax for creating class
# class Employee:                     
    # Methods(Functions) and Variables







class Employee:
    name="Ashwinee Kumar Sharma"
    company="Google"
    age=30
    Address="Lalitpur-25"

    def getSalary(self):
        print(f"The Salary for {self.name} working in {self.company} is {self.salary} ")


ashwin=Employee()
ashwin.salary=500000
ashwin.getSalary()


# Static Method can be initialised using @staticmethod Keyword.







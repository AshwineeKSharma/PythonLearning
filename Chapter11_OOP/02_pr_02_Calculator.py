# Write a class Calculator capable of finding Square,Cube and Squareroot of a number. 


class Calculator:
    def __init__(self,number):
        self.number=number



    def Calculation(self):
        sq= self.number*self.number
        cube=self.number*(self.number*self.number)
        sqr=self.number*0.5

        print(f"Square of {self.number} is {sq}")
        print(f"Cube of {self.number} is {cube}")
        print(f"Squareroot of {self.number} is {sqr}")



number=int(input("Enter your Number here :"))

ash=Calculator(number)
ash.Calculation()



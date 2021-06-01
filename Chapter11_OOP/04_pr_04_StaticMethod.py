# Add a static method in problem 2 to greet the user with hello. 




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

    @staticmethod
    def greetUser():
        print("**************************Hello User*************************************** \n")




number=int(input("Enter your Number here :"))

ash=Calculator(number)
ash.greetUser()
ash.Calculation()


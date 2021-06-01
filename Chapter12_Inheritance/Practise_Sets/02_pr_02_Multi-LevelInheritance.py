# Create a class pets from a class animals and further create a class dog from class pets.
# Add a method Bark() to class Dog. 

class Animals:
    animalType="Mammal"



class Pets(Animals):
    color="White"


class Dog(Pets):
    @staticmethod
    def Bark():
       print("This is Bark Method")



d=Dog()
d.Bark()




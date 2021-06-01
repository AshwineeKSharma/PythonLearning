# Operator overloading is done using dunder method i.e method containing doubleunderscore.
# other dunder method __str__  used to set what gets displayed upon calling str(obj) 
#  __len__ used to set what gets displayed upon calling __len__() or len(obj)


class Number:
    def __init__(self,num):
        self.num=num

# ---------------------------- For Addition Operator----------------------------------------------------
    def __add__(self,num2):
        self.num2=num2
        print("Let's Add two Numbers.!!! ")
        return self.num+num2.num

#--------------------------------------------------------------------------------------------------------



# ---------------------------- For Multiplication Operator------------------------------------------------
    def __mul__(self,num2):
        self.num2=num2
        print("Let's Multiply two Numbers.!!! ")
        return self.num*num2.num


#-----------------------------------------------------------------------------------------------------------  



# ---------------------------- For substraction Operator-----------------------------------------------------
    def __sub__(self,num2):
        self.num2=num2
        print("Let's Subtract two Numbers.!!! ")
        return self.num-num2.num


#-----------------------------------------------------------------------------------------------------------    


# ---------------------------- For Division Operator--------------------------------------------------------
    def __truediv__(self,num2):
        self.num2=num2
        print("Let's Divide two Numbers.!!! ")
        return self.num/num2.num


#-----------------------------------------------------------------------------------------------------------   



# ---------------------------- For Floor Division Operator--------------------------------------------------------
    def __floordiv__(self,num2):
        self.num2=num2
        print("Let's floor Divide two Numbers.!!! ")
        return self.num//num2.num


#----------------------------------------------------------------------------------------------------------- 
    def __str__(self):
        return f"Decimal Number : {self.num}"        


#---------------------------------------------------------------------------------------------------------

    def __len__(self):

        return 1

n= Number(9)
print(n)
print("The length of given Number is : {}".format(len(n)))



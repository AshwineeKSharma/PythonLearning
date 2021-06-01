# A Function can be defined as a group of statement(Codes) preforming the specific task.
# Functions usually "take in" data, process it, and "return" a result.
# Once a function is written, it can be used over and over and over again. 
# Functions can be "called" from the inside of other functions.
# E.g. Func() --------> This is a function Call.
# There are two types of Function in Python. 1) Built-in function.  2) User Defined Function. 

def percent(Marks):         # Defining The Function inside the program(Internal Function) with
    return(sum(Marks)/600)*100  # return Value


Marks=[77,80,75,95,66,90]
Marks2=[80,85,87,95,60,92]

# precentage=(sum(Marks)/600)*100

percentage1=percent(Marks)
percentage2=percent(Marks2)

print(f"The Precentage of 1st student is  :{percent(Marks)} ")
print(f"The Precentage of 2nd student is  :{percentage2} ")







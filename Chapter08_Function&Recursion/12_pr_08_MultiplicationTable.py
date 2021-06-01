# WAP to print Multiplication Table of Given Number using Function 


def Multiplication_Table(num):
    for i in range(1,11):
        mult= num*i
        print(f"{num} X {i} = {mult}")
    return()



num=int(input("Enter The Number For Multiplication Table : "))

Multiplication_Table(num)

    


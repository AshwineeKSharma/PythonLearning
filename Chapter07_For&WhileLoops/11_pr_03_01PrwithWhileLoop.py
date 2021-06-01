# WAP to print the Multiplication Table of a given number using while Loop.


num1=int(input("Enter a Number For Multiplication Table : "))

i=1
while(i<=10):
    Mult= num1*i
    # print(f"{num1} X {i} = {Mult}")
    print("{} X {} = {}".format(num1,i,Mult))
    i+=1

    

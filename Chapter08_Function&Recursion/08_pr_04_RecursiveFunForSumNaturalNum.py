# WAP to find the sum of N natural Number using Recursion


def sumOfNatural(num):
    
    if(num==1 or num==0):
        return 1
    return num+ sumOfNatural(num-1)



num=int(input("Enter A Number : "))

print(f"The Sum of Natural Number Upto {num} is {sumOfNatural(num)}")



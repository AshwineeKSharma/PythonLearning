# WAP to calculate the factorial of a given number using For Loop. 
# n!= 1 x 2 x 3 x 4 x ............. x n
# 5!= 1 x 2 x 3 x 4 x 5


num=int(input("Enter Your Number for Factorial : "))
fact=1
for i in range (1,num+1):
    fact= fact*i
print(f"The Factorial Of {num} is {fact}")


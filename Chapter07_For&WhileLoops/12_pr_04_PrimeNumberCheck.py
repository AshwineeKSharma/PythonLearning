# WAP to find if the given number is prime or not 

num1=int(input("Enter The Number You Want To Check : "))
prime=True

for i in range(2,num1):
    if(num1%i==0):
        prime=False
        
if prime:
    print("The Number You Entered is Prime")

else:
    print("The Number You Entered is not Prime.")




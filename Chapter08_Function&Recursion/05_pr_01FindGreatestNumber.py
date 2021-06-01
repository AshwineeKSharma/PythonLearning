# WAP to Find the greatest of three numbers using Function 

def greatNum(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print(f"First Number {num1} you Entered is greater than {num2} and {num3}")

    elif(num2>num1 and num2>num3):
        print(f"Second Number {num2} you Entered is greater than {num1} and {num3}")

    elif(num3>num1 and num3>num2):
        print(f"Third Number {num3} you Entered is greater than {num1} and {num2}")

    else:
        print("Are any Number Equal ?")

   


num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))
num3=int(input("Enter Third Number : "))

greatNum(num1,num2,num3)
    
    


# Try with else is used when we have to execute some piece of code when try block is successful.


try:
    i=int(input("Enter a number : "))
    c= 1/i

except ValueError as e:
    print("Value Error Occured")
    # print(e)
    print("Please Enter the Valid Integer")

except ZeroDivisionError as e:
    print("ZeroDivisionError Occured")
    # print(e)
    print("Number can't be divisible by zero(0)")


except Exception as e:
    print(e)

else:
    print("The program executed successfully !!! ")



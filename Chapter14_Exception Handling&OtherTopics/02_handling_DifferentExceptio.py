try:
    a= int(input("Enter a number : "))
    c= 1/a
    print(c)
    
except ValueError as e:
    print("Value Error Occured")
    # print(e)
    print("Please Enter the Valid Integer")

except ZeroDivisionError as e:
    print("ZeroDivisionError Occured")
    # print(e)
    print("NUmber can't be divisible by zero(0)")

except Exception as e:
    pass




print("Thank you.")


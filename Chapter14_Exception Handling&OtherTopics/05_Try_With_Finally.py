# Try with Finally 
# Python offers the a clause "Finally" which executes the block of codes
# irrespective of the exception occured.
 



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
    exit()


except Exception as e:
    print(e)

else:
    print("The program executed successfully !!! ")

finally:
    print("This is Print from Finally Block.")

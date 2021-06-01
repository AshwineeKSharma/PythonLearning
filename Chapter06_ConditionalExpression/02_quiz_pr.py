# WAP to print "Yes" if the age entered by the user is greater than 18

age=int(input("Enter Your Age : "))

if(age>18):
    print("Yes your age is greater than 18")

elif(age<18):
    print("You are underaged.")

else:
    print("Your age is 18.")
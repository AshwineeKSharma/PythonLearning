# WAP to find whether the given username contains less than 10 character or not 


UserName=input("Please Enter Your Username : ")
ucount=len(UserName)

if(ucount<10):
    print("The UserName You Entered is Less Than 10 Characters")

else:
    print("The UserName You Entered is More Than 10 Characters")


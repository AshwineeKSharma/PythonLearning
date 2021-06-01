#  Exception handling is the process of responding to the occurrence of exceptions 
#  – anomalous or exceptional conditions requiring special processing – during the execution of a program.
# 1)try-except   2) try-except- else    3) try-finally

# Syntax:------------------------------------------------------------------------------------------------------
# try:    
#     #block of code     
    
# except Exception1:    
#     #block of code    
    
# except Exception2:    
#     #block of code    
    
# #other code  
# ------------------------------------------------------------------------------------------------------------------ 
while(True):
    
    print("Enter Q/q to quit")
    a= input("Enter a number : ")

    if a =='q':
        break
    try:                                # Try Block Statement
        a= int(a)


        if a>6:
            print(f"The number {a} is greater than 6. ")

        elif a<6:
            print(f"The number {a} is less than 6.")


    except Exception as e:                  # Except Block Statement
        print("You Entered the string in place of Integer number.")

print("Thanks for playing this game!!!")












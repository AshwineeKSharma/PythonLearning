# WAP to Calculate the Grade of a Student from the marks obtained using following Scheme. 
# 90-100  : A +
# 80-90   : A
# 70-80   : B
# 60-70   : C
# 50-60   : D
# <50     : F


Marks= int(input("Enter Your Total Marks Obtained :  "))

if(Marks>90 and Marks<=100):
    print("Congratulation Your Grade is A+")

elif(Marks>80 and Marks<=90):
    print("Congratulation Your Grade is A")


elif(Marks>70 and Marks<=80):
    print("Congratulation Your Grade is B")


elif(Marks>60 and Marks<=70):
    print("Congratulation Your Grade is C")


elif(Marks>50 and Marks<=60):
    print("Congratulation Your Grade is D")


elif(Marks<50):
    print("Sorry!!! You Are Failed and Your Grade is F")


else:
    print("Your Marks Exceeded The Total Marks Enter Again!!")
# WAP to find whether a student is pass or fail based on the marks obtained on three (3) subjects
# Assuming that it requires 40% total and at least 33% in each subject to pass and get the
# Marks input from the user.



mt=int(input("Enter Your Marks in Maths out of 100 : "))
sci=int(input("Enter Your Marks in Science out of 100 : "))
eng=int(input("Enter Your Marks in English out of 100 : "))

omtp=(mt/100)*100    # percentage of Marks obtained in Maths
oscip=(sci/100)*100  # percentage of Marks obtained in Science
oengp=(eng/100)*100  # percentage of Marks obtained in Maths

tmksp=((omtp+oscip+oengp)/300)*100  # Percentage of total marks obtained.

if(omtp>=33 and oscip>=33 and oengp>=33 and tmksp>=40):
    print("Congratulation You Passed Your Examination")


else:
    print("We are sorry to say you failed!! better luck next time.")






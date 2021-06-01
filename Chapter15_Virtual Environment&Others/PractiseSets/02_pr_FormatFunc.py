# WAP to input name, marks and phone number of a student and format it using format function as below.

# "The name of student is something, his marks are something and phone number is something. "

name=input("Enter the name of the Student : ")
marks= int(input("Enter the Total Marks of the Student : "))
phno=int(input("Enter the Phone Number :  "))

print("The name of the student is {}, Total marks obtained by student is {} and Phone Number is {}".format(name,marks,phno))

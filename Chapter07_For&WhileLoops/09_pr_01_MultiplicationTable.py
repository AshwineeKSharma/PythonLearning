# WAP to print the Multiplication Table of a given number using For Loop. 

num=int(input("Enter The Number For Multiplication Table : "))

for i in range(1,11):
    mult= num * i 
    print("{} X {} = {}".format(num,i,mult))
    # print(f"{num} X {i} = {mult}")      # F string Can be used for Simplification of task.
    i+=1

    


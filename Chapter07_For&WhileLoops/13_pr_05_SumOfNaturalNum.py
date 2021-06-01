# WAP to print the sum of first Natural numbers using while loop 


num=int(input("Enter The Natural Number for calculating Total Sum Upto it :  "))


if(num<0):
    print("Enter Positive Number")


else:
    sum=0

    while(num>0):
        sum+=num
        num-=1
    
    print(f"The Total Sum Is :  {sum}")










# WAP to print the multiplication table of n using for loop in reversed order 


num= int(input("Enter A Number Here : "))

for i in range(10,0,-1):
    mul=num*i
    print(f"{num} X {i} = {mul}")
    i-=1
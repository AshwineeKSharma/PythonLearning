# Write a list comprehension to print the list which contains the multiplication table 
# of a user entered number. 


unum=int(input("Enter Your Number : "))

table=[unum*i for i in range(1,11)]

print(table)

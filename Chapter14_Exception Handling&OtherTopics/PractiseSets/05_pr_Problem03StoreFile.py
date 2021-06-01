# Store the multiplication table generated in problem 03 in a file named table.txt 




unum=int(input("Enter Your Number : "))

table=[unum*i for i in range(1,11)]

print(table)

with open("table.txt","a") as fil:
    fil.write(str(table))
    fil.write("\n")
    




# WAP to find out the maximum of the number in a list using reduce function. 
from functools import reduce    #-----------> Importing reduce from functools...


l1=[4,5,2,3,8,57]

mx= reduce(max,l1)
print(f"the maximum number in the given list is : {mx}")






sum= lambda a,b: a+b

li1=[2,4,6,8,10,12,14,16,18,20]

val=reduce(sum,li1)

print(val)



# Map applies a function to all the items in an input_list. 
# can be used wih lambda function.
# syntax:-----------> map(function,Input_list)



def square(num):
    return num*num



l1=[2,4,6,8]
l2=[]

# Method 1: 

for item in l1:
    l2.append(square(item))

print(l2)


# Method 2:

print(list(map(square,l1)))     #---------------> Type casting into list









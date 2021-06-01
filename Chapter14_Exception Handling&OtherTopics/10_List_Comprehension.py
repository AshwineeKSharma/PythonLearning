# A list comprehension is a syntactic construct available in some
# programming languages for creating a list based on existing lists.
# List comprehension is an elegant way to define and create lists based 
# on existing lists. List comprehension is generally more compact and
# faster than normal functions and loops for creating list,Set and Dictionary.

a=[2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
b=[]
c=[]

# for item in a:
#     if item%2==0:
#         b.append(item)

# print(b)

b=[item for item in a if item%2==0]    #----------> Inline for loop with if statement inside list.
print(b)

for item in a:
    if item%3==0:
        c.append(item)

print(c)


# t=[1,2,4,2,1,2,3,4]
set={i for i in a}
print("-----------------------Printing Set Data--------------------------")
print(set)


# Recursive Function (Recursion) can be defined as the function calling itself.



# n!= 1 x 2 x 3 x 4 x ........ x n

# n=4
# fact=1

# for i in range(4):
#     fact= fact*(i+1)

# print(fact)


def fact_iter(n):
    fact=1

    for i in range(n):
        fact= fact*(i+1)

    return fact



print (f"Iterative Function with value 6 : {fact_iter(6)}")
f=fact_iter(5)
print(f"Iterative Function with value 5 : {f}")



def fact_recur(n):
    if n==1 or n==0:
        return 1
    return n* fact_recur(n-1)


print(f"Recursive Function with value 5 : {fact_recur(5)} ")


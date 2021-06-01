# Reduce applies a rolling computation to sequential pair of elements. function can be lambda.

from functools import reduce    # Reduce imported from functools, syntax: reduce(function,iterable object)

add=lambda num1,num2: num1+num2
l1=[1,3,5,7,9,11]

val= reduce(add,l1)

print(val)
print(type(val))



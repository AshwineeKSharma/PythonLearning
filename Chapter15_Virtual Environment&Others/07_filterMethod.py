# filter creates the list of items for which the function returns true
#   Can be used with lambda function
# syntax: filter(function, iterable object) ---------------> i.e List,Tuple etc.
#


def greaterThan5(num):
    if num > 5:
        return True

    else:
        return False

g10=lambda num: num>10

l1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,22,24,26,28,30]


fl = filter(greaterThan5, l1)
fl2=filter(g10,l1)
print(list(fl))
print(list(fl2))



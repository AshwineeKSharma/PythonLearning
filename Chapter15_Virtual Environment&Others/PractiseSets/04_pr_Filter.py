# WAP to filter a list of numbers which are divisible by 5.
def divBy5(num):
    if num%5==0:
        return True

    else:
        return False


l1=[2,4,6,8,10,12,14,15,16,18,20,25,30]
a=filter(lambda a: a%5==0,l1)      #---------------> Inline Method.
fil=filter(divBy5,l1)

print(list(fil))
print(list(a))




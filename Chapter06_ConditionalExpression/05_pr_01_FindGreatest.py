# WAP to find the greatest of the four numbers entered by the user


a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
c=int(input("Enter 3rd Number :"))
d=int(input("Enter 4th Number :"))

if(a>b and a>c and a>d):
    print("The First Number {} is the greatest among {},{},{},{}".format(a,a,b,c,d))


elif(b>a and b>c and b>d):
    print("The Second Number {} is the greatest among {},{},{},{}".format(b,a,b,c,d))


elif(c>a and c>b and c>d):
    print("The Third Number {} is the greatest among {},{},{},{}".format(c,a,b,c,d))



elif(d>a and d>b and d>c):
    print("The Fourth Number {} is the greatest among {},{},{},{}".format(d,a,b,c,d))


else:
    print("Is there any error in the input?")


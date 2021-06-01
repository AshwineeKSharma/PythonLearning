# WAP to display a/b where a and b are integers.
# if b= 0, display infinite by handling Division by zero.

try:
    a= int(input("Enter your First Number : "))
    b= int(input("Enter your Second Number : "))
    c= a/b
    print(c)

except ZeroDivisionError as e:
    val="Infinite"
    print(f"Value when Divisible by Zero is : {val} ")



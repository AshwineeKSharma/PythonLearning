# WAP to convert celcius into Farenheit using Function 


def tempConversion(temp):
    Ftemp=(temp*1.8)+32
    return print(f"{temp} degree Celsius equals to :  {Ftemp} degree Farenheit.")




temp=float(input("Enter The Temperature in Celcius : "))
tempConversion(temp)

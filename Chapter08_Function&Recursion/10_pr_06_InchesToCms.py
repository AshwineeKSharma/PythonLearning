# WAP to convert inches(in) to cemtimeters(cms) using Function 

def lenConversion(inch):
    cms=inch*2.54
    return print(f"The Value of {inch} inch is {cms} Centimeters.")


inch=float(input("Enter The Length in inch : "))

lenConversion(inch)

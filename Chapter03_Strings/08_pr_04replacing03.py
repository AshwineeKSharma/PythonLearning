# WAP to detect double spaces in a string and replace it with single space.

status="this is just the test status to find the double  spaces in between the given string. let's hope this thing works."
status=status.capitalize()
Ds=status.replace("  "," ")
print(Ds)

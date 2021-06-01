# A list contains the multiplication table of 7. WAP to convert it to a vertical string of same numbers.

from typing import List, Type


mul7=[str(i*7) for i in range(1,11)]

print(mul7)

verticalTable= "\n" .join(mul7)

print(verticalTable)
print(type(verticalTable))












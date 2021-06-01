# Create a class with class attribute a;
# create an object from it and set a directly 
# using object a=0. does this change the class attribute.

class Sample:
    a="Simple"



obj=Sample()
obj.a="Thoughtful"

print(Sample.a)
print(obj.a)



# A variable declared outside of the function or in global scope is known as a global variable.
# This means that a global variable can be accessed inside or outside of the function.

name="Aaryan"   #------------------------> Global Variable


def getName():
    global name #------------------------> Re-using global variable inside a function ----- > use global Variable
    print(name)
    name="Sambhujit"    #---------------------------> Local Variable / Changes global variable Value. 
    print(name)



getName()

print(name)

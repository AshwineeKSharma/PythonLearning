#Sets Method are the inbuilt functions(Methods) used to simplify the task for the user.



s3= set()
print(type(s3))


#------- Adding Values to the Empty Set----------

s3.add(10)          #add() method is used to add the value into the set.


s3.add(12)


s3.add(14)


# s3.add([2,3,4])   # Adding List to the set will throw the error as List are not Hashable i.e user can change it's value over Lifetime.
s3.add((50,60,80,100))  # Adding Tuples to the Set as they are hashable i.e user cannot change it's value over lifetime.


# s3.add({4:5})  # Adding Dictionary also throws the error as Dictionary are also not Hashable.

print(type(s3))     #type() method is used to display the datatype of variable.

print(s3)


#--------- Length of the set-------------

print(len(s3))      #len(variable) method used to determine the length of given set.



#--------- Removing Values from the set-------------


s3.remove(10)       #remove(value) method used to remove the value inside the set.


s3.remove((50,60,80,100)) # removing tuple from the set.


# s3.remove(33)       #removing undefined value inside the set throws an error.




s3.pop()     # Removes any arbitrary value from the set.


# s3.clear()        # Method used to empty the set.


u=s3.union({1,3,5,7})           #union() method is used to show union value with another set
i=s3.intersection({1,3,5,7})    #intersection() method is used to show the intersected value among two or more set.


print(s3)
print(u)   #Prints the union values
print(i)    # Prints The Intersected values.









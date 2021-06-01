# Dictionary Methods are the inbulit functions(Methods) used to perform various task related to the dictionary.



dict1 = {
  "name": "Ashwinee Kumar Sharma",
  "age": "30",
  "profession": "Chef",
  "marks": [1,3,5,7,9],   # Assigning List as a value to the Key.
  1:2,

    #Defining another dictionary inside the dictionary(Nested Dictionary)
"dict2":
{
    "hobbies": "Singing & Dancing "
}

}



# ---------------- Dictionary Methods-------------------


print(dict1.keys())   # print(dict1.keys()) Method used to display all the Keys inside the Dictionary


print(dict1.values()) # print(dict1.values()) is used to display only the values inside the dictionary.  


print(list(dict1.keys())) # Prints the content of dictionary by converting it to the list.


print(type(dict1.keys()))  # print(type(dict1.keys())) Method used to identify the type.



print(dict1.items())        # print(dict1.items()) method used to display all the Key Value Pairs Seperately inside the Dictionary.


print(dict1)


# ------ Defining new dictionary with Key Value Pairs for updating the existing dictionary 
update_dict={"Shyam" : "Friend"}

dict1.update(update_dict)  # dict1.update(update_dict) method used to update(Add) content to the dictionary

print(dict1)


print(dict1.get("Shyam"))  # Returns the value assigned to the key "Shyam".
print(dict1["Shyam"])      # Returns the value assigned to the key "Shyam".

#-------------- Differentiate Between the .get() method  and [] syntax-------------
print(dict1.get("Shyam2"))  # Returns None if the given Key is not available in the dictionary.
# print(dict1["Shyam2"])      # Throws Error if the given key is not available in the dictionary.











# Dictionary is a data container used to store data/values in key:value pairs
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


dict1 = {
  "Name": "Ashwinee Kumar Sharma",
  "Age": "30",
  "Profession": "Chef",
  "Marks": [1,3,5,7,9],   # Assigning List as a value to the Key.

    #Defining another dictionary inside the dictionary(Nested Dictionary)
"dict2":
{
    "Hobbies": "Singing & Dancing "
}

}



print(dict1)   # Prints all keys with it's corresponding values inside dictionary.


print(dict1['Name']) # Prints assigned key's value. 


print(dict1['Marks'])  #Prints the List Value assigned to the Key "Marks"



print(dict1['dict2']['Hobbies']) #Printing The data inside another dictionary. 






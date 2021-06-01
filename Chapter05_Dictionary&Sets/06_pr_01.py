# WAP to create a dictionary of Nepali Words with values as their english translation. Provide user with an option to look it up.


MyDict={
    "Namaste" : "Greetings",
    "Kasko":"who's",
    "khana khanu bhayo?":" had your food?",
    "K cha hajur ko halkhabar" : "How are you doing",
    "Ka jadai hununcha?":"Where are you going?",
    "Byana ko khana ma k cha?":"What's in there for lunch?",
    "ka jana lako":" where are you going"

}
print("Options Are : ", MyDict.keys())
word=input("Enter Nepali Word For it's Meaning : ")
# print("The Meaning of the word you entered is ", MyDict[word] ) # This line will throw error if the key(word) is not available in the dictionary
print("The Meaning of the word you entered is ", MyDict.get(word) )






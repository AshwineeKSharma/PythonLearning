# WAP to Remove a word from the String and Strip at the same time using Function.


# The strip() method returns a copy of the string by removing both the leading 
# and the trailing characters (based on the string argument passed). 
# 
# e.g.   text= "  hello   this is    some text   "
#         print(text)
#         print(text.strip())




def remove_strip(string,word):
    newStr= string.replace(word,"")
    return newStr.strip()


this="      Harry is good   "

n=remove_strip(this,"Harry")
print(n)






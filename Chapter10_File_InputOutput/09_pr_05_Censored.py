# Repeat program 4 for a list of such words to be Censored. 

words=["donkey","monkey","hippo","fatso","gorilla"]

with open('D:\\Python Learning\\Chapter10_File_InputOutput\\test.txt','r') as fil:
    data=fil.read()
for word in words:

    data=data.replace(word,"######")  # Replacing Text

with open('D:\\Python Learning\\Chapter10_File_InputOutput\\test.txt','w') as fil:
    data=fil.write(data)                # Updating file.

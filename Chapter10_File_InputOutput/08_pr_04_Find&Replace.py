# A file contain a word "Donkey" multiple times. So, WAP to replace the word "Donkey"
# with "######" by updating the same file.


with open('D:\\Python Learning\\Chapter10_File_InputOutput\\test.txt','r') as fil:
    data=fil.read()

data=data.replace("Donkey","######")  # Replacing Text

with open('D:\\Python Learning\\Chapter10_File_InputOutput\\test.txt','w') as fil:
    data=fil.write(data)                # Updating file.





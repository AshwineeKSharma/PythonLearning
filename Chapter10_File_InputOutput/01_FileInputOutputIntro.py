# A File can be defined as a data stored in a storage device.
# There are two types of files. They are : 1) Text Files(.txt,.c, etc.) 
#   and  2) Binary Files(.jpg,.dat, etc.)
# Python includes Functions for CRUD(Create, Read, Update, Delete) operation.

# Open() is a built-in function used to open Files and takes two parameters (Filename,Mode) Mode of Opening.
# e.g.  open(test.txt,r)------> r is for readonly mode for text file.
# e.g.  open(test.jpg,rb)------> r is for readonly mode for binary file.
# Modes for Opening a File (r-read, w-write, a-append, +-Updating)


# 1st parameter for file location with filename along with its extension. 2nd parameter for mode of Opening.

# fil=open('D:\Python Learning\Chapter10_File_InputOutput\\test.txt','r') 
fil=open('D:\Python Learning\Chapter10_File_InputOutput\\test.txt') # By Default the Mode is r. 
# data=fil.read()
data=fil.read(7)  # Reads first 7 character from the file.
print(data)
fil.close()



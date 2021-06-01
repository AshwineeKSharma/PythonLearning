
# Read Function

fil=open('D:\Python Learning\Chapter10_File_InputOutput\\test.txt','r') 
data=fil.read()
print(data)
fil.close()



# Write Function in Write mode also executes everytime.
fil=open('D:\Python Learning\Chapter10_File_InputOutput\\another.txt','w') 
data=fil.write("This is the Write Method to write contents in files (.txt) format.  ")
fil.close()



# Append Function  appends data every time the program executes.

# fil=open('D:\Python Learning\Chapter10_File_InputOutput\\another.txt','a') 
# data=fil.write("Append this to the File.  ")
# fil.close()



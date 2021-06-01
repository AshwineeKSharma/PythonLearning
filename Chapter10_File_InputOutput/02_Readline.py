# fil=open('D:\Python Learning\Chapter10_File_InputOutput\\test.txt','r') 
fil=open('D:\Python Learning\Chapter10_File_InputOutput\\test.txt') # By Default the Mode is r. 
data=fil.readline()

 # readlines() method will return all the lines
 # in a file in the format of a list where each element is a line in the file.

# data=fil.readlines() 
print(data)
fil.close()
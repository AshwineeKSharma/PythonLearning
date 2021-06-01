# The Best way to open and close the file automatically  is the with Statement.
# Can be Used With All File functions with methods(functions).
# Also Knows as Context Manager.


with open('D:\Python Learning\Chapter10_File_InputOutput\\test.txt','r') as fil:
    data=fil.read()
print(data)





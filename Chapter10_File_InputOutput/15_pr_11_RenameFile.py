# WAP to rename a file to "renamed_by_python.txt" 
import os



oldname="D:\\Python Learning\\Chapter10_File_InputOutput\\poem2.txt"
newname="D:\\Python Learning\\Chapter10_File_InputOutput\\renamed_by_python.txt"

with open(oldname) as fil:
    data=fil.read()

with open(newname, "w") as fil:
    fil.write(data)


    os.remove(oldname)
    




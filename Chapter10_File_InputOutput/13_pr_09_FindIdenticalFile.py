# WAP to find out whether a file is identical & matches the content of another file. 


file1="D:\\Python Learning\\Chapter10_File_InputOutput\\testcopy.txt"
file2= "D:\\Python Learning\\Chapter10_File_InputOutput\\test.txt"

with open(file1) as fil:
   data1=fil.read()

with open(file2) as fil:
   data2=fil.read()

   if data1==data2:
       print("Both Files are identical")

   else:
        print("No They are not")





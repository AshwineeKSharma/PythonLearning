# WAP to make the copy of a text file "test.txt". 



with open("D:\\Python Learning\\Chapter10_File_InputOutput\\test.txt", "r") as fil:
    data=fil.read()




with open("D:\\Python Learning\\Chapter10_File_InputOutput\\testcopy.txt", "w") as fil:
    fil.write(data)
    

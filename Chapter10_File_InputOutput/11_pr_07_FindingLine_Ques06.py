# WAP to find out the line number where "python" is present from Question no. 6. 


# WAP to mine a Log file and find out the line number where it contains "python" . 

data=True
i=1
with open("D:\\Python Learning\\Chapter10_File_InputOutput\\log.txt","r") as fil:
    
    while data:
        
        data=fil.readline().lower()
        
        if ("python" in data):
            print(f"python keyword is found in the file, in line no : {i}")
            print(data)
        else:
            print("Did not find the keyword.")

        i+=1



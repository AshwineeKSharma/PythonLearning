# WAP to mine a Log file and find out whether it contains "python". 


with open("D:\\Python Learning\\Chapter10_File_InputOutput\\log.txt","r") as fil:
    data=fil.read().lower()
    if ("python" in data):
        print("python keyword is found in the file.")
        
    else:
        print("Did not find the keyword.")
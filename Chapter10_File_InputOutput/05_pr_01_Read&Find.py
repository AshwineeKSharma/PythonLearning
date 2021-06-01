# WAP to read the text from the given file "poem.txt" and find 
# out whether it contains the word "twinkle". 

with open('D:\Python Learning\Chapter10_File_InputOutput\\poem.txt','r') as fil:
    data=fil.read()
    if "twinkle" in data:
        print("twinkle is present in the poem")

    else:
        print("Sorry!!! No twinkle found.")
print(f"\n\n\n{data}")




